#Arnaud Moulis
import matplotlib.pyplot as plt
from scipy.spatial import distance


P1_data  = []
with open('1CDH.pdb') as pdbfile:
    for line in pdbfile:
        if line[:4] == 'ATOM' and line[13:15] == "CA":
            
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
        if line[:4] == 'ATOM' and line[13:15] == "CA":
            
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
        if dst < 4:
            atom_index.append(i)
            break   
            
            
                    

print("Number of comparisons : ",comparisons)

print("\n List of Atom Numbers of protein2 which overlaps with atleast 1 atom in Protein1 : ", atom_index)

          
#plt.figure()
#plt.scatter(X, Y, color = "G")
#plt.show()




























#
#ok_pairs= []
#
#X = []
#Y = []
#
#for i in range (0,len(pair_list)):
#    for j in range (0,len(pair_list)):
#        dst = distance.euclidean(pair_list[i], pair_list[j])
##            distancelist.append((dst))
##            print(dst)
#        if dst <= 5:
#            X.append(i)
#            Y.append(j)
#            ok_pairs.append([i,j])
#            
#plt.figure()
#plt.scatter(X, Y, color = "G")
#plt.show()
#
#      
#        
##c = 100
#           
#tracklist = []
#
#for c in range(0,len(pair_list)):
#    CountA = 0
#    CountB = 0
#    CountExt = 0
#    for i in range(0,len(ok_pairs)):
#        if ok_pairs[i][0] > c and ok_pairs[i][1] > c:
#            CountB += 1
#        elif ok_pairs[i][0] < c and ok_pairs[i][1] < c:
#            CountA += 1
#        else:
#            CountExt += 1
#        
#    splitvalue = (CountA/CountExt) * (CountB/CountExt)
#    tracklist.append(splitvalue)    
#
#
#intersectlist = [(max(tracklist)/2) for x in range(len(pair_list))]
#
#inter = (max(tracklist)/2)
#
#plt.figure()                    
#plt.plot(tracklist, color = "G")
#plt.plot(intersectlist, color = "B")
#plt.show
#
#
#maxval = max(tracklist)
#Index_max = tracklist.index(maxval)
#
#
#index_of_splits = []
#
#for x in range(0, len(pair_list)):
#    if tracklist[x] > inter:
#        index_of_splits.append(tracklist.index(tracklist[x]))
#
## Ncount is the count of domains found from peaks in plot
## it starts from 1 since code below only adds 1 if it finds another peak which fulfills the MDS criteria
#Ncount = 1
#
##MDS, Minimal Domain Size
#MDS = 40
#Where_split = []
#
#for t in range(0, len(index_of_splits)):
#    while t != len(index_of_splits)-1:
#        if ((index_of_splits[t+1] - index_of_splits[t]) > MDS):
#            Ncount += 1
#            Where_split.append(t)
#            
#        break
#    
## add latst index for where to split, since above code do not catch it. 
#tmp = len(index_of_splits) - Where_split[-1]
#Where_split.append(Where_split[-1] + (tmp/2))
#        
#        
## with given middle indexes of peak intervals, lookup what they correspond to in index_of_splits 
#Lookup = []
#temp = 0
#split_point_in_graph = []
#
#for i in range(0, len(Where_split)):
#    temp = int(Where_split[i])
#    split_point_in_graph.append(index_of_splits[temp])
#
#    
#print("\n Segment can be split at ", Ncount ," points at",split_point_in_graph, "\n Therefore ", Ncount +1," domains exists" )
#

        