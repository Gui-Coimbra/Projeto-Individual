CREATE DATABASE teste;
USE teste;

drop table processos;
CREATE TABLE processos(
idProcesso INT PRIMARY KEY auto_increment,
nome VARCHAR(50),
porcentagemCpu DECIMAL(5,2),
fkServidor INT,
horario datetime
);

INSERT INTO processos(nome, porcentagemCpu, fkServidor, horario) VALUES("ivan", 10.0, 1, now());

select * from processos where idProcesso = 15;
SELECT COUNT(*) FROM processos;

SELECT nome, max(porcentagemCpu) FROM processos WHERE DAY(horario) >= DAY(now()) 
AND MINUTE(horario) >= MINUTE(now()) GROUP BY nome ORDER BY max(porcentagemCpu) DESC LIMIT 5;