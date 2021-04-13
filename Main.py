Numb = int(input("Введите длину спирали - "))
mass = [[0] * Numb for i in range(Numb)]
Pos = (Numb*Numb)
Index = 0

for i in range(Numb // 2):
    for j in range(Numb - Index):
        mass[i][j + i] = Pos
        Pos -= 1
    for j in range(i + 1, Numb - i):
        mass[j][-i - 1] = Pos
        Pos -= 1
    for j in range(i + 1, Numb - i):
        mass[-i - 1][-j - 1] = Pos
        Pos -= 1
    for j in range(i + 1, Numb - (i + 1)):
        mass[-j - 1][i] = Pos
        Pos -= 1
    Index += 2

if(Numb % 2 != 0):
    mass[Numb // 2][Numb // 2] = 1

for i in mass:
    print(*i)