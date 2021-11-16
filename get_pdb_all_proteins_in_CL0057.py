import wget


def otwieranie_pliku(nazwa_pliku):
    plik = open(nazwa_pliku)
    linijki = plik.readlines()
    plik.close()
    linijki = [linia.strip().split() for linia in linijki]
    return linijki


def pobieranie_pdb(plik):
    pliki = []
    białka = otwieranie_pliku(plik)[1:]
    for białko in białka:
        if len(białko) == 3:
            id_pdb = białko[2].split(";")
            for id in id_pdb[:-1]:
                try:
                    wget.download(f"https://files.rcsb.org/download/{id}.pdb", f"{białko[0]}_{białko[1]}_{id}.pdb")
                    pliki.append(f"{białko[0]}_{białko[1]}_{id}.pdb")
                except:
                    pass
    return pliki


print(pobieranie_pdb("cl0057_with_pdb_references.txt"))
