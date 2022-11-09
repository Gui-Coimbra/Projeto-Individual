CREATE DATABASE teste;
USE teste;

CREATE TABLE processos(
idProcesso INT PRIMARY KEY auto_increment,
nome VARCHAR(50),
porcentagemCpu DECIMAL(5,2),
fkServidor INT,
horario datetime
);

/* INSERT INTO processo(nome, porcentagemCpu, fkServidor, horario) VALUES(%s, %s, %s, now())*/
select * from processos;