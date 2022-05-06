from Bio import SeqIO
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Parse start time =", current_time)

records = list(SeqIO.parse("../s_protein_NCBI_2.aln", "fasta"))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Parse end Time =", current_time)

# This is my reference
print(records[0].id)  # first record
print(records[0].description)

mutationList = []
haploTypeList = []

# Set up List with reference sequnce
for index, letter in enumerate(records[0].seq):
    mutationList.append({letter: 0})

for i in range (1, len(records)):
    haploType = {}
    for index, letter in enumerate(records[i].seq):
        if (letter not in mutationList[index]):       
            mutationList[index][letter] = 1
            haploType[index] = [letter]
        elif (letter != records[0].seq[index]):
            mutationList[index][letter] += 1
            haploType[index] = [letter]
        haploTypeList.append(haploType)
    print(haploType)  

# Print Results
for index, position in enumerate(mutationList):
    for aa in  position.keys():
        if position[aa] != 0:
            print("Postion: ", index+1, "aaSubst: ", aa, "Count: ", position[aa] )


# print(mutationList)  

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


# # Create Plot 

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import rc
# import pandas as pd

# # Data
# # r = [0,1,2,3,4]
# r = range(len(mutationList))

# # raw_data = {'greenBars': [20, 1.5, 7, 10, 5], 'orangeBars': [5, 15, 5, 10, 15],'blueBars': [2, 15, 18, 5, 10]}
# df = pd.DataFrame(mutationList)
 
# # From raw value to percentage
# totals = [i+j+k for i,j,k in zip(df['greenBars'], df['orangeBars'], df['blueBars'])]
# greenBars = [i / j * 100 for i,j in zip(df['greenBars'], totals)]
# orangeBars = [i / j * 100 for i,j in zip(df['orangeBars'], totals)]
# blueBars = [i / j * 100 for i,j in zip(df['blueBars'], totals)]

# # plot
# barWidth = 0.85
# names = ('A','B','C','D','E')

# # Create green Bars
# plt.bar(r, greenBars, color='#b5ffb9', edgecolor='white', width=barWidth, label="group A")
# # Create orange Bars
# plt.bar(r, orangeBars, bottom=greenBars, color='#f9bc86', edgecolor='white', width=barWidth, label="group B")
# # Create blue Bars
# plt.bar(r, blueBars, bottom=[i+j for i,j in zip(greenBars, orangeBars)], color='#a3acff', edgecolor='white', width=barWidth, label="group C")
 
# # Custom x axis
# plt.xticks(r, names)
# plt.xlabel("group")
 
# # Add a legend
# plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
 
# # Show graphic
# plt.savefig('aa_sub.png')
