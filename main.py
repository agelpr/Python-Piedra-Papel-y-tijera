#Juego de piedra, papel o tijera
#importar libreria random

import random

print("""[ ๐ค Bienvenido al juego Piedra, Papel o tijera ๐]   """)
print('>>> Ingresa una opciรณn <<<')
iuser = 0
icomp = 0
rounds = 1
while True:
  #creo una tupla con las opciones de la computadora
  options = ('piedra', 'papel', 'tijera')
  print("*" * 10)
  print(" Round ", rounds)
  print("*" * 10)
   #pido la opcion al usuario
  user_option = input("piedra, papel o tijera: ")
  #tranformo los datos a minusculas
  user_option = user_option.lower()
  #compruebo las opciones de la tupla al usuario
  if not user_option in options:
    print('La opcion que elegiste no esta dentro de las opciones')
  #le digo a la funcion choice de la libreria random que elija aleatoriamente una de las opciones declaradas en la tupla
  computer_option = random.choice(options)
  #outputs al usuario
  #print("La opcion de elegiste es: ", user_option)
  print("La computadore elige: ", computer_option)

  if user_option == computer_option:
    print("Empate!")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("โ gana a โ๏ธ")
      print(" ๐user ganรณ!")
      iuser += 1
    else:
      print("๐๏ธ gana a โ")
      print("๐คcomputer gano!")
      icomp += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("โ๏ธ gana a ๐๏ธ")
      print("๐ user gano!")
      iuser += 1
    else:
      print("โ gana a โ๏ธ")
      print("๐ค computer gano!")
      icomp += 1
  elif user_option == "papel":
    if computer_option == "piedra":
      print("๐๏ธ gana a โ")
      print("๐ user gano!")
      iuser += 1
    else:
      print("โ๏ธ gana a ๐๏ธ")
      print("๐ค computer gano!")
      icomp += 1
  if iuser == 2:
    print("Felicidades ganaste ๐")
    break
  if icomp == 2:
    print("Has perdido, te ganรณ la computadora ๐ค")
    break

  rounds += 1


