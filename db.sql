CREATE DATABASE db;

CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(24) NOT NULL UNIQUE CHECK ( length(name) >= 2 )
    );

CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (36) NOT NULL UNIQUE CHECK ( length(name) >= 2 ),
        /*price DECIMAL (8, 2) NOT NULL CHECK ( price > 0 ),*/
        description VARCHAR (140) NOT NULL CHECK ( length(description) >= 10 ),
        category_id INTEGER NOT NULL,
        FOREIGN KEY ( category_id ) REFERENCES categories ( id ) ON DELETE RESTRICT
    );

CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(24) NOT NULL CHECK ( length(name) >= 2 ),
        email VARCHAR(24) NOT NULL UNIQUE CHECK ( length(name) >= 8 ) /*CHECK( "@" in name)*/
    );

CREATE TABLE IF NOT EXISTS statuses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(10) NOT NULL UNIQUE CHECK ( length(name) >= 2 )
    );

CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        status_id INTEGER NOT NULL,
        FOREIGN KEY ( user_id ) REFERENCES users ( id ) ON DELETE RESTRICT,
        FOREIGN KEY ( status_id ) REFERENCES statuses ( id ) ON DELETE RESTRICT
    );

CREATE TABLE IF NOT EXISTS order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        FOREIGN KEY ( order_id ) REFERENCES orders ( id ) ON DELETE RESTRICT,
        FOREIGN KEY ( product_id ) REFERENCES products ( id ) ON DELETE RESTRICT
    );

