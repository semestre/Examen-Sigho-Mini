CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    email TEXT,
    password TEXT,
    es_admin INTEGER DEFAULT 0
);

CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    categoria TEXT,
    precio REAL,
    stock INTEGER,
    nombre_categoria_legible TEXT
);

CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER,
    fecha TEXT
);

CREATE TABLE logs_acceso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_email TEXT,
    fecha TEXT,
    ip TEXT
);
