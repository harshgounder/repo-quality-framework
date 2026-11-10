import importlib.util
import sqlite3
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / 'store.py'
spec = importlib.util.spec_from_file_location('store', MODULE)
store = importlib.util.module_from_spec(spec)
spec.loader.exec_module(store)

class StoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / 'evidence.sqlite'
        self.conn = store.connect(self.db)
        store.initialize(self.conn)
        self.data = {'sources':[{'id':'s1','url':'https://example.org/1','kind':'report','version':'unknown'}],
                     'entities':[{'id':'e1','kind':'observation','label':'observation'}, {'id':'e2','kind':'change','label':'change'}],
                     'assertions':[{'id':'a1','subject':'e1','predicate':'related_to','object':'e2',
                                    'source':'s1','locator':'body','evidence_status':'source_reported','note':'not independently reproduced'}]}
    def tearDown(self):
        self.conn.close(); self.tmp.cleanup()
    def test_unversioned_existing_database_is_rejected(self):
        other = store.connect(Path(self.tmp.name) / 'other.sqlite')
        try:
            other.execute('create table unrelated (id text)')
            with self.assertRaises(ValueError): store.initialize(other)
            self.assertEqual(other.execute('PRAGMA user_version').fetchone()[0],0)
        finally: other.close()
    def test_foreign_version_one_database_is_rejected(self):
        other = store.connect(Path(self.tmp.name) / 'foreign.sqlite')
        try:
            other.execute('PRAGMA user_version = 1')
            with self.assertRaises(ValueError): store.initialize(other)
        finally: other.close()
    def test_unsupported_schema_version_is_rejected(self):
        other = store.connect(Path(self.tmp.name) / 'future.sqlite')
        try:
            other.execute('PRAGMA user_version = 99')
            with self.assertRaises(ValueError): store.initialize(other)
        finally: other.close()
    def test_repeated_identical_load_is_idempotent(self):
        store.load(self.conn,self.data); store.load(self.conn,self.data)
        self.assertEqual(self.conn.execute('select count(*) from assertions').fetchone()[0],1)
    def test_conflict_rejects_whole_import(self):
        store.load(self.conn,self.data)
        data = {'sources':[{'id':'s2','url':'https://example.org/2','kind':'report','version':'unknown'},
                           {'id':'s1','url':'https://different.example/','kind':'report','version':'unknown'}], 'entities':[], 'assertions':[]}
        with self.assertRaises(ValueError): store.load(self.conn,data)
        self.assertEqual(self.conn.execute('select count(*) from sources').fetchone()[0],1)
    def test_dangling_reference_rolls_back(self):
        self.data['assertions'][0]['object']='missing'
        with self.assertRaises(sqlite3.IntegrityError): store.load(self.conn,self.data)
        self.assertEqual(self.conn.execute('select count(*) from sources').fetchone()[0],0)
    def test_invalid_evidence_status_is_rejected(self):
        self.data['assertions'][0]['evidence_status']='verified-because-we-said-so'
        with self.assertRaises(sqlite3.IntegrityError): store.load(self.conn,self.data)
        self.assertEqual(self.conn.execute('select count(*) from sources').fetchone()[0],0)

if __name__ == '__main__': unittest.main()
