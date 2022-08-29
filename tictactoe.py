
import random


def Replay(Table, num):
    for i in Table:
        if num == i:
            Table[Table.index(num)] = "X"


def ReplayO(Table, o):
    for j in Table:
        if o == j:
            Table[Table.index(o)] = "O"


def X123(X, str):
    cpt = 0
    for i in X:
        if i == str:
            cpt += 1
    if cpt == 3 and str == 'X':
        print("you win !!")
        exit(0)
    elif cpt == 3 and str == 'O':
        print("you lose !!")
        exit(0)


def XYZ(X, Y, Z, str, x):
    for i in range(x):
        if (X[i] == Y[i] == Z[i] == str) and str == 'X':
            print("you win !!")
            exit(0)
        elif (X[i] == Y[i] == Z[i] == str) and str == 'O':
            print("you lose !!")
            exit(0)


def XYZ5(X, Y, Z, str):
    for i in range(1):
        if X[i] == Y[i + 1] == Z[i + 2] == str and str == 'X':
            print("you win !!")
            exit(0)
        elif X[i] == Y[i + 1] == Z[i + 2] == str and str == 'O':
            print("you Lose !!")
            exit(0)
        if X[i + 2] == Y[i + 1] == Z[i] == str and str == 'X':
            print("you win !!")
            exit(0)
        elif X[i + 2] == Y[i + 1] == Z[i] == str and str == 'O':
            print("you Lose !!")
            exit(0)


def act1(str):
    X123(X, str)
    X123(Y, str)
    X123(Z, str)
    XYZ(X, Y, Z, str, 1)
    XYZ(X, Y, Z, str, 2)
    XYZ(X, Y, Z, str, 3)
    XYZ5(X, Y, Z, str)



Table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
table = f'''{1} | {2} | {3} | \n{4} | {5} | {6} |\n{7} | {8} | {9} |\n'''
print(table)
# print(Table)
x = []
y = []
z = []
for i in range(len(Table)):
    z, y, x = Table[i], Table[i - 1], Table[i - 2]
# print(x)
# print(y)
# print(z)

l = []
lx = []
while True:
    try:
        num = int(input("enter x :"))
        while num not in range(1, 10):
            num = int(input("enter number between 1 and 9 :"))
        break
    except:
        print("not valid")
l.append(num)

while len(l) <= 10:
    if len(l) == 8:
        print("The game ended with draw")
        exit(0)
    while len(l) <= 9:

        Replay(x, num)
        Replay(y, num)
        Replay(z, num)
        X, Y, Z = ''.join(map(str, x)), ''.join(map(str, y)), ''.join(map(str, z))
        act1('X')

        o = int(random.randint(1, 9))
        while o in l:
            o = int(random.randint(1, 9))
        l.append(o)
        lx.append(num)
        # print(lx)
        ReplayO(x, o)
        ReplayO(y, o)
        ReplayO(z, o)
        X, Y, Z = ''.join(map(str, x)), ''.join(map(str, y)), ''.join(map(str, z))
        print(('|'.join([f' {i} ' for i in X])))
        print(('|'.join([f' {i} ' for i in Y])))
        print(('|'.join([f' {i} ' for i in Z])))
        act1('O')
        while True:
            try:
                num = int(input("enter x :"))
                while num not in range(1, 10):
                    num = int(input("enter number between 1 and 9 :"))
                break
            except:
                print("not valid")
        while num in l:
            while True:
                try:
                    num = int(input("enter x :"))
                    while num not in range(1, 10):
                        num = int(input("enter number between 1 and 9 :"))
                    break
                except:
                    print("not valid")

        l.append(num)

        Replay(x, num)
        Replay(y, num)
        Replay(z, num)
