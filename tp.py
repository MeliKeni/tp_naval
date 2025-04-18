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
    posicionesBarcos: list[list[int]] = []
    
    while 0 < cantidadBarcos:
        tamanoBarco:int = int(input("Tamaño del barco: "))
        if tamanoBarco > 3:
            print("El barco es de hasta 3 casillas")
            continue

        posicionx = random.randint(0, n-1)
        posicionxfinal= posicionx + tamanoBarco - 1
        if posicionxfinal > n-1:
            print("Hubo un error, repetir ese barco")
            continue
        posiciony = random.randint(0, n-1)
        if [posicionx, posiciony] in posicionesBarcos:
            continue
        for i in range(tamanoBarco):
           posicionesBarcos.append([posicionx + i, posiciony])
           tablero[posicionx + i][posiciony] = "barco"
        cantidadBarcos -= 1
        print("Barco colocado")
    return posicionesBarcos

def sistema_disparos(tablero: list[list[str]], posiciones_barcos: list[list[int]]) -> None: #aca me gustria poner 2 intes, para que devuleva aciertos y fallos pero no se como hacerlo
    cantidadDisparos:int =int(input("Cuantos intentos quiere?"))
    disparosAcertados:int =0
    disparosFallados:int =0
    for i in range(cantidadDisparos):
        entrada:str = input("Decir posicion barco")
        intentoDisparo:list[int] = [int(entrada.split(",")[0]), int(entrada.split(",")[1])]

        if intentoDisparo in posicionesBarcos:
            disparosAcertados += 1
            posicionesBarcos.remove(intentoDisparo)
            tablero[intentoDisparo[0]][intentoDisparo[1]] = "golpeado"
            print("Disparo acertado")
        else :
            disparosFallados += 1
            print("Disparo fallado")
    return disparosAcertados, disparosFallados

#creacion y configuarcion del juego
n= int(input("Tamaño del tablero: "))
tablero: list[list[str]] = crearTablero(n)

cantidadBarcos = int(input("Cuantos barcos?"))

posicionesBarcos = asignarBarcos(tablero, cantidadBarcos)

print(posicionesBarcos) #me indica donde estan los barcos
#juego
disparosAcertados, disparosFallados = sistema_disparos(tablero, posicionesBarcos)

#finalizar el juego
imprimirTablero(tablero)
print("la cantidad de disparos acertados fueron: ", + disparosAcertados)
print("la cantidad de disparos fallados fueron: ", + disparosFallados)




