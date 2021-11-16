# Program zwraca id uniprotowe, id organizmu, z którego pochodzi białko i sekwencję odczytaną z pliku pdb.
# Do id uniportowego dla plików pochodząxyxh z alphafolda dodałam _p, by wiedzieć potem, że to predykcja.
# Nazwy plików to skopiowany wynik z mojego programu pfam_alphafold_get_pdb.py, który pobrał te sekwencje
# W przypadków plików pochodzących z PDB nazwa informuje o kodzie uniprot, kodzie organizmu i kodzie pdb.

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
    try:
        for aminokwas in sekwencja:
            sekwencja_skroty += slownik[aminokwas]
    except:
        pass
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

pliki_z_pdb = ['P0C079_83333_2K29.pdb', 'P0C079_83333_2KC8.pdb', 'P0C079_83333_4FXE.pdb', 'P0AFY8_83333_1IU3.pdb',
               'P0AFY8_83333_1J3E.pdb', 'P0AFY8_83333_1LRR.pdb', 'P0AFY8_83333_1XRX.pdb', 'P0AFY8_83333_2CH3.pdb',
               'P0AFY8_83333_3FMT.pdb', 'P0A6Z6_83333_1Q5V.pdb', 'P0A6Z6_83333_1Q5Y.pdb', 'P0A6Z6_83333_2HZA.pdb',
               'P0A6Z6_83333_2HZV.pdb', 'P0A6Z6_83333_3BKF.pdb', 'P0A6Z6_83333_3BKT.pdb', 'P0A6Z6_83333_3BKU.pdb',
               'P0A6Z6_83333_3OD2.pdb', 'G3XCY4_208964_3QOQ.pdb', 'Q47150_83333_4Q2U.pdb', 'P03049_10754_1MNT.pdb',
               'P03049_10754_1QEY.pdb', 'P0A8N0_83333_4D8J.pdb', 'P62552_83333_2ADL.pdb', 'P62552_83333_2ADN.pdb',
               'P62552_83333_2H3A.pdb', 'P62552_83333_2H3C.pdb', 'P62552_83333_3G7Z.pdb', 'P62552_83333_3HPW.pdb',
               'P0A8U6_83333_1CMA.pdb', 'P0A8U6_83333_1CMB.pdb', 'P0A8U6_83333_1CMC.pdb', 'P0A8U6_83333_1MJ2.pdb',
               'P0A8U6_83333_1MJK.pdb', 'P0A8U6_83333_1MJL.pdb', 'P0A8U6_83333_1MJM.pdb', 'P0A8U6_83333_1MJO.pdb',
               'P0A8U6_83333_1MJP.pdb', 'P0A8U6_83333_1MJQ.pdb', 'P22995_562_2AN7.pdb', 'P96621_224308_4ME7.pdb',
               'O25896_85962_2CA9.pdb', 'O25896_85962_2CAD.pdb', 'O25896_85962_2CAJ.pdb', 'O25896_85962_2WVB.pdb',
               'O25896_85962_2WVC.pdb', 'O25896_85962_2WVD.pdb', 'O25896_85962_2WVE.pdb', 'O25896_85962_2WVF.pdb',
               'O25896_85962_3LGH.pdb', 'O25896_85962_3PHT.pdb', 'O25896_85962_3QSI.pdb', 'O25896_85962_6MRJ.pdb',
               'P9WLM7_83332_4CHG.pdb', 'A0A140ND86_469008_4ML0.pdb', 'P67697_83333_6HPB.pdb', 'P67697_83333_6HPC.pdb',
               'P58091_190650_3KXE.pdb', 'P13920_1311_1B01.pdb', 'P13920_1311_1EA4.pdb', 'P13920_1311_2CPG.pdb',
               'Q63NA5_272560_6G1C.pdb', 'Q63NA5_272560_6G1N.pdb', 'Q63NA5_272560_6G26.pdb', 'O58316_70601_2BJ1.pdb',
               'O58316_70601_2BJ3.pdb', 'O58316_70601_2BJ7.pdb', 'O58316_70601_2BJ8.pdb', 'O58316_70601_2BJ9.pdb',
               'P11906_562_4A62.pdb', 'B5Z8Y5_563041_2Y3Y.pdb', 'P03050_10754_1ARQ.pdb', 'P03050_10754_1ARR.pdb',
               'P03050_10754_1B28.pdb', 'P03050_10754_1BAZ.pdb', 'P03050_10754_1BDT.pdb', 'P03050_10754_1BDV.pdb',
               'P03050_10754_1MYK.pdb', 'P03050_10754_1MYL.pdb', 'P03050_10754_1NLA.pdb', 'P03050_10754_1PAR.pdb',
               'P03050_10754_1QTG.pdb', 'P03050_10754_1U9P.pdb', 'Q57812_243232_2EFV.pdb', 'O07227_83332_3H87.pdb',
               'O53778_83332_5X3T.pdb', 'P0CL61_83332_6KYT.pdb', 'Q9K2J6_243277_1Y9B.pdb', 'O25010_85962_1X93.pdb',
               'C3TAR7_562_6U0I.pdb', 'Q57468_1314_1IRQ.pdb', 'Q57468_1314_2BNW.pdb', 'Q57468_1314_2BNZ.pdb',
               'Q57468_1314_2CAX.pdb', 'A0A0N8J336_562_5WTU.pdb', 'J7QA90_562_6AJM.pdb', 'J7QA90_562_6AJN.pdb',
               'J7QA90_562_6GTO.pdb', 'J7QA90_562_6GTQ.pdb', 'J7QA90_562_6GTR.pdb', 'J7QA90_562_6GTS.pdb',
               'Q8EGZ2_211586_6IYA.pdb', 'F7Y4V9_536019_6X0A.pdb', 'F7YBW8_536019_5CEG.pdb', 'F7YBW8_536019_6X0A.pdb',
               'Q7VY20_257313_3KK4.pdb', 'A0A5P8YCM0_632_4P78.pdb', 'A0A5P8YCM0_632_4P7D.pdb', 'Q5SJJ5_300852_1WV8.pdb',
               'A0A0H3GLZ1_1125630_5ZGN.pdb', 'Q8NL33_190486_2K6L.pdb', 'Q9KJ82_108619_1P94.pdb',
               'Q9KJ82_108619_5U1G.pdb', 'Q9ZLR7_85963_2K1O.pdb', 'Q8ZG78_632_3VEA.pdb', 'Q8ZG78_632_3VEB.pdb',
               'P62553_83334_3TCJ.pdb', 'P07166_176299_2RH3.pdb', 'P9WJ35_83332_4XGQ.pdb', 'P9WJ35_83332_4XGR.pdb',
               'P9WLU3_83332_6A7V.pdb', 'Q5G3N6_1351_6QEQ.pdb', 'Q6EEF9_31966_3NO7.pdb']
for plik in pliki_z_pdb:
    uniprot_id, organizm_id, pdb_id = plik.split('_')
    print(f'>{uniprot_id} {organizm_id} {pdb_id[:-4]}\n{tlumaczenia_na_skroty(plik)}')
