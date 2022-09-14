import random, time, sys#, pruebas.py

# Éste programa sólo acepta equipos de 1 y 2 integrantes

#  Ésta primera función recibe número de equipos y jugadores y devuelve la lista de los equipos sorteados al azar

#"""

fError = "\033[1m" + "\033[31m"
fExito = "\033[1m" + "\033[32m"

def  sorteoEquipos(nEquipos: int, nJugadores: int) -> list:
  
  listaEquipos = []
  nombreJugadores = []

  while int(nJugadores) % int(nEquipos) != 0:
    print(fError + "Error! Los números de equipos y jugadores no son compatibles\n" + '\033[0m')
    nEquipos = int(input("Ingrese un nuevo número de equipos: "))
    nJugadores = int(input("Ingrese un nuevo número de integrantes: "))

  for i in range(0, nJugadores):
    nombreJugadores.append(input("Ingrese el nombre del jugador número %d: " %(i + 1)))

  print('\033[33m' + "Procesando equipos", end="") 
  
  for i in range(0, int(nJugadores)):      #  Éste bucle solo imprime bonito los puntos xD
    print("." + ('\033[%dm' %(random.randint(31, 35))), end="")
    sys.stdout.flush()
    time.sleep(0.5)
    
  random.shuffle(nombreJugadores)
     
  print(fExito + "\nEquipos repartidos!\n" + "\033[0m")

  if nJugadores == nEquipos:
    return nombreJugadores

  else:
    for i in range(0, int(nJugadores), 2):
     listaEquipos.append(nombreJugadores[i] + " y " + nombreJugadores[i + 1])

  return listaEquipos

#"""

#  Ésta segunda función recibe la lista de equipos y los enfrenta y elimina el perdedor hasta que sólo haya 1 equipo en la lista
#"""
def  sorteoTorneo(lEquipos: list):
  
  if len(lEquipos) % 4 != 0:
    print(fError + "Error!, la cantidad de equipos no permite un torneo de eliminación" + "\033[0m")
    return None

  i = 0
  
  try:
    while lEquipos[1]: 
      perdedor = int(input("\033[33m" + "\033[1m" + "\nPartido!\n" + "\033[0m" +"\n\n%d. %s VS %d. %s\ny perdió: " % (i, lEquipos[i], i + 1, lEquipos[i + 1])))
      
      if input("El equipo de %s será eliminado! Ingresa n para cancelar\n" % lEquipos[perdedor]) == "n":
        continue
        
      lEquipos.remove(lEquipos[perdedor])
      i += 1
      if i >= len(lEquipos):
        i = 0
        
  except:
    print(fExito + "El equipo ganador es %s!, Felicitaciones!" % lEquipos[0])
#"""
equipos = sorteoEquipos(4, 4)
sorteoTorneo(equipos)