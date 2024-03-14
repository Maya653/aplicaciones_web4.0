CREATE TABLE IF NOT EXISTS productos(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    precio INT NOT NULL,
    existencias INT NOT NULL
);



INSERT INTO 
    productos(nombre, descripcion, precio, existencias)
VALUES
    ('Zucaritas', 'cereal', 70, 5),
    ('Agua', 'botella de agua', 12, 14);




CREATE USER 'user_agenda'@'localhost' IDENTIFIED BY 'Agenda.2024';
GRANT ALL PRIVILEGES ON agenda_db.* TO 'user_agenda'@'localhost';
FLUSH PRIVILEGES;
