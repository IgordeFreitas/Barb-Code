CREATE TABLE barbeiro(
  id_barbeiro SERIAL PRIMARY KEY,
  nome VARCHAR(70) NOT NULL,
  CPF VARCHAR(14) NOT NULL UNIQUE CHECK (cpf ~ '^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$'),
  email VARCHAR(80) NOT NULL UNIQUE CHECK (email LIKE '%@%'),
  senha VARCHAR(12) NOT NULL,
  telefone VARCHAR(20) NOT NULL
);

CREATE TABLE cliente(
  id_cliente SERIAL PRIMARY KEY,
  nome VARCHAR(70) NOT NULL,
  email VARCHAR(80) NOT NULL UNIQUE CHECK (email LIKE '%@%'),
  telefone VARCHAR(20) NOT NULL,
  senha VARCHAR(12) NOT NULL
);

CREATE TABLE servico(
  id_servico SERIAL PRIMARY KEY,
  nome VARCHAR(40) NOT NULL UNIQUE,
  preco DECIMAL(6,2) NOT NULL CHECK (preco > 0)
);

CREATE TABLE agenda(
  id_agenda SERIAL PRIMARY KEY,
  data_hora TIMESTAMP NOT NULL,
  status VARCHAR(20) DEFAULT 'disponivel' CHECK (status IN ('disponivel', 'reservado', 'cancelado')),
  id_barbeiro INT REFERENCES barbeiro(id_barbeiro)
);

CREATE TABLE atendimento(
  id_atendimento SERIAL PRIMARY KEY,
  data_hora_inicio TIMESTAMP NOT NULL,
  data_hora_fim TIMESTAMP NOT NULL,
  status VARCHAR(20) DEFAULT 'concluido' CHECK (status IN ('concluido', 'pendente', 'cancelado')),
  id_barbeiro INT NOT NULL REFERENCES barbeiro(id_barbeiro),
  id_cliente INT NOT NULL REFERENCES cliente(id_cliente),
  id_servico INT REFERENCES servico(id_servico)
);