from herramientas import * 

def evaluaMail1(correo):
    indice = correo.find('@')
    mensa = 'CORRECTO'
    if indice == -1:
        mensa = 'INCORRECTO'
    return mensa

def evaluaMail2(correo):
    cont = correo.count('@')
    mensa = 'INCORRECTO'
    if cont == 1:
        mensa = 'CORRECTO'
    return mensa

clrScr()
correo = input("Mail: ")
estado = evaluaMail1(correo)
print(estado)
estado = evaluaMail2(correo)
print(estado)
