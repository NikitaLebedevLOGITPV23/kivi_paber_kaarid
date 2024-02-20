from random import *

player1=input("Sisestage mängija 1 nimi: ")
player2=input("Sisestage mängija 2 nimi: ")
voor=int(input("Mitu vooru soovite mängida? "))

player1_punkt=0
player2_punkt=0
viik=0

for i in range(viik):
    print(f"\nVoor {i + 1}:")

mylist=["kivi", "käärid", "paber"]
liigutus1=choice(mylist)
liigutus2=choice(mylist)

while True:
    print(f"{player1} näitas: {liigutus1}")
    print(f"{player2} näitas: {liigutus2}")
    if liigutus1 == liigutus2:
            print("Viik!")
            viik+=1
    elif (liigutus1=="kivi" and liigutus2=="käärid") or \
        (liigutus1=="käärid" and liigutus2=="paber") or  \
        (liigutus1=="paber" and liigutus2=="kivi"):
        print(f"{player1} võitis vooru!")
        player1_punkt+=1
    else:
        print(f"{player2} võitis vooru!")
        player2_punkt+=1
        break

    print("\nMängu tulemused:")
    print(f"{player1}: {player1_punkt} punkti")
    print(f"{player2}: {player2_punkt} punkti")
    print(f"Viik: {viik} korda")

import random

player1_name = input("Sisestage mängija 1 nimi: ")
player2_name = input("Sisestage mängija 2 nimi: ")
rounds = int(input("Mitu vooru soovite mängida? "))


