#!/usr/bin/env python3
"""Small evidence graph prototype. Inputs are curated JSON, not untrusted code."""
import argparse
import json
import sqlite3
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIELDS = {
    'sources': ('id','url','kind','version'),
    'entities': ('id','kind','label'),
    'assertions': ('id','subject','predicate','object','source','locator','evidence_status','note'),
}

def connect(path):
    conn = sqlite3.connect(path)
    conn.execute('PRAGMA foreign_keys = ON')
    return conn

def initialize(conn):
    version = conn.execute('PRAGMA user_version').fetchone()[0]
    if version not in (0, 1):
        raise ValueError(f'unsupported schema version: {version}')
    app_id = conn.execute('PRAGMA application_id').fetchone()[0]
    existing = conn.execute("SELECT name FROM sqlite_master WHERE name NOT LIKE 'sqlite_%' LIMIT 1").fetchone()
    if version == 0 and (existing or app_id):
        raise ValueError('refusing to initialize a nonempty or owned database')
    if version == 1 and app_id != 0x52454631:
        raise ValueError('database does not belong to this prototype')
    conn.executescript((HERE / 'schema.sql').read_text(encoding='utf-8'))

def load(conn, snapshot):
    if set(snapshot) != set(FIELDS):
        raise ValueError('snapshot must contain exactly sources, entities, assertions')
    with conn:
        for table, fields in FIELDS.items():
            for record in snapshot[table]:
                if set(record) != set(fields) or any(not isinstance(record[k], str) or not record[k].strip() for k in fields):
                    raise ValueError(f'invalid {table} record')
                values = tuple(record[k] for k in fields)
                existing = conn.execute(f'SELECT {",".join(fields)} FROM {table} WHERE id=?', (record['id'],)).fetchone()
                if existing is not None:
                    if existing != values:
                        raise ValueError(f'conflicting {table} ID: {record["id"]}')
                    continue
                conn.execute(f'INSERT INTO {table} ({",".join(fields)}) VALUES ({",".join("?" for _ in fields)})', values)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('database', type=Path)
    parser.add_argument('snapshot', type=Path)
    args = parser.parse_args()
    snapshot = json.loads(args.snapshot.read_text(encoding='utf-8'))
    with connect(args.database) as conn:
        initialize(conn); load(conn, snapshot)
        for table in FIELDS:
            print(f'{table}: {conn.execute(f"SELECT count(*) FROM {table}").fetchone()[0]}')

if __name__ == '__main__': main()
