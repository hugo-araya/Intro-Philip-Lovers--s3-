import matplotlib.pyplot as plt
ar = open('datos.txt')
comuna = []
habi = []
linea = ar.readline().rstrip('\n')
while linea != '':
    lista = linea.split(',')
    if lista[1] == '7':
        comuna.append(lista[2])
        habi.append(float(lista[4]))
    linea = ar.readline().rstrip('\n')
ar.close()
print(sum(habi))
plt.plot(comuna, habi)
plt.show()




