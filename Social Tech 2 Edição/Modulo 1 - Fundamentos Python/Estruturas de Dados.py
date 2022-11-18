"""
Estrutura de dados podem ter 4 tipos:
    List    [1, 2, 3, 4] = Ordenada e mutável;
    Tuple   (1, 2, 3, 4) = Ordenada e imutável;
    Set     {1, 2, 3, 4} = Não ordenada, mutável e valores únicos;
    Dict    {'a':1, 'b':2, 'c':3} = Mapeamento (key:value), não ordenada e mutável;
"""



""""
LIST (Lista):
"""

lista1 = [1, 2, 3, 4]; 
lista2 = [1, 3, 4, 2];
print(lista1, lista2); #lista1 e lista2 são listas diferentes, pois os valores da lista tem ordens diferentes 

#Podemos valiar isso comparando as duas listas com o operador '==', exemplo:
lista1 = [1, 2, 3, 4]; 
lista2 = [1, 3, 4, 2];
print (lista1 == lista2); #O valor retornado deve ser False, pois são listas diferentes, apesar dos mesmos valores dentro da lista, eles estão em ordens diferentes

#A estrura de dados tipo List pode ter valores heterogênios:
lista1 = [2, 'a', 5.44, True, None]; # Essa lista contem valores de varios tipos: Inteiro (2), String (a), Float (5.44), Boolean (True) e Null (none);

#As listas podem estar dentro de outras listas (listas aninhadas):
lista1 = [1, 2, 3, ['a', 'letra'], 7, [4,89, True, ['string', 55], 128, 'casa'], 57,558, False];

#Listas também podem ser vazias:
lista1 = [];

#Para acessar valores especificos (indices) de uma lista precisamos especificar o indice desejado (por padrão toda lista começa com indice 0):
#Odem do indice: 0  1   2   3   4   5
lista1        = [1, 2,  3,  4,  5,  6];
print(lista1[0]); # Na console o valor retornado será o número 1, pois ele está no indice 0.
print(lista1[3]); # Na console o valor retornado será o número 4, pois ele está no indice 3. 

#É possível acessar os indices por intervalos:
#Odem do indice: 0  1   2   3   4   5
lista1        = [1, 2,  3,  4,  5,  6];
print(lista1[0:3]); # Na console o valor retornado serão os números 1, 2 e 3 (ordenados), pois foi especificado que os valores entre os indices 0 e 3 devem ser retornados.
print(lista1[:]);   # Neste exemplo não foi especificado um intervalo especifico, então o valor retornado na console será a list inteira.
print(lista1[-1]);  # Neste exemplo o valor retornado será o número 6, pois quando especificamos o indice -1 ele lê o indice de forma inversa.

#Abaixo iremos utilizar uma estrutura de repetição com 'for' junto com listas para encontrarmos a maior idade:
listaIdades = [10, 23, 55, 37, 80, 27, 78, 15];
maior_idade = listaIdades[0] #A variavél maior_idade deve receber algum valor inicial para que a estrutura de repetição possa trabalhar, nesse caso escolhemos o primeiro indice
for idade in listaIdades:
    if idade > maior_idade: 
        maior_idade = idade
print(maior_idade);

#É possível adicionar um valor e realizar operações em uma lista utilizando .append():
lista1 = [1, 2, 3, 4]; 
lista1.append(55);      #Aqui especificamos que o valor 55 será adicionado ao final da lista, neste caso logo após o valor 4.
lista1.append(21/2)     #Ao final da lista será realizada a operação de divisão.
print(lista1)

#É possível alterar ou substituir valores de uma lista:
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista1[1] = 'casa'          #Aqui especificamos que a string 'casa' será atribuída no indice 1, logo o valor 2 (que está no indice 1) será substituido por 'casa'.
lista1[-1] = lista1[-1] + 2 #Aqui especificamos que o ultimo indice deve receber o seu proprio valor + 2, logo o resultado devera ser 9.
lista1.remove(4)            #O valor 4 será removido da lista (note que estamos declarando o valor e não o indice).
print(lista1)

#Concatenação '+', repetição '*' e filiação 'in' de listas:
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [2, 'a', 80, True, 8.22]

print(lista1 + lista2)  #As listas 1 e 2 serão concatenadas em uma só lista.
print(lista1 * 4)       #A lista 1 será repetida 4 vezes seguidas.
print(10 in lista2)     #Verificar se o valor 10 está na lista2 e retorna True ou False

#Funções úteis:
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [2, 'a', 80, True, 8.22]

print(len(lista2))      #Retorna o tamanho da lista2
print(sum(lista1))      #Retorna a soma dos valores da lista1 (funciona somente com valores númericos)
print(max(lista1))      #Retorna o maior valor da lista1 (funciona somente com valores númericos)



"""
TUPLE (Tuplas)
Tuplas são muito semelhantes às listas, porém suas declaração é realizada com '()' ao invés de '[]' e seus valores são fixos (imutáveis)
Tornam seu codigo mais seguro uma vez que evitam que condigo que não precisam sofrer alterações sofram alterações.
Podem ser utilizadas como chaves de dicionários.
São mais rapidas quê listas
"""
tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tupla1)


"""
SET (Conjuntos)
A ordem dos valores dos conjuntos não importam, não podem ser alterados e valores repetidos são descartados
"""

conjunto1 = {10, 1, 3, 6}
conjunto2 = {3, 6, 10, 1}
print(conjunto1 == conjunto2)                  #O valor retornado deve ser True, pois os dois conjuntos possuem os mesmos valores apesar da ordem ser diferente

#Quando um set (conjunto) tem valores heterogênos ele ordena os valores na seguinte prioridade, Booleanos, Inteiros, Floats, Strings e Nulos
#No caso de valores Booleanos, True = 1 e False = 0. Assim no Set (conjunto) ele ira organizar False como prioritario a True
conjunto1 = {3, 'b', True, None, 6.88}
print(conjunto1)

#Operação de união
conjunto1 = {10, 1, 3, 6}
conjunto2 = {22, 16, 77, 10}

print(conjunto1 | conjunto2)                    #Os valores dos dois sets (conjuntos) serão unidos (nota, o valor 10 será removido pois é repetido nos dois conjuntos)
print(conjunto1.union(conjunto2))               #Também retorna a união dos dois conjuntos, nesse caso utilizamos o metodo .union() ao invés do simbolo '|'

#Operação de interseção
conjunto1 = {10, 1, 3, 6}
conjunto2 = {22, 16, 77, 10}

print(conjunto1 & conjunto2)                    #Retorna o valor repetido nos dois conjuntos, no caso 10, utilizamos o operador '&'
print(conjunto1.intersection(conjunto2))        #Também retorna o valor repetido nos dois conjuntos utilizando o metodo .intersection()

#Operação de diferença
conjunto1 = {10, 1, 3, 6}
conjunto2 = {22, 16, 77, 10}

print(conjunto2 - conjunto1)                     #Retorna apenas os valores diferentes entre cada conjunto, nesse exemplo utilizamos o operador '-'
print(conjunto1.difference(conjunto2))           #Retorna apenas os valores diferentes entre cada conjunto, nesse exemplo utilizamos o metodo .difference()
#No exemplo acima é importante notar que a ordem de declaração dos conjuntos importa, note que o print com operador e print com metodo tem a ordem dos conjuntos invertidas para melhor entendimento


"""
DICT (Dicionario)
Dicionário é uma coleção de itens, cada elemento é um par 'key:value'
"""

#É possível ter chaves de tipos mistos
dicionario1 = {'nome': 'Gabriel', 'idade': '30', 'sexo': 'masculino'}
dicionario2 = {2: 'dois', 1: 'um', 20: 'vinte'}
dicionario3 = {20: 'vinte', 5.66: 'boolean', 'key': None}
print(dicionario1, dicionario2, dicionario3)
print(dicionario2[2])   #O valor retornado neste caso NÃO SERA O INDICE, e sim a CHAVE.



nome = "Teste"

start_num = int(100) 
end_num = int(500) 
cnt = start_num 
while cnt <= end_num: 
    
    
    if cnt % 2 == 0 and cnt % 7 == 0 and cnt % 5 == 0: 
        print(cnt, " is divisible by 2, 5 and 7.") 
          
    
    cnt += 1
    
    
    # declaração das variáveis
inicio = 0
fim = 100
# verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim):
    if numero % 5 == 0:
        print(numero)
        
c= '5'+'5'
print (c)

d = (2 + 3) * 5 - 1
print(d)

e = True and False
print(e)

e = False and True
print(e)


# relação dos nomes
nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']
# estrutura que irá armazenar o número de letras de cada nome
qtd_letras = {}
# calcula o tamanho de cada nome (em número de letras) e armazena o valor na estrutura
for nome in nomes:
    qtd_letras[nome] = len(nome)