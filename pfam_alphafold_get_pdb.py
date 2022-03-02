import wget
import os


# pobiera listę uniprot id i organizm id  białek należących do klanu
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


# identyfikatory organizmów na podstawie ftp alphafolda
alphafold_organizmy = ['7955', '237562', '10090', '83333', '7227', '243232', '36329', '83332', '6239', '44589',
                       '353153', '559292', '284812', '10116', '9606', '3702', '4577', '5671', '93061', '3847', '39947']

nasze_bialka = []
if os.path.isfile("baza.txt") == 0:
    rozbudowa_linku()
with open("baza.txt") as plik:
    for wynik in plik.readlines():
        wynik = wynik.split()
        id = wynik[0]
        organizm = wynik[1]
        if organizm in alphafold_organizmy:
            nasze_bialka.append(wynik)

# plik 'cl0057' zawiera listę rodzin z klanu w jednej linijce rodzielone spacją


# zakresy
słownik_zakresow = {}
with open(r"zakresy.txt") as zakresy:
    for linia in zakresy.readlines():
        print(linia)
        linia = linia.strip().split("/")
        słownik_zakresow[linia[0][1:]] = linia[1].split("-")

wynik = ""
# tworzy tablicę z nazwami plików pdb, które uda nam sie pobrać
for protein in nasze_bialka:
    if 0 == os.path.isfile(f'{protein[0]}_{protein[1]}.pdb'):
        try:
            wget.download(rf'https://alphafold.ebi.ac.uk/files/AF-{protein[0]}-F1-model_v1.pdb',
                          f"{protein[0]}_{protein[1]}.pdb")
        except:
            pass
    if 1 == os.path.isfile(f'{protein[0]}_{protein[1]}.pdb'):
        wget.download(rf'https://www.uniprot.org/uniprot/{protein[0]}.fasta', f'{protein[0]}_{protein[1]}.fasta')
        with open(f'{protein[0]}_{protein[1]}.fasta') as plik:
            if protein[0] in słownik_zakresow.keys():
                wynik += f'>alphafold_{protein[0]}_{protein[1]}|\n'

                zakres_odpowiedni=słownik_zakresow[protein[0]]
                pom=""
                for linia in plik.readlines()[1:]:
                    pom += linia.strip()
                wynik +=pom[int(zakres_odpowiedni[0]):int(zakres_odpowiedni[1])] + "\n"
print(wynik)
