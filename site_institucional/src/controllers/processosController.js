var processosModel = require("../models/processosModel");

function receberDadosProcessos(req, res) {
    var fkTorre = req.body.fkTorreServer;
    // var limite = req.body.limiteServer;

    if (fkTorre == undefined) {
        res.status(400).send("A fkTorre do aeroporto está undefined!");
    } else {
        processosModel.listarProcessos(fkTorre)
            .then(
                function (resultado) {
                    console.log(`\nProcessos: ${resultado}`);
                    res.json(resultado)
                }
            ).catch(
                function (erro) {
                    console.log(erro);
                    console.log("\nHouve um erro ao receber os processos! Erro: ", erro.sqlMessage);
                    res.status(500).json(erro.sqlMessage);
                }
            )
    }
}

module.exports = {
    receberDadosProcessos
}