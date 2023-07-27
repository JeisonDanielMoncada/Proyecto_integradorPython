nom = input("Ingrese su nombre de jugador: ") 
print("Bienvenido jugador ", nom)

import readchar
import os

key = readchar.readkey()

from readchar import readkey, key
laberinto = """..###################
....#...#...........#
#.###.#########.#.###
#...#.........#.#.#.#
#.#######.#.#.#.###.#
#.......#.#.#...#...#
#######.#.###.#.###.#
#...#.....#...#...#.#
#.###.###.#####.###.#
#.#...#...#.....#...#
#.#.#######.#####.###
#.........#.....#...#
###.#####.#.#.###.#.#
#.#.#.....#.#.....#.#
#.#####.#########.#.#
#.........#.......#.#
###.#.#####.###.#.#.#
#...#.#.....#...#.#.#
#.#######.#####.###.#
#...#.......#.....#.#
###################.#"""
import os

def conver_matriz (laberinto):
    matriz = []
    for linea in laberinto.split("\n"):
        matriz.append(list(linea))
    return matriz
matriz = conver_matriz(laberinto)

def mostrar_matriz(matriz):
    os.system('cls' if os.name == 'nt' else 'clear')
    for laberinto in matriz:
        print(' '.join([str(elem) for elem in laberinto]))


filas = matriz
coordenadas = []
for i, fila in enumerate(filas):
    for j, caracter in enumerate(fila):
        if caracter == "#":
            coordenadas.append((i, j))
coordenadas = tuple(coordenadas)
py , px = (0 , 0)
while True:
  matriz[py][px]= "P"
  posicion_inicial = [0 , 0]
  posicion_final= [20, 19]
  print(mostrar_matriz(matriz))
  k = readkey()
  if k == key.RIGHT and (py , px) not in coordenadas:
    matriz[py][px]= "."
    py , px = (py, (px+1))
  elif k == key.DOWN and (py , px) not in coordenadas:
    matriz[py][px]= "."
    py , px = ((py+1), (px))  
  elif k == key.UP and (py , px) not in coordenadas:
    matriz[py][px]= "."
    py , px = ((py-1), (px))   
  elif k == key.LEFT and (py , px) not in coordenadas:
    matriz[py][px]= "."
    py , px = ((py), (px-1))   
  elif posicion_inicial == posicion_final:
    
    break