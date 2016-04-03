print("Benvenuti!")
print('Calcolo Mentale----By SystX V.0.1')
import random

punteggio = 0
numero_1facile = random.randint(1, 25)
numero_2facile = random.randint(1, 20)
numero_1difficile = random.randint(25, 40)
numero_2difficile = random.randint(20, 35)
print("Pronti?\nPremi 1 per il livello 'facile' \nPremi 2 per il livello 'difficile'\nPremi tutt'altro tasto per uscire!")
a = int(input())
if a == 1:
    while True:
        print('Addizione o Moltiplicazione?\nPremi qualcos\'altro per uscire')
        b = str(input())
        if b == "addizione":
            while True:
                print(numero_1facile, "+", numero_2facile, "=")
                addizione = int(input())
                if addizione == numero_1facile + numero_2facile:
                    print("Esatto")
                    punteggio += 1
                    numero_1facile = random.randint(1, 25)
                    numero_2facile = random.randint(1, 20)
                else:
                    print("Sbagliato, la risposta corretta era", numero_1facile + numero_2facile)
                    punteggio -= 1
                    numero_1facile = random.randint(1, 25)
                    numero_2facile = random.randint(1, 20)
                if punteggio >= 20:
                    print("Bravo!!!Sei diventato esperto!")
        elif b == "moltiplicazione":
            while True:
                print(numero_1facile, "*", numero_2facile, "=")
                moltiplicazione = int(input())
                if moltiplicazione == numero_1facile * numero_2facile:
                    punteggio += 3
                    print("Esatto")
                    numero_1facile = random.randint(1, 25)
                    numero_2facile = random.randint(1, 20)
                    print(punteggio)
                else:
                    print("Sbagliato, la risposta corretta era", numero_1facile * numero_2facile)
                    punteggio -= 2
                    numero_1facile = random.randint(1, 25)
                    numero_2facile = random.randint(1, 20)
                if punteggio >= 20:
                    print("Hai vinto il gioco!!!Sei diventato esperto!")
        else:
            break
if a == 2:
    while True:
        print("Addizione o Moltiplicazione?\nPremi qualcos'altro per uscire")
        b = str(input())
        if b == "addizione":
            while True:
                print(numero_1difficile, "+", numero_2difficile, "=")
                addizione = int(input())
                if addizione == numero_1difficile + numero_2difficile:
                    print("Esatto")
                    punteggio += 3
                    numero_1difficile = random.randint(25, 40)
                    numero_2difficile = random.randint(20, 35)
                else:
                    print("Sbagliato, la risposta corretta era", numero_1difficile + numero_2difficile)
                    punteggio -= 2
                    numero_1difficile = random.randint(25, 40)
                    numero_2difficile = random.randint(20, 35)
                if punteggio>=100:
                    print("Hai vinto il gioco!Sei un sommo guru delle moltiplicazioni!!!")
        elif b == "moltiplicazione":
            while True:
                print(numero_1difficile, "*", numero_2difficile, "=")
                moltiplicazione = int(input())
                if moltiplicazione == numero_1difficile * numero_2difficile:
                    print("Esatto")
                    punteggio += 6
                    numero_1difficile = random.randint(25, 40)
                    numero_2difficile = random.randint(20, 35)
                else:
                    print("Sbagliato, la risposta corretta era", numero_1difficile * numero_2difficile)
                    punteggio -= 4
                    numero_1difficile = random.randint(25, 40)
                    numero_2difficile = random.randint(20, 35)
                if punteggio>=100:
                    print("Hai vinto il gioco!Sei un sommo guru delle moltiplicazioni!!!")
        else:
            break
