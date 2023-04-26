# Determinar la cantidad de dinero que recibirá un trabajador por 
# concepto de las horas extras trabajadas en una empresa, sabiendo 
# que cuando las horas de trabajo exceden de 40, el resto se consideran 
# horas extras y que estas se pagan al doble de una hora normal cuando 
# no exceden de 8; si las horas extras exceden de 8 se pagan las 
# primeras 8 al doble de lo que se pagan las horas normales y el 
# resto al triple.

# Datos entrada: horas_ex(Entero), horas_total(Entero), valor_hora(Entero)

# Datos salida: sueldo_final(Entero)
import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

horas_totales = int(input('Horas trabajadas: '))
valor_hora = int(input('Valor de la hora: '))

if (horas_totales <= 40):
    sueldo_final = horas_totales*valor_hora
else:
    horas_ex = horas_totales - 40
    if (horas_ex <= 8):
        sueldo_final = 40*valor_hora + horas_ex*2*valor_hora
    else:
        horas_ex = horas_ex - 8
        sueldo_final = 40*valor_hora + 8*2*valor_hora + horas_ex*3*valor_hora
print("Sueldo a recibir: ", sueldo_final)

