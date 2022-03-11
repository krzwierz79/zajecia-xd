import random
import string

male = string.ascii_lowercase
wielkie = string.ascii_uppercase
znaki = string.punctuation
cyfry = string.digits
wszystkie_znaki = [male, wielkie, znaki, cyfry]

n_znakow = 0
while n_znakow not in range(12, 21):
    print('Wybierz liczbę znaków hasła (12-20)')
    n_znakow = int(input())

haslo = ""
wylosowana_lista = []
while len(wylosowana_lista) < n_znakow:
    for typ_znakow in wszystkie_znaki:
        wylosowana_lista += random.sample(typ_znakow, 1)
    random.shuffle(wylosowana_lista)
    haslo = ''.join(wylosowana_lista)[:n_znakow]

print(f"Twoje haslo ({n_znakow} znaków) to {haslo}")
