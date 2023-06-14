#import herramientas as hs
from herramientas import *

def f(x):
    y = 5*x + 1
    return y 

def evaluaTodos(x):
    largo = len(x)
    i = 0
    while i < largo:
        valor = f(x[i])
        print(valor)
        i = i + 1

clrScr()
x = [1,2,3,4,5,6,7,8,9,10]
evaluaTodos(x)


 
