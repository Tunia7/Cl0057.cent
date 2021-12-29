import wget
import os.path

with open(r"cl0057_members_from_html.txt") as plik:
    html_kod = plik.readlines()
rodziny = []
for linia in html_kod:
    linia = linia.strip()
    if linia[:14] == r'href="/family/':
        rodziny.append(linia[14:-2])  # przykładowa linijka to "href="/family/PF19807">"
wszystkie_zakresy = ""
for rodzina in rodziny:
    if 0 == os.path.isfile(f"{rodzina}.txt"):
        wget.download(
            fr"http://pfam.xfam.org/family/{rodzina}/alignment/full/format?format=pfam&alnType=full&order=t&case=l&gaps=dashes&download=0",
            f"{rodzina}.txt")
    with open(f"{rodzina}.txt") as plik:
        dane = plik.readlines()
        for linia in dane:
            wszystkie_zakresy += linia

print(wszystkie_zakresy)
plik = open("wszystkie_zakresy_z_pfam.txt", "w")
plik.write(wszystkie_zakresy)
plik.close()
