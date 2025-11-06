## Calculatrice 


operande_gauche = int(input("Vous aller rentrer une opération mathématique, commencer par donner l'opérande de gauche Exemple : 4 "))
operateur = input("Puis l'opérateur Exemple : sois +, -, /, * ")
operande_droite = int (input("Rentrer l'opérande de droite "))
if operateur == "+":
    result = (operande_gauche + operande_droite)
    print (result)
elif operateur == "-":
    result = (operande_gauche - operande_droite)
    print (result)

elif operateur == "/":
    result = (operande_gauche / operande_droite)
    print (result) 

elif operateur == "*" :
    result = (operande_gauche * operande_droite)
    print (result) 

else : 
    print ("Erreur dans durant la saisie de l'opération")