import random
import time
import os

# sistema di colorazione caratteri
os.system("cls")
setcolor_green = "\u001b[32m"
setcolor_white = "\u001b[37m"
setcolor_cyan = "\u001b[36m"
setcolor_red = "\u001b[31;1m"


def start_program():
    print(setcolor_white)
    time.sleep(2)
    print("")
    print("Benvenuto Utente, questa è la versione digitale di Carta, Forbice, Sasso.")
    print("Per giocare scrivere 'play' e inviare per mostrare ulteriori info digitare")
    print("'info' e inviare, dopo la rivelazione delle info  il gioco partirà automaticamente")
    start = input()

    if start == "play":
        print("")
        print_iniziali()
    elif start == "info":
        print("Versione: relase - 1.2")
        print("")
        time.sleep(1)
        print("developer: Vincenzo Scarso")
        time.sleep(2)
        print(setcolor_green)
        print("=====")
        print("START")
        print("=====")
        print(setcolor_white)
        time.sleep(1)
        print_iniziali()
    else:
        print("Scusa non ho capito")
        print("Starting del programma...")
        time.sleep(2)
        print(setcolor_green)
        print("=====")
        print("START")
        print("=====")
        print(setcolor_white)
        time.sleep(1)
        print_iniziali()


def print_iniziali():
    # serie di print
    print('Ciao')
    time.sleep(1)
    print('come ti chiami?')
    risposta = input()
    print("...")
    time.sleep(2)
    print('Bene ' + setcolor_cyan + risposta + setcolor_white + ' giochiamo!!!')
    time.sleep(2)
    programma()


def programma():
    print('Per giocare scegli tra carta=1 sasso=2 forbice=3')
    cfs = int(input())
    time.sleep(1)
    print("...")
    print('bene hai fatto la tua scelta')
    time.sleep(1)
    print('ora tocca a me :)')
    time.sleep(1)
    print('...')
    time.sleep(1)

    # randomizzatore di numeri
    a = range(1, 4)
    combinazione = random.sample(a, 1)

    # vincita
    vincita = setcolor_green + "HO VINTO!!!" + setcolor_white
    if combinazione == [1] and cfs == 2:
        print(vincita + " io ho scelto carta")
        final()

    if combinazione == [2] and cfs == 3:
        print(vincita + " io ho scelto sasso")
        final()

    if combinazione == [3] and cfs == 1:
        print(vincita + " io ho scelto forbice")
        final()

    # perdita
    perdita = setcolor_red + "ho perso :(" + setcolor_white
    if combinazione == [2] and cfs == 1:
        print(perdita + " io ho scelto sasso")
        final()

    if combinazione == [3] and cfs == 2:
        print(perdita + " io ho scelto forbice")
        final()

    if combinazione == [1] and cfs == 3:
        print(perdita + " io ho scelto carta")
        final()

    # input_errato
    if cfs > 3:
        print('Scusa non ho capito!')
        programma()

    if cfs < 1:
        print('Scusa non ho capito!')
        programma()


def final():
    print("")
    time.sleep(3)
    print("Bene il gioco è ora terminato si desidera continuare a giocare oppure ricominciare?")
    print("Nota: continuando verrà usato lo stesso nickname.")
    print("Se si preferisce uscire premere qualsiasi altra lettera e inviare.")
    print(setcolor_green + "[C]ontinuare" + setcolor_white
          + " o " + setcolor_red + "[R]icominciare" + setcolor_white)
    stay_leave = input()

    if stay_leave == "C":
        programma()

    if stay_leave == "R":
        print_iniziali()


# ___STARTER___
start_program()
