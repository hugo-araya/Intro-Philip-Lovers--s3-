import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

cont = 0
todas = 0
cantidad = int(input('Cantidad de estudiantes: '))
while (cont < cantidad): 
    Nota = float(input('Nota' + str(cont + 1) + ': '))
    todas = todas + Nota
    cont = cont + 1
Promedio = todas/cantidad
print(Promedio)
