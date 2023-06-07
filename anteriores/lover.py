maestra = '123456789'
clave1 = ''
clave2 = ''
largo = len(maestra)
i = 0
while(i < largo):
    caracter = maestra[i]
    if (i % 2) == 0:
        clave1 = clave1 + caracter
    else:
        clave2 = clave2 + caracter
    i = i + 1
print(clave1)
print(clave2)
