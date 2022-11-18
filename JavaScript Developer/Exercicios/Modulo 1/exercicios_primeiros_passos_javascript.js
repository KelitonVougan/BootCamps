/* Programa para calcular o valor de uma viagem.

    Terá 3 variáveis, sendo elas:
        1 - Preço do combustível;
        2 - Gasto médio de combustível do carro por KM;
        3 - Distancia em KM da viagem;

*/

const precoEtanol = 5.79;
const precoGasolina = 6.78;
const kmPorLitros = 10;
const distanciaViagemKm = 100;
const tipoCombustivel = 'Gasolina';

const mediaCarro = distanciaViagemKm / kmPorLitros;

if (tipoCombustivel === 'Etanol') {
  const gastoCombustivelViagem = mediaCarro * precoEtanol;
  console.log(gastoCombustivelViagem.toFixed(2));
} else {
  const gastoCombustivelViagem = mediaCarro * precoGasolina;
  console.log(gastoCombustivelViagem.toFixed(2));
}

/* 
  Faça um algoritimo que dado as 3 notas tiradas por um aluno em um semetre da faculdade calcule e imprima
  a sua média e a sua classificação conforme a tabela abaixo:

  Média = (nota 1 + nota 2 + nota 3) / 3;

  Classificação:
    - Média menor que 5, reprovado;
    - Média entre 5 e 7, recuperação;
    - Média acima de 7, aprovado;
*/

const nota1 = 10;
const nota2 = 9;
const nota3 = 8;

const mediaNotas = (nota1 + nota2 + nota3) / 3;
//console.log(mediaNotas);

if (mediaNotas < 5) {
  console.log("Você está reprovado, sua nota foi: " + (mediaNotas.toFixed(2)));
} else if (mediaNotas >= 5 && mediaNotas <= 7) {
  console.log('Você está na média, sua nota é: ' + (mediaNotas.toFixed(2)));
} else {
  console.log('Você está aprovado, sua nota é: ' + (mediaNotas.toFixed(2)));
}

/* 
  Calculo de IMC
  IMC = peso / (altura * altura)
  Abaixo de 10.5: Abaixo do peso;
  Entre 18.5 e 25: Peso normal;
  Entre 25 e 30: Acima do peso;
  Entre 30 e 40: Obeso;
  Acima de 40: Obesidade grave;
*/

const peso = 150;
const altura = 1.75;

const imc = peso / Math.pow (altura, 2);


if (imc < 10.5) {
  console.log('Você está abaixo do peso, seu IMC é: ' + (imc.toFixed(2)));
} else if (imc >= 18.5 && imc < 25) {
  console.log('Você está no peso ideal, seu IMC é: ' + (imc.toFixed(2)));
} else if (imc >= 25 && imc < 30) {
  console.log('Você está acima do peso, seu IMC é: ' + (imc.toFixed(2)));
} else if (imc >= 30 && imc < 40) {
  console.log('Você está obeso, seu IMC é: ' + (imc.toFixed(2)));
} else {
  console.log('Você tem obesidade grave, seu IMC é: ' + (imc.toFixed(2)));
}

/*
  Calcule o que deve ser pago em um produto, considerando o preço normal da etiqueta e a escolha da forma de pagamento:
  Debito:             10% desconto;
  Em especie ou PIX:  15% de desconto;
  Parcelado 2x:       Preço normal etiqueta;
  Acima de 2x:        Preço normal etiqueta + 10% juros;
*/

const precoEtiqueta = 100;

const formaPagamento = 1

if (formaPagamento === 1){
  console.log(precoEtiqueta - (precoEtiqueta * 0.1));
} else if (formaPagamento === 2) {
  console.log(precoEtiqueta - (precoEtiqueta * 0.15));
} else if (formaPagamento === 3){
  console.log(precoEtiqueta);
} else {
  console.log(precoEtiqueta + (precoEtiqueta * 0.1));
}


