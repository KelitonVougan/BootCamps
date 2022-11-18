// Abaixo um array onde a variavel 'notas' recebe os valores pelo metodo '.push'
const notas = [];

notas.push(10);
notas.push(7);
notas.push(5);
notas.push(3);
notas.push(9);
notas.push(8);

// variavel 'soma' inicia sem valor, poís será utilizada na estrutura de repetição de 'for'
let soma = 0;

/* 
    Estrutura de repetição: notas.lenght realiza o incremento (em 1) até alcançar a quantidade total do
    array (array possui 6 valores nesse exemplo)
*/ 
for (let i = 0; i < notas.length; i++) {
    const nota = notas[i];
    soma = soma + nota;
}

// calculo da média
const media = soma / notas.length;
console.log(media);

// O codigo abaixo imprime a tabuada do número que você escolher
const numero = 50;

for (let i = 1; i <= 10; i++) {
    console.log(i * numero);
    
}

/* 
    Utilize o 'for' percorrer uma lista de números e imprime
    somente os números pares da lista     
*/
const listaDeNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

for (let i = 0; i < listaDeNumeros.length; i++) {
    const verificaPar = listaDeNumeros[i];
    if (verificaPar % 2 === 0){
        console.log(verificaPar);
    }   
}
