def pendu():
    import random
    choix = ["lapin", "ocean", "dent", "alpha"]
    mot = random.choice(choix)
    vies = 7
    lettres_trouvees = ""
    affichage = ""
    for l in mot:
        affichage = affichage + "_"
        
    while vies > 0 :
        print("Mot à deviner : ", affichage)
        proposition = input("proposez une lettre : ")

        if proposition in mot:
            lettres_trouvees = lettres_trouvees + proposition
            print ("Bonne réponse")
            affichage = ""
            for x in mot:
                if x in lettres_trouvees:
                    affichage += x + " "
                else:
                    affichage += "_ "
        
        else:
            vies -=1
            print ("Mauvaise réponse, tu perds une vie. Il te reste", vies, "vies")
            if vies==0:
                print(" ==========Y= ")
            if vies<=1:
                print(" ||/       |  ")
            if vies<=2:
                print(" ||        0  ")
            if vies<=3:
                print(" ||       /|\ ")
            if vies<=4:
                print(" ||       /|  ")
            if vies<=5:                    
                print("/||           ")
            if vies<=6:
                print("==============\n")


        if "_" not in affichage:
            print(">>> Gagné! <<<")
            break

    print("\n    * Fin de la partie *    ")
          
    

pendu()
    