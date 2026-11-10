import importlib.util
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / 'prepare_issue_leads.py'
spec = importlib.util.spec_from_file_location('prepare_issue_leads', MODULE)
prepare = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prepare)

class PrepareTests(unittest.TestCase):
    def test_preserves_unreviewed_status_and_source_identity(self):
        rows = [{'url':'https://github.com/example/project/issues/42','title':'Example', 'source_project':'example/project', 'issue_number':'42'}]
        data = prepare.convert(rows, 'batch-1')
        self.assertEqual(len(data['sources']),1)
        self.assertEqual(len(data['entities']),2)
        self.assertEqual(len(data['assertions']),1)
        self.assertEqual(data['assertions'][0]['evidence_status'],'lead')
        self.assertEqual(data['sources'][0]['url'],rows[0]['url'])
    def test_exact_duplicate_is_deduplicated(self):
        row = {'url':'https://github.com/example/project/issues/42','title':'Example', 'source_project':'example/project', 'issue_number':'42'}
        self.assertEqual(len(prepare.convert([row,row], 'batch-1')['assertions']),1)
    def test_conflicting_duplicate_is_rejected(self):
        a = {'url':'https://github.com/example/project/issues/42','title':'Example', 'source_project':'example/project', 'issue_number':'42'}
        b = dict(a, title='Different')
        with self.assertRaises(ValueError): prepare.convert([a,b], 'batch-1')

if __name__ == '__main__': unittest.main()
