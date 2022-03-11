import re

domains = ["cos.pl", "cos2.pl", "cos.eu", "cos.online", "cos2.eu", "cos3.pl"]

# tlds = [".eu", ".online"]
tlds = []
with open('tlds.txt') as file:
    tlds = [line.rstrip() for line in file]

# works
# r = re.compile(".*eu")
selected = []
for domain in domains:
    for tld in tlds:
        r = r".*" + tld + ""
        if re.search(r, domain):
            selected.append(domain)

# TEXTO = sys.argv[1]
# my_regex = r".*" + eu + r"\b(?!\w)"

# if re.search(my_regex, subject, re.IGNORECASE):

print(selected)
