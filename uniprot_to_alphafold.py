import wget

bialka2=open('bialka.txt').readlines()
print(len(bialka2))
bialka2=[i[:-1] for i in bialka2]
bialka=[['P0C079', '83333'], ['P0AFY8', '83333'], ['P9WJ47', '83332'], ['P95006', '83332'], ['P9WL41', '83332'], ['P9WIJ7', '83332'], ['P9WJ45', '83332'], ['P0A6Z6', '83333'], ['P9WJ87', '83332'], ['P9WJ57', '83332'], ['P9WJ09', '83332'], ['P9WJ43', '83332'], ['P9WLM7', '83332'], ['Q57812', '243232'], ['Q60386', '243232'], ['O07227', '83332'], ['O53778', '83332'], ['P9WJ29', '83332'], ['P0AAU7', '83333'], ['P9WJ49', '83332'], ['P0A8U6', '83333'], ['P67697', '83333'], ['P0CL61', '83332'], ['P9WLZ1', '83332'], ['P9WJ33', '83332'], ['Q59073', '243232'], ['P13959', '83333'], ['P62552', '83333'], ['Q47150', '83333'], ['P0A8N0', '83333'], ['O06779', '83332'], ['Q57969', '243232'], ['P9WJ59', '83332'], ['P9WJ35', '83332'], ['P9WLU3', '83332'], ['Q58177', '243232'], ['P06627', '83333'], ['P9WJ19', '83332'], ['P0ADQ5', '83333'], ['P9WKS5', '83332'], ['Q58522', '243232'], ['P9WJ39', '83332'], ['O53811', '83332'], ['P9WJ31', '83332'], ['P0CW33', '83332'], ['A0A4S5AWG6', '83333'], ['A0A6D2Y319', '83333'], ['A0A4V3YUV1', '83333'], ['O06243', '83332'], ['A0A4S5AMA0', '83333'], ['A0A6D2VVF0', '83333'], ['O53702', '83332'], ['O05910', '83332'], ['I6XFC2', '83332'], ['A0A6D2VV69', '83333'], ['A0A4S5AZB4', '83333'], ['A0A4S5APM6', '83333'], ['A0A4V3YTW5', '83333'], ['A0A4S5B2P6', '83333'], ['A0A4S5AP11', '83333'], ['A0A4S5AMB7', '83333'], ['A0A6D2WMJ6', '83333'], ['A0A4S4NZT2', '83333'], ['A0A6D2X6W5', '83333'], ['A0A367GJC0', '3847']]
licznik=0
wynik=[]
organizmy=set()
for protein2 in bialka:

    protein=protein2[0]
    try:
        wget.download(f'https://alphafold.ebi.ac.uk/files/AF-{protein}-F1-predicted_aligned_error_v1.json',f"{protein}.txt")
        wynik.append(protein)
        print(protein + ',')
        licznik+=1
        organizmy.add(protein2[1])
    except:
        pass
wynik.sort()
print(organizmy)
'''for i in range(0,47):
    if wynik[i] not in bialka2:
        print('O nie', bialka[i][0])
    else:
        print('hurra')'''


