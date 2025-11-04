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
  FOREIGN KEY (id_barbeiro) REFERENCES barbeiro(id_barbeiro)
);

CREATE TABLE atendimento (
  id_atendimento INT AUTO_INCREMENT PRIMARY KEY,
  data_hora_inicio DATETIME NOT NULL,
  data_hora_fim DATETIME NOT NULL,
  status ENUM('concluido', 'pendente', 'cancelado') DEFAULT 'concluido',
  id_barbeiro INT NOT NULL,
  id_cliente INT NOT NULL,
  id_servico INT,
  FOREIGN KEY (id_barbeiro) REFERENCES barbeiro(id_barbeiro),
  FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
  FOREIGN KEY (id_servico) REFERENCES servico(id_servico)
);
