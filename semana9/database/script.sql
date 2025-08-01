CREATE DATABASE saludtotal;
USE saludtotal;

CREATE TABLE Pacientes (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  Nombre VARCHAR(100) NOT NULL,
  Edad INT,
  Genero VARCHAR(10),
  HistorialMedico TEXT,
  Contacto VARCHAR(100)
);
