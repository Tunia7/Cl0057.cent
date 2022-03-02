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
    if 0 == os.path.isfile(f"{rodzina}.fasta"):
        wget.download(
            fr"http://pfam.xfam.org/family/{rodzina}/alignment/full/format?format=fasta&alnType=full&order=t&case=l&gaps=default&download=0",
            f"{rodzina}.fasta")
    with open(f"{rodzina}.fasta") as plik:
        dane = plik.readlines()
        for linia in dane:
            wszystkie_zakresy += linia



print(wszystkie_zakresy)
