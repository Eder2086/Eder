# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 21:08:06 2020

@author: no3803
"""

######### Variaveis

a = 3
print(a)
x = "Hellor World"
print (x[0:2])
print(x[-1])
print(x[2:])
a
print(x[1:-3])
texto = "Hello, Python!"


print("O bolo leva %f quilos de %s." %(1.5, "farinha"))
print("O bolo leva %.2f quilos de %s." %(1.5, "farinha"))
print("o bolo leva" + str(a) + "quilos de farinha")
print(x, texto)
print(2+3)
print(4%2)
print(3%2)

b = 4
b = b+1
b += 1

texto1 = "casa"
texto2 = "azul"

## BooLean

a=5
b=10
print ( a>=b )

print (a==b and a>=b)
print (a==b or a<=b)

while a < 10:
    print(a)
    a = a + 1

## Estrutura de controle

i = 30
o = 20
if i > o:
    print("i é maior do que o")    

num = float(input("Digite um numero:  "))
int(num)
    
import numpy as np
num2 = np.random.randint(10)
print(num2)
if num > num2:
    print ("Num2 é maior que 3")
elif num < num2:
    print ("Num2 é menor que 3")
elif num2 == num :
    print ("Num2 é igual a 3")
    
## listas

lista = [9,8,7]
print(lista)
lista2 = ["casa", "azul", 2, 6.5]
print(lista2)
    
print(lista2[1:3])
print(lista2[-3:])

texto = "Hello Phyton"
print(texto[3:])

lista.remove(8)    
texto.index(" ")

print(texto[:texto.index(" ")])

print(" " in texto)
print(6 in lista)

# Procura um caractere no texto:
c = input("digite um caractere")
if c in texto:
        print ("sim, esta no texto")
else:
    print("Ops!")

## Criar lista/ adicionar elementos

lista3 = [1,8,7,56,9,4]
print(len(lista3))
lista3.append(3)
print(lista3)
lista3.append([1,2,3])
lista3.extend([10,11,12])
lista_letras = list('asdasdasdsa')
lista3.extend(lista_letras)
lista3.append(lista_letras)

#Fazer um programa que solicita o nome de uma fruta e verifica se contem 
#na lista
#se a fruta existir imprimir sim
#caso contrario não

frutas = ["banana", "acabaxi", "manga"]
fruta = input("digite o nome da fruta: ")
if fruta in frutas:
    print("Sim, a fruta está na lista")
else:
    print("Não está na lista")
    
#gerar uma lista de numeros aleatorios
    #tamanho 10, solicitar um numero
    #verificar se o numero esta na lista
    
import numpy as np

numeros = np.random.randint(0,10,10) 

num = int(input("digite um numero:                      "))
if num in numeros:
    print("O número está na lista")
else:
    print("Não está na lista")

##converter int32 lista numpy em lista
    
numeros = list(numeros)
numeros.count(9)

##buscar numero maior da lista

maior = -1
for i in numeros:
    if i > maior:
        maior = i
print(maior)
        
menor = 100000000000
for i in numeros:
    if i < menor:
        menor = i
print(menor)

#Extrair valor maximo e minimo
maior2 = np.max(numeros)
print(maior2)

menor2 = np.min(numeros)
print(menor2)

#ordenação da lista
sorted_numeros = np.sort(numeros)




















    
    