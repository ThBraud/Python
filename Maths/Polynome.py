def calcul_polynome(P,X):
    nb_coeffs = len(P)
    resultat = 0
    for i in range(nb_coeffs):
        resultat += P[i]*(X**i)

    return resultat


P = [-4,0,1,-4,0,15]

print(calcul_polynome(P, 12))


