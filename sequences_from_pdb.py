# Program zwraca id uniprotowe, id organizmu, z którego pochodzi białko i sekwencję odczytaną z pliku pdb.
# Do id uniportowego dodałam _p, by wiedzieć potem, że to predykcja.
# Nazwy plików to skopiowany wynik z mojego programu pfam_alphafold_get_pdb.py, który pobrał te sekwencje


# zwraca podzielony na zesplitowane linijki plik
def otwieranie_pliku(nazwa_pliku):
    plik = open(nazwa_pliku)
    linijki = plik.readlines()
    plik.close()
    linijki = [linia.split() for linia in linijki]
    return linijki


# zwraca sekwencję wyciągniętą z pdb w formacie skrótów 3-literowych
def wyciagniecie_sekwencji(plik):
    pdb = otwieranie_pliku(plik)
    sekwencja = []
    for linia in pdb:
        if linia[0] == 'SEQRES':
            for aminokwas in linia[4:]:
                sekwencja.append(aminokwas)
    return sekwencja


# tłumaczy skróty 3-literowe na 1-literowe
def tlumaczenia_na_skroty(plik):
    sekwencja = wyciagniecie_sekwencji(plik)
    sekwencja_skroty = ''
    for aminokwas in sekwencja:
        sekwencja_skroty += slownik[aminokwas]
    return sekwencja_skroty


slownik = d = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
               'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
               'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
               'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

pliki = ['P0C079_83333.pdb', 'P0AFY8_83333.pdb', 'P9WJ47_83332.pdb', 'P95006_83332.pdb', 'P9WL41_83332.pdb',
         'P9WIJ7_83332.pdb', 'P9WJ45_83332.pdb', 'P0A6Z6_83333.pdb', 'P9WJ87_83332.pdb', 'P9WJ57_83332.pdb',
         'P9WJ09_83332.pdb', 'P9WJ43_83332.pdb', 'P9WLM7_83332.pdb', 'Q57812_243232.pdb', 'Q60386_243232.pdb',
         'O07227_83332.pdb', 'O53778_83332.pdb', 'P9WJ29_83332.pdb', 'P0AAU7_83333.pdb', 'P9WJ49_83332.pdb',
         'P0A8U6_83333.pdb', 'P67697_83333.pdb', 'P0CL61_83332.pdb', 'P9WLZ1_83332.pdb', 'P9WJ33_83332.pdb',
         'Q59073_243232.pdb', 'Q47150_83333.pdb', 'P0A8N0_83333.pdb', 'O06779_83332.pdb', 'Q57969_243232.pdb',
         'P9WJ59_83332.pdb', 'P9WJ35_83332.pdb', 'P9WLU3_83332.pdb', 'Q58177_243232.pdb', 'P9WJ19_83332.pdb',
         'P0ADQ5_83333.pdb', 'P9WKS5_83332.pdb', 'Q58522_243232.pdb', 'P9WJ39_83332.pdb', 'O53811_83332.pdb',
         'P9WJ31_83332.pdb', 'P0CW33_83332.pdb', 'O06243_83332.pdb', 'O53702_83332.pdb', 'O05910_83332.pdb',
         'I6XFC2_83332.pdb', 'A0A367GJC0_3847.pdb']

for plik in pliki:
    uniprot_id, organizm_id = plik.split('_')
    print(f'>{uniprot_id}_p {organizm_id[:-4]}\n{tlumaczenia_na_skroty(plik)}')
