# Author: Edgars Liepa
# Date: 6.5.22 
# Descripton: Create a list of amino acid substitutions from multiple sequences 
# in single fasta file.
# Programm firstly creates pairvise allignment to reference sequnce 
# and then counts changed positions
# 
# Dependencies: BioPython   


from Bio import SeqIO
from datetime import datetime
import csv
import sys

if 2 > len(sys.argv):
    print("\nNo allignment file provided\nexample: python parse.py protein.fasta\n")
    exit()

print("Counting mutations for", sys.argv[1], "file")

# TODO add that you can specify reference optinally in other file


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Parse start time =", current_time)

records = list(SeqIO.parse(sys.argv[1], "fasta"))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Parse end Time =", current_time)

print("Reference: ",records[0].description)

mutationList = []
haploTypeList = []

# Set up List with reference sequnce
for index, letter in enumerate(records[0].seq):
    mutationList.append({letter: 0})

for i in range (1, len(records)):
    haploType = {}
    for index, letter in enumerate(records[i].seq):
        if index >= len(mutationList): # sequence is larger than reference and aa sub. array
            mutationList.append({letter: 1})             
        elif (letter not in mutationList[index]): # aa sub. seen first time       
            mutationList[index][letter] = 1
            haploType[index] = [letter]
        else:   # aa sub is in the mutation list, increase aa counter
            if (index < len(records[0].seq)): # index is in the reference range
                if (letter != records[0].seq[index]):
                    mutationList[index][letter] += 1
                    haploType[index] = [letter]
            else:
                mutationList[index][letter] += 1
                haploType[index] = [letter]
        haploTypeList.append(haploType)
    # print(haploType)  

# Print Results

header = ['Postion', 'aaSubst', 'Count']

with open('mutations.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for index, position in enumerate(mutationList):
        for aa in  position.keys():
            if position[aa] != 0:
                print("Postion: ", index+1, "aaSubst: ", aa, "Count: ", position[aa])
                writer.writerow([index+1, aa, position[aa]])



print("AA substitition counts saved at ")  

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

