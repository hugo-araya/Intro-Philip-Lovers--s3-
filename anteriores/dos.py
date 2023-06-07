pal1 = input('Pal 1: ')
pal2 = input('Pal 2: ')
largo = len(pal1)
largo = largo - 3
final = pal1[largo:]
riman1 = pal2.endswith(final)
largo = len(pal1)
largo = largo - 2
final = pal1[largo:]
riman2 = pal2.endswith(final)
if riman1 == True:
    print("Riman")
else:
    if riman2 == True:
        print("Riman poco")
    else:
        print("No riman")