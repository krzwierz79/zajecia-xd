import re

# local_flags = []
with open('flags.txt', encoding="utf-8") as file:
    local_flags = [line.rstrip() for line in file]


# tlds = []  # ['.eu','.pl','.online']
with open('tlds_short.txt') as file:
    tlds = [line.rstrip() for line in file]

# TODO: jak to napisać krócej?
# local_flags = ["kubel-wody.pl", "cebula.pl", "turbo-gabka.eu", "xd.online", "woreknakulki.pl", "kamera.online"]
# tld = ['.eu','.pl','.online']
# categories = {"Domeny: " + k: [el for el in local_flags if k in el] for k in tld} daje słownik który daje taki wynik dla skróconych (wymyślonych) danych -->>> {'Domeny: .eu': ['turbo-gabka.eu'], 'Domeny: .pl': ['kubel-wody.pl', 'cebula.pl', 'woreknakulki.pl'], 'Domeny: .online': ['xd.online', 'kamera.online']}

categories_d = {"Domeny: " +
                k: [el for el in local_flags if k in el] for k in tlds}

categories_l = [[el for el in local_flags if k in el] for k in tlds]

# tl_domains = []
# for link in local_flags:
#     for tld in tlds:
#         r = r".*" + tld + "$"
#         if re.search(r, link):
#             tl_domains.append(link)

print(categories_d)
# print(tl_domains)
print(categories_l)
