import time
import random




def start_program():
    print("")
    print("Benvenuto utente questa è la versione digitale di Carta, Forbice, Sasso.")
    print("Per giocare scrivere 'play' e inviare per mostrare ulteriori info"
        " digitare 'info' e inviare, dopo la rivelazione delle info partirà "
        " automaticamente il gioco con un timer di 5 secondi.")
    start = input()

    if start == "play":
        print("")
        print_iniziali()
    elif start == "info":
        print("Versione: relase - 1.0 ")
        print("")
        time.sleep(2)
        print("developer: Vincenzo Scarso")
        time.sleep(5)
        print("=====")
        print("START")
        print("=====")
        print("")
        print_iniziali()
    else:
        print("Scusa non ho capito")
        print("Starting del programma...")
        time.sleep(2)
        print("")
        print("=====")
        print("START")
        print("=====")
        print("")
        print_iniziali()




def print_iniziali():
    #serie di print
    print('Ciao')
    time.sleep(1)
    print('come ti chiami?')
    risposta = input()
    print("...")
    time.sleep(2)
    print('Bene ' + risposta + ' giochiamo!!!')
    time.sleep(2)





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

    #randomizzatore di numeri
    a = range(1, 4)
    combinazione = random.sample(a, 1)

    #vincita
    if combinazione == [1] and cfs == 2:
        print("HO VINTO!!! io ho scelto carta")
        time.sleep(1)

    if combinazione == [2] and cfs == 3:
        print("HO VINTO!!! io ho scelto sasso")
        time.sleep(1)

    if combinazione == [3] and cfs == 1:
        print("HO VINTO!!! io ho scelto forbice")
        time.sleep(1)

    #perdita
    if combinazione == [2] and cfs == 1:
        print("ho perso :( io ho scelto sasso")
        time.sleep(1)

    if combinazione == [3] and cfs == 2:
        print("ho perso :( io ho scelto forbice")
        time.sleep(1)

    if combinazione == [1] and cfs == 3:
        print("ho perso :( io ho scelto carta")
        time.sleep(1)

    # input errato
    if cfs > 3:
        print('Prego scegliere tra carta=1 sasso=2 forbice=3')
        time.sleep(1)


    else:
        print("-_-")





def final():
    print("Bene il gioco è ora terminato si desidera continuare a giocare oppure ricominciare?")
    print("Nota: continuando verrà usato lo stesso nickname")
    print("[C]ontinuare o [R]icominciare")
    stay_leave = input()

    if stay_leave == "C":
        programma()

    if stay_leave == "R":
        print_iniziali()




start_program()

programma()

final()
