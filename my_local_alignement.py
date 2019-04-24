import numpy as np



match = 2
mismatch = -1
gap_penalty = 2


STOP = 0
UP = 1
LEFT = 2
DIAG = 3

X = "PAWHEAE"
Y = "HDAGAWGHEQ"

def LocalAlignment(X, Y):
        #Initialize scoring and backtracking matrices
    s = np.zeros((len(X)+1,len(Y)+1))
    backtrack = np.zeros((len(X)+1,len(Y)+1))
    
        
        #Fill in scoring and backtracking matrices
    score = 0
    tmp = 0
    curr_max = 0    
    for i in range(1,len(X)+1):
        for j in range(1,len(Y)+1):
                
            if  X[i-1] == Y[j-1] :
                score = s[i-1][j-1] + match
            else:
                score = s[i-1][j-1] + mismatch
            
            backtrack[i][j] = 3
                
            tmp = s[i-1][j] - gap_penalty
            if tmp > score:
                score = tmp
                backtrack[i][j] = UP
                
            tmp = s[i][j-1] - gap_penalty
            if tmp > score:
                score = tmp
                backtrack[i][j] = LEFT
                   
            if score < 0:
                s[i][j] = 0
                backtrack[i][j] = 0
            else:
                s[i][j] = score
                       
            if score >= curr_max:
                curr_max = score
#            print(curr_max)    
            
            
            
        #Find maximum cell from the biggest max value found in previous itteration
        maxpos_i = 0
        maxpos_j = 0
        for i in range(1,len(X)+1):
            for j in range(1,len(Y)+1):
                if s[i][j] == curr_max:
                    #save i and j position of max value in matrix
                    maxpos_i = i
                    maxpos_j = j
#                    print(s[i][j])
#                    print(curr_max)
#                    print("position ",maxpos_i, maxpos_j)
                    break        
 
                
    print(s)
    print("\n",backtrack)            
    
        
        #Backtracking and output
    i = maxpos_i
    j = maxpos_j
    V = ''
    W = ''
    x = ''
    EQ_count = 0
        
    while backtrack[i][j] != 0:
            
        if i == 0:
            V += '-'
            x += ' '
            W += Y[j-1]
            j = j-1
                
                
                
        elif j == 0:
            V += X[i-1]
            x += ' '
            W += '-'
            i = i-1
                
            
        elif backtrack[i][j] == 1:
            V += X[i-1]
            x += ' '
            W += '-'        
            i = i-1
                
            
        elif backtrack[i][j] == 2:
            V += '-'
            x += ' '
            W += Y[j-1]
            j = j-1
                
                
        elif backtrack[i][j] == 3:
            V += X[i-1]
            x += '|'
            W += Y[j-1]
            i = i-1
            j = j-1
            EQ_count += 1
            
        
    return int(s[len(X)][len(Y)]), V[::-1], W[::-1], x[::-1], EQ_count

score, V, W, x, EQ_count  = LocalAlignment(X, Y)

#ex.2

identical_resedues = EQ_count

total_resedues_short = min(len(V),len(W))

PrId = (identical_resedues / total_resedues_short)*100


print ('\nScore: ' + str(score), "\n")

print (V)
print (x)
print (W, "\n")


print ("The percent identity is calculated by simply dividing the number of identical resedues between two sequences with the total number of resedues in the shortest sequence and multiplying it by 100 \n" )
print ("The percent identity is :", PrId)


#ex.3

count = 0 

for i in range(0,min(len(X),len(Y))):
    if X[i] != Y[i]:
        count += 1
    else:
        count = count


print ("\nHamming distance is ",count, "\n\nconsidering equal length of strings. If not equal, the overhang-bit is discarded")     
#
# 
#ex.4


            