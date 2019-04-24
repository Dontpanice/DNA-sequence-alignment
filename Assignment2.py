import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from scipy.spatial import distance

Datafile = pd.read_csv("data.csv", header = None)

Atomlist = Datafile.iloc[:,2]
CA_lits = []

for i in range(0,len(Datafile)):
    if Atomlist[i] == 'CA':
        CA_lits.append(Datafile[i])
    else:
        pass
    
    



Xcord = Datafile.iloc[:,6]
Ycord = Datafile.iloc[:,7]
Zcord = Datafile.iloc[:,8]

plt.figure()
plt.scatter(Xcord,Ycord)
plt.show()


plt.figure()
plt.scatter(Zcord,Ycord)
plt.show()


pair_list = list(zip(Xcord,Ycord,Zcord))
#Z_Y_pair = list(zip(Zcord,Ycord))

count = 0

for i in range(0,len(Datafile)-1):
    dX = Xcord[i] - Xcord[i+1]
    dY = Ycord[i] - Ycord[i+1]
    dZ = Zcord[i] - Zcord[i+1]
    
    dst = distance.euclidean(pair_list[i], pair_list[i+1] )
    
    if dst < 7:
#        print("CA_index (i,j) are close to each other" ,(i,i+1))
        count += 1
        
        
