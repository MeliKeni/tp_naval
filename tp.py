import random
#delcaracion de funciones
def crearTablero(n:int) -> list[list[str]]:
    tablero: list[list[str]] = []
    for i in range(n):
        tablero.append([])
    for i in range(n):
        for _ in range(n):
            tablero[i].append(" ")
    return tablero
def imprimirTablero(tablero:list[list[str]]) -> None:
    for fila in tablero:
        print(fila)

def asignarBarcos(tablero:list[list[str]], cantidadBarcos:int) -> list[list[int]]:
    posicionesBarcos: list[list[list[int]]] = []
    
    for i in range(cantidadBarcos):
        barco_i: list[list[int]] = []

    while len(posicionesBarcos) < cantidadBarcos:
        tamanoBarco:int = int(input("Tamaño del barco: "))
        if tamanoBarco > 3:
            print("El barco es de hasta 3 casillas, automaticamente se hara su barco de 3 casillas")
            tamanoBarco=3
        posicionx = random.randint(0, n-1)
        posiciony = random.randint(0, n-1)
        posicionyfinal= posiciony + tamanoBarco - 1
        if posicionyfinal > n-1:
            print("Hubo un error, repetir ese barco")
            continue
        if [posicionx, posiciony] in posicionesBarcos:
            continue
        for i in range(tamanoBarco):
           barco_i.append([posicionx, posiciony + i])
           tablero[posicionx][posiciony + i] = "barco"
        print("Barco colocado")
        posicionesBarcos.append(barco_i) 
    return posicionesBarcos

def sistema_disparos(tablero: list[list[str]], posiciones_barcos: list[list[list[int]]]) -> None: #aca me gustria poner 2 intes, para que devuleva aciertos y fallos pero no se como hacerlo
    cantidadDisparos:int =int(input("Cuantos intentos quiere?"))
    disparosAcertados:int =0
    disparosFallados:int =0
    for i in range(cantidadDisparos):
        entrada:str = input("Decir posicion barco")
        intentoDisparo:list[int] = [int(entrada.split(",")[0]), int(entrada.split(",")[1])]
        
        for i in range(len(posiciones_barcos)):
            if intentoDisparo in posiciones_barcos[i]:
                disparosAcertados += 1
                tablero[intentoDisparo[0]][intentoDisparo[1]] = "golpeado"
                print("Disparo acertado")
            else :
                disparosFallados += 1
                print("Disparo fallado")
    for barco_i in posiciones_barcos:
        hundido:bool = True
    for casilla in barco_i:
        x, y = casilla
        if tablero[x][y] != "golpeado":
            hundido = False
    if hundido:
        print("Barco hundido")
        for casilla in barco_i:
            x, y = casilla
            tablero[x][y] = "hundido"
    return disparosAcertados, disparosFallados

#creacion y configuarcion del juego
n= int(input("Tamaño del tablero: "))
tablero: list[list[str]] = crearTablero(n)

cantidadBarcos = int(input("Cuantos barcos?"))

posicionesBarcos = asignarBarcos(tablero, cantidadBarcos)


disparosAcertados, disparosFallados = sistema_disparos(tablero, posicionesBarcos)

#finalizar el juego
imprimirTablero(tablero)
print("la cantidad de disparos acertados fueron: ", + disparosAcertados)
print("la cantidad de disparos fallados fueron: ", + disparosFallados)




