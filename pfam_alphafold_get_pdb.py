import wget
import os


def get_ids(clan):
    with open(clan) as file:
        families = file.readlines()
        families = families[0].split()
        link = r"https://www.uniprot.org/uniprot/?query="
        for family in families:
            link += f'database:(type:pfam%20{family})%20OR%20'
        link = link[:-8] + '&format=tab&columns=id,organism-id&sort=score'
        wget.download(link, "base.txt")


# organism ids in alphafold
organism_alphafold = ['7955', '237562', '10090', '83333', '7227', '243232', '36329', '83332', '6239', '44589',
                      '353153', '559292', '284812', '10116', '9606', '3702', '4577', '5671', '93061', '3847', '39947']
get_ids("cl0057.txt")
our_proteins = []
if os.path.isfile("base.txt") == 0:
    get_ids("cl0057.txt")
with open("base.txt") as file:
    for result in file.readlines()[1:]:
        result = result.split()
        print(result)
        id = result[0]
        organism = result[1]
        if organism in organism_alphafold:
            our_proteins.append(result)

# ranges
dict_ranges = {}
with open(r"zakresy.txt") as ranges:
    for line in ranges.readlines():
        print(line)
        line = line.strip().split("/")
        dict_ranges[line[0][1:]] = line[1].split("-")

for protein in our_proteins:# create table with names of pdb files

    if 0 == os.path.isfile(f'{protein[0]}_{protein[1]}.pdb'):
        try:
            wget.download(rf'https://alphafold.ebi.ac.uk/files/AF-{protein[0]}-F1-model_v1.pdb',
                          f"{protein[0]}_{protein[1]}.pdb")
        except:
            pass
    if 1 == os.path.isfile(f'{protein[0]}_{protein[1]}.pdb'):
        wget.download(rf'https://www.uniprot.org/uniprot/{protein[0]}.fasta', f'{protein[0]}_{protein[1]}.fasta')
        with open(f'{protein[0]}_{protein[1]}.fasta') as file:
            if protein[0] in dict_ranges.keys():
                print()
                print(f'>alphafold_{protein[0]}_{protein[1]}|')
                correct_range = dict_ranges[protein[0]]
                result = ""
                for line in file.readlines()[1:]:
                    result += line.strip()
                print(result[int(correct_range[0]):int(correct_range[1])])
