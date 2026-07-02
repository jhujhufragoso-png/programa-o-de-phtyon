
arquivo: main.py

from ex1 import aleatorio
from ex2 import aleatorio2


aleatorio()
aleatorio2()

aquivo: ex2.py

import random
def aleatorio2():
    n   =  random.randrange(10,30)
   
    print(n)
    
arquivo: ex1.py

import random
def aleatorio():
    n  =  random.randint(5,10)
    print(n)    







    import random


def atividade1():
    x  =  random.randint(5,10)
    return x

def atividade2():
    x  =  random.randint(1,10)
    y  =  random.randint(1,10)
    z  =  random.randint(1,10)
    return x, y, z




# import metodo

# print(metodo.atividade1())
# print(metodo.atividade2())


# **6 - Tabuada de multiplicação**
# Pede ao usuário para inserir um número inteiro
numero = int(input("Digite um número inteiro para ver a sua tabuada: "))

print(f"\nTabuada do {numero}:")
print("-" * 15)

# Calcula e mostra a tabuada de 1 a 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2d} = {resultado}")

print("-" * 15)

# ***Utilize print() na saída***

# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.

# (while ou for )

# **7 -  Números ímpares reversos**
print("Contagem regressiva de números ímpares (99 a 1):")
print("-" * 45)

# O range começa em 99, vai até 0 (para incluir o 1) e diminui de 2 em 2
for i in range(99, 0, -2):
    print(i, end=" ")

print("\n" + "-" * 45)
# Exiba uma contagem regressiva de números ímpares de 99 a 1.

# (for)