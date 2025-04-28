def match_pattern(texte,pattern):
    resultat = []
    for i in range(len(texte)):
        if texte[i] in pattern:
            if pattern[0] == texte[i]:
                trouve = True
                for j in range(1, len(pattern)):
                    if trouve == True:    
                        if i+j < len(texte) and pattern[j] == texte[i+j]:
                            trouve = True
                        else :
                            trouve = False
                if trouve:
                    resultat.append(i)
    print(resultat)

match_pattern("JFJDFKFGHMJHHKJKJHGAABAIHIHGKTYTLJGLJFKUYHGJGAABA", "AABA")
