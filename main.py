nom = input("Ingrese su nombre de jugador: ") 
print("Bienvenido jugador ", nom)

import readchar

key = readchar.readkey()

from readchar import readkey, key

while True:
  k = readkey()
  print("Para que se detenga presione la tecla fecla UP")
  print(k)
  if k == key.UP:
    # do stuff
    break

def conteo (n: int):
    while n<50:
        import os
        k = readkey()
        n=n+1
        os.system('cls' if os.name=='nt' else 'clear')
        print(n)
        if k == 50:
            os.system('cls' if os.name=='nt' else 'clear')
            break
conteo (0)
  