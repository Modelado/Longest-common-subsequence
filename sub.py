def lcs(a, b):
    #Llenamos de 0 una matriz de b+1 x a+1 y la inizializamos en 0.
    longitud = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    #Recorremos la matriz
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                longitud[i+1][j+1] = longitud[i][j] + 1
            else:
                longitud[i+1][j+1] = max(longitud[i+1][j], longitud[i][j+1])
    #Leemos la subcadena de la matriz
    resultado = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if longitud[x][y] == longitud[x-1][y]:
            x -= 1
        elif longitud[x][y] == longitud[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            resultado = a[x-1] + resultado
            x -= 1
            y -= 1
    return resultado
a="curator Jacque Sauniere in D. Brown's novel The Da Vinci Code (Brown 2003, pp. 43, 60-61, and 189-192). In the Season 1 episode Sabotage (2005) of"
b="the television crime drama NUMB3RS, math genius Charlie Eppes mentions that the Fibonacci numbers are found in the structure of crystals and the spiral"
print (lcs(a,b))
