/*
    Faça um programa que receba a média de um aluno.
    Condições:
        Caso a média seja menor que 5: Imprima "Reprovado"
        Caso a média seja maior ou igual a 5: Imprima "Recuperação"
        Caso a média seja maior que 7: Imprima "Aprovado"
*/

const {gets, print} = require ('./exercicios_export.js');

const media = gets ();

if (media < 5){
    print ('Reprovado');
} else if (media >=  5 && media < 7){
    print ('Recuperação');
} else {
    print ('Aprovado');
}