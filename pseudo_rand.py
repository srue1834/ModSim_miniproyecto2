import random

def rand_range(rep, x, mat, per2):
    for y in range(rep):
        y = random.randint(0, x)
        per = round(y/x, 2)

        if per >= 0.0 and per < 0.1:
            mat[0] += 1
        elif per > 0.1 and per < 0.2:
            mat[1] += 1
        elif per > 0.2 and per < 0.3:
            mat[2] += 1
        elif per > 0.3 and per < 0.4:
            mat[3] += 1
        elif per > 0.4 and per < 0.5:
            mat[4] += 1
        elif per > 0.5 and per < 0.6:
            mat[5] += 1
        elif per > 0.6 and per < 0.7:
            mat[6] += 1
        elif per > 0.7 and per < 0.8:
            mat[7] += 1
        elif per > 0.8 and per < 0.9:
            mat[8] += 1
        elif per > 0.9 and per < 1.0:
            mat[9] += 1

    for i in range(10):
        per2[i] = round(mat[i]/rep, 2)
        histogram([per2[i]], str(mat[i]), str(per2[i]*100))

def gen(n, m):
    rep = int(input("Ingrese el numero de repeticiones: "))
    mat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    per2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for x in range(rep):
        x = (n**5)*rep % ((2**m)-1)

    rand_range(rep, x, mat, per2)

def gen3():
    rep = int(input("Ingrese el numero de repeticiones: "))
    mat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    per2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # for x in range(rep):
    #     x = random.randint(0, rep)
    #     per = round(x/rep, 2)
    
    rand_range(rep, rep, mat, per2)

def histogram(items, num, perc):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 0.005
        print(output + "  (" + num + ", "+ perc + "%)")

active = True

while active:
    print(
    """ 
    EJERCICIO #3

        1. Generador 1
        2. Generador 2
        3. Generador 3
        4. Salir

    """)
    opt = int(input("Ingrese una opcion: "))
    if opt == 1:
        gen(5, 35)
    elif opt == 2:
        gen(7, 31)
    elif opt == 3:
        gen3()
    elif opt == 4:
        print("\nAdios!!")
        raise SystemExit
    else:
        print("\nIngrese una opcion valida")


