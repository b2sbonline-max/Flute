-- FLUTE CRM PostgreSQL Schema
-- Production Ready

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    full_name VARCHAR(150),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);

CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);

CREATE TABLE IF NOT EXISTS tbl_registry (
    id SERIAL PRIMARY KEY,
    table_name_en VARCHAR(100) NOT NULL UNIQUE,
    table_name_he VARCHAR(100) NOT NULL,
    created_by INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(id)
);

CREATE INDEX idx_registry_created_by ON tbl_registry(created_by);

CREATE TABLE IF NOT EXISTS tbl_fields (
    id SERIAL PRIMARY KEY,
    table_name_en VARCHAR(100) NOT NULL,
    field_name_he VARCHAR(100) NOT NULL,
    field_name_en VARCHAR(100) NOT NULL,
    field_type VARCHAR(20) NOT NULL,
    field_position INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (table_name_en) REFERENCES tbl_registry(table_name_en) ON DELETE CASCADE
);

CREATE INDEX idx_fields_table ON tbl_fields(table_name_en);

INSERT INTO users (username, password, email, full_name, is_active)
VALUES ('admin', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5/tABqNhV2lCy', 'admin@flute.local', 'Administrator', TRUE)
ON CONFLICT (username) DO NOTHING;
