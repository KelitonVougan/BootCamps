/* 
    Podemos exportar e importar valores de um arquivo para outro (utilizando Nodejs). Para isso usamos 
    module.exports = {}. Module.exports é um objeto literal. 
    Para importar utilizamos require('./caminho_do_arquivo')

    Abaixo estamos exportando a função 'gets' e 'print' para o arquivo exercicios_import.js
*/

const entradas = [8];
let i = 0;

function gets (){
    const valor = entradas [i];
    i++;
    return valor;
}

function print (texto){
    console.log(texto);
}

module.exports = {gets, print};