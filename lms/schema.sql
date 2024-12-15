-- schema.sql
CREATE TABLE home_app (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    app_name TEXT NOT NULL,
    version TEXT NOT NULL,
    description TEXT NOT NULL
);
