''' Kérj be két számot a felhasználótól
Írj eljárást
    számok néven, (ciklusok.py)
    melynek a paramérete a felhasználó által megadott két szám
    és
    az eljárás kiírja a számokat ezen két paraméter között.
'''

import ciklusok

a: int = int(input("a: "))

b: int = int(input("b: "))
'''A felhasználó csak olyan b-t tudjon megadni,ami nagyobb mint az a'''
while (a>b):
    print("B-nek nagyobbnak kell lenie A-nal")
    b:int = int(input(f"Adj {a}-nal nagyobbt!"))

ciklusok.szamok(a,b)