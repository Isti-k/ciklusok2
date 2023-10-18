''' Kérj be két számot a felhasználótól
Írj eljárást
    számok néven, (ciklusok.py)
    melynek a paramérete a felhasználó által megadott két szám
    és
    az eljárás kiírja a számokat ezen két paraméter között.
'''

import ciklusok

a: int = int(input("Adjon meg egy számot!"))
b: int = int(input("Adjon meg egy számot!"))
ciklusok.szamok(a,b)