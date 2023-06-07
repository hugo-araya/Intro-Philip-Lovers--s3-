nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
examen = float(input('Examen: '))
trabajo = float(input('Trabajo: '))

notas = (nota1 + nota2 + nota3)/3
final = notas*0.55 + examen*0.3 + trabajo*0.15

if (final >= 4):
    print('Felicitaciones aprobo el curso')
    print('Con la nota final : ', final)
else:
    print('Lo siento, nos vemos el proximo año')
    print('La nota que lo condeno fue:', final)
print('--------------------')
