CREATE TABLE IF NOT EXISTS vehicules (
    id VARCHAR(32) PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    type VARCHAR(7) NOT NULL,
    max_speed INTEGER NOT NULL,
    acceleration INTEGER NOT NULL
);