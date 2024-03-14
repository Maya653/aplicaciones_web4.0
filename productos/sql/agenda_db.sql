CREATE DATABASE IF NOT EXISTS agenda_db;

USE agenda_db;

CREATE TABLE IF NOT EXISTS productos(
    id_producto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    producto VARCHAR(50) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    precio INT NOT NULL,
    existencias INT NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET=latin1;

INSERT INTO productos(producto, descripcion, precio, existencias)
VALUES
('Zucaritas', 'cereal', 70, 5),
('Agua', 'botella de agua', 12, 14);

CREATE USER 'user_agenda'@'localhost' IDENTIFIED BY 'Agenda.2024';
GRANT ALL PRIVILEGES ON agenda_db.* TO 'user_agenda'@'localhost';
FLUSH PRIVILEGES;
