import whois

occupations = ['psychologist', 'lawyer', 'dentist', 'barber', 'hairstylist', 'optometrist', 'chiropractor', 'orthodontics', 'orthodontist', 'psychotherapy']
domains = []

with open('./cities.txt') as f:
    cities = f.read().splitlines()

for occ in occupations:
    for city in cities:
        domains.append(city + occ + '.com')
        print(city + occ + '.com')
open('./availabledomains.txt', 'w').close()  # delete all contens of file by opening it in writing mode


for dom in domains:
    print("Checking " + dom)
    try:
        w = whois.whois(dom)
    except whois.parser.PywhoisError:
        li = open('availabledomains.txt', 'a')
        li.write(dom + '\n')
        li.close()