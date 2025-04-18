import random

n = 10
tablero: list[list[str]] = []

for i in range(n):
    tablero.append([])

for i in range(n):
    for _ in range(n):
        tablero[i].append(" ")
    print(tablero[i])

cantidadBarcos = 2
posicionesBarcos: list[list[int]] = []

for i in range(cantidadBarcos):
    posicionx = random.randint(0, n-1)
    posiciony = random.randint(0, n-1)
    if [posicionx, posiciony] in posicionesBarcos:
        continue #chequear que te estaria faltando un barco
    posicionesBarcos.append([posicionx, posiciony])

print(posicionesBarcos)

cantidadDisparos:int = 3
disparosAcertados:int =0 
disparosFallados:int =0

for i in range(cantidadDisparos):
    entrada:str = input("Decir posicion barco")
    intentoDisparo:list[int] = [entrada.split(",")[0], entrada.split(",")[1]]

    if intentoDisparo in posicionesBarcos:
        disparosAcertados += 1
        posicionesBarcos.remove(intentoDisparo)
        tablero[intentoDisparo[0]][intentoDisparo[1]] = "golpeado"
    else :
        disparosFallados += 1

for i in range(n):
    for j in range(n):
        print(tablero[i])

print(disparosAcertados)
print(disparosFallados)




