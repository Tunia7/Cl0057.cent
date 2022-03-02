# dostosowyanie danych do pliku nexus, by miały odpowiednie długości
wynik = ""
with open("pfam.txt") as plik:

    przerwy = ""
    for i in range(0, 26):
        przerwy += "-"
    for linia in plik.readlines():
        linia = linia.strip().split()
        linia[1] = linia[1][:72] + przerwy+linia[1][73:]
        wynik+=linia[0]+"\t"+linia[1]+"\n"

with open("alphafold.txt") as plik:
    słownik={}
    przerwy = ""
    for i in range(0, len("99999999953321141777777123131336252116")):
        przerwy += "?"
    for linia in plik.readlines():
        linia=linia.strip().split()
        if linia[0] in słownik.keys():
            słownik[linia[0]]=słownik[linia[0]]+linia[1]
        else:
            słownik[linia[0]]=linia[1]

    for klucz in słownik.keys():
        wynik+=klucz+"\t"+słownik[klucz]+przerwy+"\n"

print(wynik)