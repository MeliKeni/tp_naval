import random #Es una libreria que voy a utilizar en la generacion de barcos para que sea random, esta libreria nos ayuda a elegir numeros aleatorios

#declaro las variables iniciales
n:int =0 #tamano tablero4
disparosAcertadosA:int =0
disparosFalladosA:int =0
disparosAcertadosB:int =0
disparosFalladosB:int =0
cantidadBarcos:int =0
#delcaracion de funciones
def crearTablero(n:int) -> list[list[str]]: #en esta funcion vamos a crear un tablero, asi si quiero jugar de a 2 jugadores puedo usar la funcion 2 veces y listo, basicamente apartir de un entero n te hace una lista de listas, creando asi nuestro tablero de nxn
    tablero: list[list[str]] = []
    for i in range(n):
        tablero.append([])
    for i in range(n):
        for _ in range(n):
            tablero[i].append(" ")
    return tablero
def imprimirTablero(tablero:list[list[str]]) -> None: #esta funcion la vamos a usar para imprimir tableros, basicamente apartir de un tablero (lista de listas) te lo imprime en la consola, prolijo separado por filas
    for fila in tablero:
        print(fila)

def asignarBarcos(tablero:list[list[str]], cantidadBarcos:int) -> list[list[int]]: #Esta funcion sirve para asignar los barcos en el tablero. Apartir de un tablero, y un entero que represetna la cantidad de barcos que quiero, va preguntando el tamano de los barcos y los va poniendo en posiciones random en el tablero devolviendonos otra lista de listas con las posicones de los tableros guardadas por barco
    posicionesBarcos: list[list[list[int]]] = []
    
    while len(posicionesBarcos) < cantidadBarcos:
        barco_i: list[list[int]] = []
        tamanoBarco:int = int(input("Tamaño del barco: ")) #el int antes del input hace que en vez de que te tome lo que escribio el usuario como string lo pase a entero. 
        if tamanoBarco > 3:
            print("El barco es de hasta 3 casillas, automaticamente se hara su barco de 3 casillas")
            tamanoBarco=3
        posicionx = random.randint(0, n-1) #estaes la generacion random de las posiciones, se usa el random.randint que te genera un random entero entre los parametros que le ponemos despues
        posiciony = random.randint(0, n-1)
        posicionyfinal= posiciony + tamanoBarco - 1
        if posicionyfinal > n-1:
            print("Hubo un error, repetir ese barco")
            continue
        for i in range(tamanoBarco-1):
            if tablero[posicionx][posiciony + i] in posicionesBarcos:
                print("Hubo un error, repetir ese barco")
                continue
        for i in range(tamanoBarco):
           barco_i.append([posicionx, posiciony + i])
           tablero[posicionx][posiciony + i] = "barco"
        print("Barco colocado")
        posicionesBarcos.append(barco_i) 
    return posicionesBarcos

def turno(tablero: list[list[str]], posiciones_barcos: list[list[list[int]]]) -> None: #Esta funcion sirve para hacer un turno, es decir, un disparo al tablero, si estuvo acertado o fallado, si hundio un barco, etc. Para esta se ingresa un tablero, y la posciones de los barcos(una lista de listas) apartir de esto le pide al usuario que ingrese una casilla (una poscion del tablero) y chequea si hay barco ahi o no, en caso de que haya chequea si con ese disparo se hunde el barco. 
    disparosAcertados:int =0
    disparosFallados:int =0
    entrada:str = input("Decir posicion barco")
    intentoDisparo:list[int] = [int(entrada.split(",")[0]), int(entrada.split(",")[1])]
    acertado = False  
    
    for i in range(len(posiciones_barcos)):
        if intentoDisparo in posiciones_barcos[i]:
            disparosAcertados += 1
            tablero[intentoDisparo[0]][intentoDisparo[1]] = "golpeado"
            print("Disparo acertado")
            acertado = True  
            break  

    if not acertado: 
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
#creamos los tableros
n= int(input("Tamaño del tablero: "))
tableroA: list[list[str]] = crearTablero(n)
tableroB: list[list[str]] = crearTablero(n)
#creamos los barcos
cantidadBarcos = int(input("Cuantos barcos?"))

print("Cree los barcos para el tablero del jugador 1")
posicionesBarcosA = asignarBarcos(tableroA, cantidadBarcos)
print("Cree los barcos para el tablero del jugador 2")
posicionesBarcosB = asignarBarcos(tableroB, cantidadBarcos)

#aca empieza la partida de forma mas directa, se pregunta la cantidad de disparos que va a tener cada equipo y empiezan aa alternarse disparando
cantidadDisparos:int =int(input("Cuantos intentos quiere?"))


for i in range(cantidadDisparos):
    print("Turno jugador 1")
    aciertos, fallados = turno(tableroA, posicionesBarcosB)
    disparosAcertadosA += aciertos
    disparosFalladosA += fallados
    print("Turno jugador 2")
    aciertos, fallados = turno(tableroB, posicionesBarcosA)
    disparosAcertadosB += aciertos
    disparosFalladosB += fallados


#termina el juego, imprimimos lo stableros y cuantos disparos fallo/acerto cada uno
print("Tablero jugador 1")
imprimirTablero(tableroA)
print("la cantidad de disparos acertados por el jugador 1 fueron: ",  disparosAcertadosA)
print("la cantidad de disparos fallados por el jugador 1  fueron: ",  disparosFalladosA)
print("Tablero jugador 2")
imprimirTablero(tableroB)
print("la cantidad de disparos acertados por el jugador 2 fueron: ",  disparosAcertadosB)
print("la cantidad de disparos fallados por el jugador 2  fueron: ",  disparosFalladosB)

#Todo lo visto por fuera de clase fue buscado en la cheatsheet, tanteado o buscado en google