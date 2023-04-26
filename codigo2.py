# Escribir un algoritmo que escriba el nombre de un articulo, clave, precio original 
# y su precio con descuento. 
# El descuento lo hace en base a la clave, si la clave es 01 el descuento es 
# del 10% y si la clave es 02 el descuento es del 20% 
# (solo existen dos claves).

# Datos de entrada: articulo(String), codigo(String), precio_or(Entero)
# Dato Salida: precio_de(Float)
import os

if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

articulo = input('-->> Nombre del articulo: ')
codigo = input('---->> Codigo: ')
precio_or = int(input('---->> Precio: '))
if (codigo == '01'):
    precio_de = precio_or * 0.9
else:
    if (codigo == '02'):
        precio_de = precio_or * 0.8
    else:
        codigo = 'Codigo no valido'
        precio_de = 0
print('-----------------------------')
print("Articulo: ", articulo)
print('Codigo: ', codigo)
print('Precio: ', precio_de)
