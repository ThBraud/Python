from math import sin, pi, cos
def calculpi(seuil):
    n=3
    U = 3*sin((2*pi)/3)
    continuer = True
    while (continuer):
        n +=1 
        Unext = n*sin((2*pi)/n)
        continuer = (abs(Unext- U) > seuil)
        U = Unext
        print(Unext)
    return(pi, n)

calculpi(0.1)


from math import *
seuil = 0.01
n = 3
u = 3*sin(2*pi/3)
continuer = True
while continuer :
    n += 1
    v = n*sin(2*pi/n)
    continuer = abs(u-v)>seuil
    u = v

print(n)
print(pi)
print(u/2)