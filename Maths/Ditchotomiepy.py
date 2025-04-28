from math import *
import matplotlib.pyplot as plt 
import numpy as np 

def dichotomie(x,a,b,seuil):
    continuer = True
    opp = 0
    while continuer:
        m = (a+b)/2
        opp += 1
        test = m**2-x
        opp += 1

        if test > 0 :
            b = m

        elif test < 0 :
            a = m

        else:
            return (m,opp)
        continuer = b-a > seuil

    return(m,opp)

dy = np.empty(shape=0)
x= np.linspace(1, 14 ,14)
for i in range (1,15):
    dy = np.append(dy, dichotomie(10,3,4,10**(-i))[1])
print(dy)
fig, ax = plt.subplots()
ax.plot(x, dy)
plt.show()


