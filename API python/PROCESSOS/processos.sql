CREATE DATABASE processo;
USE processo;

drop table processos;
CREATE TABLE processos(
idProcesso INT PRIMARY KEY auto_increment,
nome VARCHAR(50),
porcentagemCpu DECIMAL(5,2),
pid VARCHAR(10),
usuario VARCHAR(50),
fkServidor INT,
horario datetime
);

select * from processos;

select * from processos where idProcesso = 15;
SELECT COUNT(*) FROM processos;

SELECT nome, max(porcentagemCpu) FROM processos WHERE DAY(horario) >= DAY(now()) 
AND MINUTE(horario) >= MINUTE(now()) GROUP BY nome ORDER BY max(porcentagemCpu) DESC LIMIT 10;

SELECT nome, max(porcentagemCpu), pid, usuario FROM processos WHERE DAY(horario) >= DAY(now()) 
GROUP BY nome ORDER BY max(porcentagemCpu) DESC LIMIT 10;