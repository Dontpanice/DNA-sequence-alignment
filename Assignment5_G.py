#Arnaud Moulis
import matplotlib.pyplot as plt
from scipy.spatial import distance


P1_data  = []
with open('1CDH.pdb') as pdbfile:
    for line in pdbfile:
        if line[:4] == 'ATOM' or line[:6] == 'HETATM':
            
            # Split the line
            splitted_line = [line[:4], line[9:11], line[13:15], line[17:20], line[21], line[21:22], line[30:38], line[38:46], line[46:54]]
#            print (splitted_line)
            P1_data.append(splitted_line)
            # To format again the pdb file with the fields extracted
#            print ("%-6s%5s %4s %3s %s%4s    %8s%8s%8s\n"%tuple(splitted_line))


Xcord = []
Ycord = []
Zcord = []


for i in range(0, len(P1_data)):
    Zcord.append(float(P1_data[i][-1])) 
    Ycord.append(float(P1_data[i][-2]))
    Xcord.append(float(P1_data[i][-3]))

P1_atoms = list(zip(Xcord,Ycord,Zcord))
list_P1_atoms = list(P1_atoms)




P2_data  = []
with open('2CSN.pdb') as pdbfile:
    for line in pdbfile:
        if line[:4] == 'ATOM' or line[:6] == 'HETATM':
            
            # Split the line
            splitted_line = [line[:4], line[9:11], line[13:15], line[17:20], line[21], line[21:22], line[30:38], line[38:46], line[46:54]]
#            print (splitted_line)
            P2_data.append(splitted_line)
            # To format again the pdb file with the fields extracted
#            print ("%-6s%5s %4s %3s %s%4s    %8s%8s%8s\n"%tuple(splitted_line))


Xcord2 = []
Ycord2 = []
Zcord2 = []


for i in range(0, len(P2_data)):
    Zcord2.append(float(P2_data[i][-1])) 
    Ycord2.append(float(P2_data[i][-2]))
    Xcord2.append(float(P2_data[i][-3]))

P2_atoms = list(zip(Xcord2,Ycord2,Zcord2))
list_P2_atoms = list(P2_atoms)

before_comparisons = 0
atom_nr_save = []

# remove coordinates that are the same between proteins and add them as in overlap list (since the obviouse overlap with identical coordinates) before sending it to comparison. This will reduse nr of camparisons a lot. 



   
# Find overlaps in remaining non identical atoms, as soon as 1 atom is overlapping , STOP, add to overlap list and move on to next atom instead. This will reduce comparison quantity


comparisons = 0

atom_index = []

for i in range (0,len(P2_atoms)):
    for j in range (0,len(P1_atoms)):
        dst = distance.euclidean(P1_atoms[j], P2_atoms[i])
#            distancelist.append((dst))
#            print(dst)
        comparisons += 1
        if dst <= 4:
            atom_index.append(i+1)
            break   


# get -1 on indexes...             
            
                    



print("\n List of Atom Numbers of protein2 which overlaps with atleast 1 atom in Protein1 : ", atom_index)

print("Number of comparisons : ",comparisons)

print("Number of clashing atoms: ",len(atom_index))