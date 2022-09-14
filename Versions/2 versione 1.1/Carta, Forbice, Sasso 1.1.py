import random
import time


def start_program():
    print("")
    print("Benvenuto utente questa è la versione digitale di Carta, Forbice, Sasso.")
    print("Per giocare scrivere 'play' e inviare per mostrare ulteriori info"
        " digitare")
    print("'info' e inviare, dopo la rivelazione delle info  il gioco partirà automaticamente")
    start = input()

    if start == "play":
        print("")
        print_iniziali()
    elif start == "info":
        print("Versione: relase - 1.1")
        print("")
        time.sleep(1)
        print("developer: Vincenzo Scarso")
        time.sleep(2)
        print("")
        print("=====")
        print("START")
        print("=====")
        print("")
        time.sleep(1)
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
        time.sleep(1)
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
    combinazione= random.sample(a, 1)

    #vincita
    if combinazione == [1] and cfs == 2:
        print("HO VINTO!!! io ho scelto carta")
        final()

    if combinazione == [2] and cfs == 3:
        print("HO VINTO!!! io ho scelto sasso")
        final()

    if combinazione == [3] and cfs == 1:
        print("HO VINTO!!! io ho scelto forbice")
        final()


    #perdita
    if combinazione == [2] and cfs == 1:
        print("ho perso :( io ho scelto sasso")
        final()

    if combinazione == [3] and cfs == 2:
        print("ho perso :( io ho scelto forbice")
        final()

    if combinazione == [1] and cfs == 3:
        print("ho perso :( io ho scelto carta")
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
    print("Bene il gioco è ora terminato si desidera continuare a giocare oppure ricominciare?")
    print("Nota: continuando verrà usato lo stesso nickname.")
    print("Se si preferisce uscire premere qualsiasi altra lettera e inviare.")
    print("[C]ontinuare o [R]icominciare")
    stay_leave = input()

    if stay_leave == "C":
        programma()

    if stay_leave == "R":
        print_iniziali()




#___STARTER___
start_program()
