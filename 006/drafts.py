import random
import string

# Generator Hasła
# - string - ciag znakow
# - losowe hasło
# - okreslona ilosc znakow - ponad 8
# - Duże litery, 2
# - Małe litery, 2
# - Znaki specjalne, 2
# - Cyfry, 2

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation
digits = string.digits
wszystkie_znaki = [lowercase, uppercase, punctuation, digits]

n_znakow = 0
while n_znakow not in range(12, 21):
    print('Wybierz liczbę znaków hasła (12-20)')
    n_znakow = int(input())


haslo = ""
wylosowana_lista = []
while len(wylosowana_lista) < n_znakow:
    print(f"dl listy {len(wylosowana_lista)}")
    for typ_znakow in wszystkie_znaki:
        wylosowana_lista += random.sample(typ_znakow, 1)
    random.shuffle(wylosowana_lista)
    haslo = ''.join(wylosowana_lista)[:n_znakow]
    print(len(wylosowana_lista))

print(haslo)
print(len(haslo))

# n_znakow_typu = 2
# wylosowana_lista = []
# while len(wylosowana_lista) < n_znakow:
#     for typ_znakow in wszystkie_znaki:
#         wylosowana_lista += random.sample(typ_znakow, n_znakow_typu)
#     random.shuffle(wylosowana_lista)
#     print(len(wylosowana_lista))

# haslo = ''.join(wylosowana_lista)[:n_znakow]
# print(haslo)
# print(len(haslo))

# losowe_znaki = random.sample(wszystkie_znaki, n_znakow)
# print(losowe_znaki)
# haslo = ''.join(losowe_znaki)

# print()
# print(haslo)
# print()

# Zadanie domowe:

# Udoskonalić generator haseł tak aby:
# 1. brał po 2 losowe cyfry/znaki i duze/male litery
# 2. losowa kolejnosc cyfr, znakow, duzych i malych liter
# 3. Pogłówkujcie co robic aby to dzialalo dobrze dla zadanej
#    liczby znakow od 12 do 20
