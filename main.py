
import os
#import random
from threading import Event
from minimax_utility_class import generate_cells
from minimax_utility_class import dispUboard
from MiniMax_Algorithm import minimax_algorithm

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def VerNumero(Dato):
    # Verificacion de si el objeto puede convertirse a numero
    try:
        int(Dato)
        return True
    except ValueError:
        return False

def Encabezado():
    # Encabezado de la aplicacion
    Clear()
    print("Juego de Tres en Raya")
    print("Los numeros del Tablero estan ordenados de izquierda a derecha.")
    print()

def Errores(Dato):
    # Impresion de errores
    print(Dato)
    print("- "*20)
    Event().wait(1) 

def Tablero_juego(Tablero):
    # Impresion del tablero en juego
    print("- "*20)
    print("Tablero de Juego")
    print()
    print("| 1 | 2 | 3 |  |",Tablero[0],"|",Tablero[1],"|",Tablero[2],"|")
    print("|-----------|  |-----------|")
    print("| 4 | 5 | 6 |  |",Tablero[3],"|",Tablero[4],"|",Tablero[5],"|")
    print("|-----------|  |-----------|")
    print("| 7 | 8 | 9 |  |",Tablero[6],"|",Tablero[7],"|",Tablero[8],"|")
    print("- "*20)
    print()

def comprueba_victoria(Tablero):
    # Revisar las lineas en horizontales
    if (Tablero[0] == Tablero[1] == Tablero[2] != ' ') or (Tablero[3] == Tablero[4] == Tablero[5] != ' ') or (Tablero[6] == Tablero[7] == Tablero[8] != ' '):
        return False
    # Revisar las lineas en verticales
    elif (Tablero[0] == Tablero[3] == Tablero[6] != ' ') or (Tablero[1] == Tablero[4] == Tablero[7] != ' ') or (Tablero[2] == Tablero[5] == Tablero[6] != ' '):
        return False
    # Revisar las lineas en diagonales
    elif (Tablero[0] == Tablero[4] == Tablero[8] != ' ') or (Tablero[6] == Tablero[4] == Tablero[2] != ' '):
        return False
    else:
        return True

def ConvertirParaIA(Tablero,Movimiento,Jugador):
    # Funcion para adaptar el juego a la IA
    if Movimiento == 1:
        Tablero[0][0] = Jugador
    elif Movimiento == 2:
        Tablero[0][1] = Jugador
    elif Movimiento == 3:
        Tablero[0][2] = Jugador
    elif Movimiento == 4:
        Tablero[1][0] = Jugador
    elif Movimiento == 5:
        Tablero[1][1] = Jugador
    elif Movimiento == 6:
        Tablero[1][2] = Jugador
    elif Movimiento == 7:
        Tablero[2][0] = Jugador
    elif Movimiento == 8:
        Tablero[2][1] = Jugador
    elif Movimiento == 9:
        Tablero[2][2] = Jugador

def Bot(TableroIA):
    #Casilla = random.choice(Movimientos)
    uboard = generate_cells(TableroIA)
    computer_decision = minimax_algorithm(uboard)
    Numero = int(computer_decision)+1
    return Numero

def JugadorFunc():
    Numero = input("Selecciona una casilla del (1-9) ")
    return Numero

def valido(Tablero,Casilla):
    if Casilla >= 0 and Casilla <= 8:
        if Tablero[Casilla] != " ":
            Errores('Esa posicion ya esta en uso.')
            return False
        else:
            return True
    else:
        Errores('Posicion invalida')
        return False

if __name__ == "__main__":

    # Variables
    # Guardardo del Tablero
    Tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    TableroIA = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
    # Creacion Primer Jugador
    Jugador = "X"
    # Creacion de las jugadas
    Jugadas = 1
    # Variagle de Gamemode
    GamemodeSeleccionado = False
    # Creacion de IA
    Movimientos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while True:

        if not GamemodeSeleccionado:
            Clear()
            print("Selecciona el modo de juego")
            print("PvP -> Jugador vs Jugador", Jugador)
            print("PvE -> Jugador vs IA", Jugador)

            Gamemode = input("Selecciona si quieres PvP o PvE - ").lower()
            if Gamemode == 'pvp' or Gamemode == 'pve':
                GamemodeSeleccionado = True
            else:
                Errores('Solo Tenemos el modo de juego pvp y pve')

        if Gamemode == 'pvp':
            Encabezado()
            Tablero_juego(Tablero)

            print("Turno del jugador", Jugador)
            Casilla = JugadorFunc()
            if VerNumero(Casilla):
                # La tabla es de 0 a 8 entonces se necesita restar 1 a la respuesta para un funcionamiento mas simple.
                Casilla = int(Casilla) - 1
                if valido(Tablero,Casilla):
                    Tablero[Casilla] = Jugador
                    Jugadas = Jugadas + 1
                else:
                    continue

                if comprueba_victoria(Tablero):
                    if Jugador == "X":
                        Jugador = "O"
                    else:
                        Jugador = "X"
                else:
                    Clear()
                    Tablero_juego(Tablero)
                    print("Se termino el juego el ganador es", Jugador)
                    Event().wait(5) 
                    break
            
                if Jugadas >= 9:
                    Clear()
                    Tablero_juego(Tablero)
                    Errores("El juego termina en empate")
                    break
            else:
                Errores('Solo se Admiten numeros')

        elif Gamemode == 'pve':
            Encabezado()
            Tablero_juego(Tablero)

            print("Turno del jugador", Jugador)
            if Jugador == "O":
                Casilla = Bot(TableroIA)
            else:
                Casilla = JugadorFunc()

            if VerNumero(Casilla):
                # La tabla es de 0 a 8 entonces se necesita restar 1 a la respuesta para un funcionamiento mas simple.
                Casilla = int(Casilla) - 1
                if valido(Tablero,Casilla):
                    # Esto sirve para que la IA no repita casillas que ya estan en uso
                    Movimientos.remove(Casilla+1)
                    ConvertirParaIA(TableroIA,Casilla+1,Jugador)
                    Tablero[Casilla] = Jugador
                    Jugadas = Jugadas + 1
                else:
                    continue

                if comprueba_victoria(Tablero):
                    if Jugador == "X":
                        Jugador = "O"
                    else:
                        Jugador = "X"
                else:
                    Clear()
                    Tablero_juego(Tablero)
                    print("Se termino el juego el ganador es", Jugador)
                    Event().wait(5) 
                    break
            
                if Jugadas >= 9:
                    Clear()
                    Tablero_juego(Tablero)
                    Errores("El juego termina en empate")
                    break
            else:
                Errores('Solo se Admiten numeros')

