import random
import math
import os

green = [0]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
w_liczby = list(range(0, 37))
colors = ['red','green','black']


RED = '\033[31m'
GREEN = '\033[32m'
BLACK = '\033[30m'
RESET = '\033[0m' 


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def rulet():
    r = random.randint(0, 36)
    return r

def sprawdzanie_p_l(r, p_l): 
    if r != 0 and p_l == 0: 
        clear()
        print(f"Wygrałeś🎉!\nWypadła liczba parzysta\n= {r} =")
    else:
        clear()
        print(f"Przegrałeś\nWypadła liczba nieparzysta lub zero\n= {r} =")
    input("Naciśnij Enter, aby kontynuować...")
    main()

def sprawdzanie_np_l(r, p_l):
    if p_l != 0:
        clear()
        print(f"Wygrałeś🎉!\nWypadła liczba nieparzysta\n= {r} =")
    else:
        clear()
        print(f"Przegrałeś\nWypadła liczba parzysta lub zero\n= {r} =")
    input("Naciśnij Enter, aby kontynuować...")
    main()

def kolor_green(r,k_l,kolor):
    clear()
    print("Wygrałeś🎉!" if kolor == 'green' else "Przegrana")
    print(f"Wylosowany kolor i liczba to = {r} = {GREEN}green{RESET} =\nWybrany kolor to = {kolor} =")
    input("Naciśnij Enter, aby kontynuować...")
    main()

def kolor_red(r,k_l,kolor):
    clear()
    print("Wygrałeś🎉!" if kolor == 'black' else "Przegrana")
    print(f"Wylosowany kolor i liczba to = {r} = {RED}red{RESET} =\nWybrany kolor to = {kolor} =")
    input("Naciśnij Enter, aby kontynuować...")
    main()

def kolor_black(r,k_l,kolor):
    clear()
    print("Wygrałeś🎉!" if kolor == 'red' else "Przegrana")
    print(f"Wylosowany kolor i liczba to = {r} = {BLACK}black{RESET} =\nWybrany kolor to = {kolor} =")
    input("Naciśnij Enter, aby kontynuować...")
    main()


def main():
    clear()
    player_input = input("-----wybory-----\n1-Podaj liczbę\n2-Podaj kolor\n3-Parzysta\n4-Nie parzysta\n== ").lower()

    if player_input == '1':
        wybor_n = int(input("Podaj liczbę 0-36: "))
        if wybor_n in w_liczby:
            r = rulet()
            print(f"Twoja liczba: {wybor_n}, Wylosowana: {r}")
            print("Wygrałeś🎉!" if wybor_n == r else "Przegrana")
            input("Naciśnij Enter, aby kontynuować...")
            main()

    elif player_input == '2':
        clear()
        kolor = input("Dostępne kolory:\nblack\nred\ngreen\n== ").lower()
        while kolor not in colors:
            clear()
            kolor = input(f"Zły kolor {kolor}\nDostępne kolory:\nblack\nred\ngreen\n== ").lower()
            
        
        r = rulet()

        if r in green:
            k_l = 1
            kolor_green(r,k_l,kolor)

        elif r in black:
            k_l = 2
            kolor_black(r,k_l,kolor)

        elif r in red:
            k_l = 3
            kolor_red(r,k_l,kolor)

    

    elif player_input == '3':
        r = rulet()
        p_l = r % 2
        sprawdzanie_p_l(r, p_l)

    elif player_input == '4':
        r = rulet()
        p_l = r % 2
        sprawdzanie_np_l(r, p_l)

clear()
main()
