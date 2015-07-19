__author__ = 'chirag'

import math

def FindLightestCoin(D):
    # This function finds the lightest coin in the shortest number of weighings
    # Basically, what you want to do is divide number of coins in groups of three

    n = len(D)
    if(n%3 != 0):
        nDivison = (n/3)+1
    else:
        nDivison = (n/3)

    if n==3:
        if D[0]>D[1]:
            return D[1]
        elif D[0]<D[1]:
            return D[1]
        else:
            return D[2]
    elif n == 2:
        if D[0]>D[1]:
            return D[1]
        else:
            return D[0]
    else:
        if float(sum(D[0:nDivison]))>float(sum(D[nDivison:(2*nDivison)])):
            return FindLightestCoin(D[nDivison:(2*nDivison)])
        elif sum(D[0:nDivison])<sum(D[nDivison:(2*nDivison)]):
            return FindLightestCoin(D[0:nDivison])
        else:
            return FindLightestCoin(D[(2*nDivison):len(D)])


coins = [0.5,0.5,0.5,0.5, 0.3,0.5,0.5,0.5, 0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
#coins =[0.5,0.5,0.4,0.5,0.5]

print FindLightestCoin(coins)



# Completed