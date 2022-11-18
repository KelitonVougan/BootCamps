#CONCEITOS BASICOS DE NUMPY
#Em Numpy o Shape (formato) dos arrays pode ter até 3 eixos:
#       Eixo 0, Eixo 1 e Eixo 2 = (0, 1, 2) 
#       O Shape do seu array ira determinar a quantidade de linhas e colunas que ele tem





#Shape com 1 eixo
import numpy as np        #Importamos a biblioteca no Numpy

list = [1, 2, 3]          #Criamos um array
x = np.array(list)        #Criamos uma variável x e ela recebe np.array(list)

print(x.shape)            #Imprimimos x com o metodo .shape, isso nos mostrará o shape


#Shape com 2 eixos
import numpy as np        #Importamos a biblioteca no Numpy

list = [[1, 2, 3], [4, 5, 6]]          #Criamos um array
x = np.array(list)                     #Criamos uma variável x e ela recebe np.array(list)

print(x.shape)                         #Imprimimos x com o metodo .shape, isso nos mostrará o shape
#O resultado será (2, 3):
#  Eixo 0|           |-----------------
#        |  [1 2 3]                   |             | Ou seja, o eixo 0 representa a quantidade de linhas (2)
#        |  [4 4 6]          (2           3)        | O Eixo 1 representa a quantiade de colunas (3) 
#        |                  Eixo 0       Eixo 1
#        --------------
#           Eixo 1

#É possível mudar os valores dos arrays para inteiros
import numpy as np

list = [1, 2.5, 3]
x = np.array(list, dtype=int)   #adicionamos dtype=int para transformar tudo dentro do array para inteiros

print(x)

#Criando array contendo apenas zeros 
import numpy as np

list = (2, 3)           #Definimos o Shape 
x = np.zeros(list)      #metodo .zeros atribui zeros a todos os valores do array

print(x)

#Criando array com valores aleatorios
import numpy as np

list = (2, 3)                  #Definimos o Shape 
x = np.random.random(list)     #metodo .random.random atribui zeros a todos os valores do array

print(x)


#É possível acessar qualquer indice para ver seu valor
import numpy as np
          
x = np.linspace(start=10, stop=100, num=10)  #Aqui estamos utilizando o metodo .linspace com argumentos, o argumento start diz que o primeiro valor será 10, argumento stop diz que o ultimo será 100 e argumento num diz que será contado de 10 em 10

print(x[1])                        #Em x[1] estamos definindo que queremos ver o valor do indice número 1



#Caso desejado podemos ver o valor de mais de um indice (Slice)
import numpy as np
          
x = np.linspace(start=10, stop=100, num=10)  #Aqui estamos utilizando o metodo .linspace com argumentos, o argumento start diz que o primeiro valor será 10, argumento stop diz que o ultimo será 100 e argumento num diz que será contado de 10 em 10

print(x[1:3])                             

