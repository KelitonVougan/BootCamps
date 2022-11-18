n = 15
soma =0
contador = 0

while contador <= n:
    soma = soma + contador
    contador = contador + 1
    print(soma)
 
 
 
inicio = 100
fim = 500
   
for numero in range(inicio, fim):
    if numero % 2 == 0:
        print(numero, "É multiplo de 2")
    elif numero % 5 == 0:
        print(numero, 'É multiplo de 5')
    else:
        numero % 7 == 0
        print(numero, 'É multiplo de 7')
        
 
inicio = 0
fim = 1000
   
for numero in range(inicio, fim):
    if numero / 2 == 0:
        print(numero, "É multiplo de 2")
  