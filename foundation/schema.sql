PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS sources (
    id TEXT PRIMARY KEY, url TEXT NOT NULL, kind TEXT NOT NULL, version TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS entities (
    id TEXT PRIMARY KEY, kind TEXT NOT NULL, label TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS assertions (
    id TEXT PRIMARY KEY,
    subject TEXT NOT NULL REFERENCES entities(id),
    predicate TEXT NOT NULL,
    object TEXT NOT NULL REFERENCES entities(id),
    source TEXT NOT NULL REFERENCES sources(id),
    locator TEXT NOT NULL,
    evidence_status TEXT NOT NULL CHECK(evidence_status IN ('lead','source_reported','independently_checked','reproduced','disputed','inaccessible','unknown')),
    note TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS assertions_by_subject ON assertions(subject);
CREATE INDEX IF NOT EXISTS assertions_by_object ON assertions(object);
PRAGMA application_id = 1380271665;
PRAGMA user_version = 1;
