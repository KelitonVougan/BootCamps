/*
   No exercicio a seguir vamos construir um programa utilizando Programação Orientada a Objetos
   para obtermos o resultado do gasto realizado por um veiculo em uma viagem.

    Terá 3 variáveis, sendo elas:
        1 - Preço do combustível;
        2 - Gasto médio de combustível do carro por KM;
        3 - Distancia em KM da viagem;
*/

class Carro {
    marca;
    cor;
    gastoMedioPorKm;

    constructor (marca, cor, gastoMedioPorKm){
        this.marca = marca;
        this.cor = cor;
        this.gastoMedioPorKm = gastoMedioPorKm; 
    }

    calcularGastoViagem(distanciaemKm, precoCombustivel){
        return distanciaemKm * this.gastoMedioPorKm * precoCombustivel;
    }

}

const gurgel = new Carro ('Gurgel', 'Branco', 1 / 12);
console.log(gurgel.calcularGastoViagem(70, 8));

const uno = new Carro ('Fiat', 'Preto', 1 / 15);
console.log(uno.calcularGastoViagem(70, 5));

/*
    O exercicio a seguir apresenta um programa construido com Programação Orientada a Objetos
    para calcular o IMC de uma pessoa
*/

class Pessoa {
    nome;
    peso;
    altura;

    constructor (nome, peso, altura){
        this.nome = nome;
        this.peso = peso;
        this.altura = altura;
    }

    calcularImc(){
        return this.peso / (this.altura * this.altura);
    }
}

const andre = new Pessoa ('André', 70, 1.78);
console.log(andre.calcularImc())

const vitor = new Pessoa ('Vitor', 92, 1.80);
console.log(vitor.calcularImc())