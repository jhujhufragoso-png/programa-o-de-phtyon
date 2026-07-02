
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




import metodo

print(metodo.atividade1())
print(metodo.atividade2())