CREATE DATABASE IF NOT EXISTS BarbCode
CHARACTER SET 'utf8mb4'
COLLATE utf8mb4_unicode_ci;
USE BarbCode;

CREATE TABLE barbeiro (
  id_barbeiro INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(70) NOT NULL,
  cpf VARCHAR(14) NOT NULL UNIQUE,
  email VARCHAR(80) NOT NULL UNIQUE,
  senha VARCHAR(12) NOT NULL,
  telefone VARCHAR(20) NOT NULL,
  CONSTRAINT chk_cpf_format CHECK (cpf REGEXP '^[0-9]{3}\\.[0-9]{3}\\.[0-9]{3}-[0-9]{2}$'),
  CONSTRAINT chk_email_format CHECK (email LIKE '%@%')
);

CREATE TABLE cliente (
  id_cliente INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(70) NOT NULL,
  email VARCHAR(80) NOT NULL UNIQUE,
  telefone VARCHAR(20) NOT NULL,
  senha VARCHAR(12) NOT NULL,
  CONSTRAINT chk_email_cliente CHECK (email LIKE '%@%')
);

CREATE TABLE servico (
  id_servico INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(40) NOT NULL UNIQUE,
  preco DECIMAL(6,2) NOT NULL,
  CONSTRAINT chk_preco_positivo CHECK (preco > 0)
);

CREATE TABLE agenda (
  id_agenda INT AUTO_INCREMENT PRIMARY KEY,
  data_hora DATETIME NOT NULL,
  status ENUM('disponivel', 'reservado', 'cancelado') DEFAULT 'disponivel',
  id_barbeiro INT,
  FOREIGN KEY (id_barbeiro) REFERENCES barbeiro(id_barbeiro) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE atendimento (
  id_atendimento INT AUTO_INCREMENT PRIMARY KEY,
  data_hora_inicio DATETIME NOT NULL,
  data_hora_fim DATETIME NOT NULL,
  status ENUM('concluido', 'pendente', 'cancelado') DEFAULT 'concluido',
  id_barbeiro INT,
  id_cliente INT,
  id_servico INT,
  FOREIGN KEY (id_barbeiro) REFERENCES barbeiro(id_barbeiro) ON DELETE SET NULL ON UPDATE CASCADE,
  FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE atendimento_servico (
  id_atendimento_servico INT AUTO_INCREMENT PRIMARY KEY,
  id_atendimento INT NOT NULL,
  id_servico INT,
  FOREIGN KEY (id_atendimento) REFERENCES atendimento(id_atendimento),
  FOREIGN KEY (id_servico) REFERENCES servico(id_servico) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE barbeiro_servico(
  id_barbeiro_servico INT AUTO_INCREMENT PRIMARY KEY,
  id_barbeiro INT,
  id_servico INT,
  FOREIGN KEY (id_barbeiro) REFERENCES barbeiro (id_barbeiro) ON DELETE SET NULL ON UPDATE CASCADE,
  FOREIGN KEY (id_servico) REFERENCES servico (id_servico) ON DELETE SET NULL ON UPDATE CASCADE
);