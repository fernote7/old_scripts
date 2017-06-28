__author__ = 'fernando.ormonde'



#primos1 eh uma funcao mais rapida que primos

def primos1(n):
    lista = []

    for j in range(n):
        j+=1
        divisores = []

        for i in range(j):
            i += 1
            if j % i == 0:
                divisores.append(i)


        if len(divisores) == 2:
            lista.append(j)


    print len(lista)
    return lista


print primos1(1000)

################################

def primos(n):
    lista = []

    for j in range(n):
        j+=1
        divisores = [1, j]

        for i in range(j):
            i += 1
            if i != 1 and i != j:
                if j % i == 0:
                    divisores.append(i)


        if len(divisores) == 2:
            lista.append(j)


    lista.pop(0)
    print len(lista)
    return lista

print primos(1000)

###########################################

def primos3(n):
    lista = []
    i = 0

    while i < n:
        i+=1
        divisores = []

        for j in range (i):
            j += 1
            if i % j == 0:
                divisores.append(j)


        if len(divisores) == 2:
            lista.append(i)



    print len(lista)
    return lista


print primos3(1000)

######################################

def primos2(n):
    lista = []

    for j in range(n):
        j+=1
        divisores = []

        for i in range(j):
            i += 1

            if len(divisores) <= 2:
                if j % i == 0:
                    divisores.append(i)
            else:
                break

        if len(divisores) == 2:
            lista.append(j)


    print len(lista)
    return lista


print primos2(1000)