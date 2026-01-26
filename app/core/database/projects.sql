CREATE DATABASE IF NOT EXISTS DB_MINDDAYCARE;
USE DB_MINDDAYCARE;

CREATE TABLE IF NOT EXISTS tbl_users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    telefone CHAR(11) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active ENUM('0',"1") DEFAULT '1'
);

-- Tabela de Desabafos
CREATE TABLE IF NOT EXISTS tbl_desabafo(
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_user INT NOT NULL,
    humor VARCHAR(30),
    descricao TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_usuario_desabafo 
        FOREIGN KEY (id_user) REFERENCES tbl_users(id) 
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tbl_refresh_token(
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_user INT NOT NULL,
    token_hash TEXT NOT NULL, 
    expires_at DATETIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_user_token
        FOREIGN KEY (id_user) REFERENCES tbl_users(id)
        ON DELETE CASCADE
);



SELECT * FROM tbl_users;