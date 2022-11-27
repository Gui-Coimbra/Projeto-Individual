var database = require("../database/config")

function listarProcessos(fkTorre) {
    if(process.env.AMBIENTE_PROCESSO == "desenvolvimento") {
        var instrucao = `SELECT nome, max(porcentagemCpu) as 'cpu', pid, usuario FROM processos 
        WHERE DAY(horario) >= DAY(now()) 
        GROUP BY nome, pid, usuario ORDER BY max(porcentagemCpu) DESC LIMIT 10;`;
        console.log("Executando a instrução SQL: \n" + instrucao);    
    } else if(process.env.AMBIENTE_PROCESSO == "producao") {
        var instrucao = `SELECT TOP ${limite} * FROM vw_Processos WHERE fkTorre = ${fkTorre};`;
        console.log("Executando a instrução SQL: \n" + instrucao);    
    }
    return database.executar(instrucao);
}

function deletarProcesso(pid) {
    var instrucao = `INSERT INTO deletarPid(pid) values (${pid});`
    return database.executar(instrucao);
}

module.exports = {
    listarProcessos,
    deletarProcesso
};