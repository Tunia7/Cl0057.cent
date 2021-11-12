import wget


# zwraca link zwracający uniprot id białek należących do klanu
def rozbudowa_linku(klan):
    plik = open(klan)
    rodziny = plik.readlines()
    plik.close()
    rodziny = rodziny[0].split()
    link_bazowy = r"https://www.uniprot.org/uniprot/?query="
    for rodzina in rodziny:
        link_bazowy += f'database:(type:pfam%20{rodzina})%20OR%20'
    link_bazowy = link_bazowy[:-8] + '&columns=id,organism-id'
    wget.download(link_bazowy, "baza.txt")
    print(link_bazowy)


# identyfikatory organizmów na podstawie ftp alphafolda
alphafold_organizmy = ['7955', '237562', '10090', '83333', '7227', '243232', '36329', '83332', '6239', '44589',
                       '353153', '559292', '284812', '10116', '9606', '3702', '4577', '5671', '93061', '3847', '39947']

nasze_bialka = []
plik = open("baza.txt").readlines()
for wynik in plik:
    wynik = wynik.split()
    id = wynik[0]
    organizm = wynik[1]
    if organizm in alphafold_organizmy:
        nasze_bialka.append(wynik)

rozbudowa_linku("cl0057")
# plik 'cl0057' zawiera listę rodzin z klanu w jednej linijce rodzielone spacją

print(nasze_bialka)  # tablica dwuelementowych tablic, gdzie pierwszy element uniprot id, a drugi organism id
print(len(nasze_bialka))
# pobiera predicted aligned error, zlicza białka, których predykcje są w alphafoldzie
licznik = 1
wynik = []
for protein in nasze_bialka:
    print(protein[0])
    try:
        wget.download(rf'https://alphafold.ebi.ac.uk/files/AF-{protein[0]}-F1-predicted_aligned_error_v1.json',
                      f"{protein[0]}_{protein[1]}.json")
        print(protein[0] + ",")
        licznik += 1
    except:
        pass
print(licznik)
