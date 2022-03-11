import requests

# https://www.dns.pl/lista_domen_funkcjonalnych

# https://www.dns.pl/lista_domen_regionalnych


def get_flags(url):
    raw = requests.get(url).text
    lines = raw.split('</p>')
    listed = []
    for line in lines:
        line = line.replace('<p>', '')
        line = line.replace('- ', '')
        line = line.lower().strip()
        listed.append(line)
    return listed


def clean_tlds(url):
    raw = requests.get(url).text
    lines = raw.split('\n')
    listed = []
    for line in lines:
        line = line.lower().strip()
        line = "." + line
        if '#' not in line and len(line) > 2:
            listed.append(line)
    return listed

# split text to lines, find <li>sted items and basic-clean, return iterable list


def clean_dns_pl(url):
    raw_info = requests.get(url)
    html = raw_info.text
    lines = html.split('\n')
    listed = []
    for line in lines:
        if '<li>' in line:
            line = line.replace('<li>', '')
            line = line.replace('</li>', '')
            line = line.strip().lower()
            listed.append(line)
    return listed


# ask for input: (url) to parse, filename to save to
def save_to_file():
    print("paste url: ")
    url = input()
    # for dns.pl
    # listed = clean_dns_pl(url)  
    # for flags
    listed = get_flags("https://zajecia-programowania-xd.pl/flagi") 
    # for tlds
    # listed = clean_tlds("https://data.iana.org/TLD/tlds-alpha-by-domain.txt") 
    print('save to file: ')
    filename = input()
    textfile = open(filename, "w", encoding="utf-8")
    for element in listed:
        textfile.write(element + "\n")
    textfile.close()


save_to_file()

# save_to_file(clean_dns_pl('https://www.dns.pl/lista_domen_regionalnych'))
