#Arnaud Moulis
import matplotlib.pyplot as plt
from scipy.spatial import distance
import numpy as np


#Task 3

datalist  = []
with open('1CDH.pdb') as pdbfile:
    for line in pdbfile:
        if line[:4] == 'ATOM' and line[13:15] == "CA":
            
            # Split the line
            splitted_line = [line[:4], line[9:11], line[13:15], line[17:20], line[21], line[21:22], line[30:38], line[38:46], line[46:54]]
#            print (splitted_line)
            datalist.append(splitted_line)
            # To format again the pdb file with the fields extracted
#            print ("%-6s%5s %4s %3s %s%4s    %8s%8s%8s\n"%tuple(splitted_line))


Xcord = []
Ycord = []
Zcord = []


for i in range(0, len(datalist)):
    Zcord.append(float(datalist[i][-1])) 
    Ycord.append(float(datalist[i][-2]))
    Xcord.append(float(datalist[i][-3]))

pair_list = list(zip(Xcord,Ycord,Zcord))


ok_pairs= []

X = []
Y = []

for i in range (0,len(pair_list)):
    for j in range (0,len(pair_list)):
        dst = distance.euclidean(pair_list[i], pair_list[j])
#            distancelist.append((dst))
#            print(dst)
        if dst <= 5:
            X.append(i)
            Y.append(j)
            ok_pairs.append([i,j])
            
plt.figure()
plt.scatter(X, Y, color = "G")
plt.show()


ok_pairs_standard = ok_pairs
ok_pairs = np.array(ok_pairs)




# This is to see what K should be equal to. the Elbow in the graph is the K number. (when a drastic change of values between 1 point to another occurs.) 
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(ok_pairs)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(ok_pairs)

# Visualising the clusters
plt.scatter(ok_pairs[y_kmeans == 0, 0], ok_pairs[y_kmeans == 0, 1], s = 30, c = 'red', label = 'Domain cluster 1')
plt.scatter(ok_pairs[y_kmeans == 1, 0], ok_pairs[y_kmeans == 1, 1], s = 30, c = 'blue', label = 'Domain cluster 2')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 100, c = 'yellow', label = 'Centroids')
plt.title('Clusters of sequence')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()


test = [list(a) for a in zip(y_kmeans, ok_pairs_standard)]
#list(zip(y_kmeans, ok_pairs_standard))

domain1 = []
domain2 = []

for i in range(0, len(test)):
    if test[i][0] == 0:
        domain1.append(test[i][1])
    else:
        domain2.append(test[i][1])
        
n1 = len(domain1)
n2 = len(domain2)
        
print("The", n1," indexes of each CA-Atom of domain1 (RED) are \n\n ", domain1, "\n\n\nThe", n2," indexes of each CA-Atom of domain2 (Blue) are \n\n", domain2)
        