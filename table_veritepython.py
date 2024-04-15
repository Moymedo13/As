#Fonction logiques

# #Fonction ET 
def et(a,b):
    #Supposons que a ET b est Vrai
    resultat = True
    #Test si a ET b est Faux
    if(a == False or b == False):
        # a ET b est Faux
        resultat = False
    return resultat

def ou(a,b):
    #Supposons que a OU b est Faux
    resultat = False
    #Test si a OU b est Vrai
    if(a == True or b == True):
        # a OU b est Vrai
        resultat = True
    return resultat

def negation(a):
    #Supposons que la negation de a est Vrai
    resultat = True
    #Test de la veracite de a
    if(a == True):
        resultat = False
    return resultat

def valeur(a):
    result = 1
    if(a == False):
        result = 0
    return result

#forme canonique
def premier_forme_canonique(a,b,c):
    return a*b*c + a*negation(b)*c + a*negation(b)*negation(c)

def second_forme_canonique(a,b,c):
    return (a + b + c) * (negation(a) + negation(b) + c)*(a + negation(b) + negation(c))*(negation(a) + negation(b) + negation(c)) 

#table de verite  
def table_verite(a,b,c):
    print(f"a | b | c | a ET b | a OU b | non a | non b | 1F | 2F")
    print("-------------------------------------------------------")
    for i in range(len(a))  :
        print(f"{valeur(a[i])} | {valeur(b[i])} | {valeur(c[i])} |    {valeur(et(a[i],b[i]))}   |    {valeur(ou(a[i],b[i]))}   |   {valeur(negation(a[i]))}   |   {valeur(negation(b[i]))}   |  {premier_forme_canonique(a[i],b[i],c[i])} |  {second_forme_canonique(a[i],b[i],c[i])}")
    pass

a = [True,True,True,True,False,False,False,False]
b = [True,True,False,False,True,True,False,False]
c = [True,False,True,False,True,False,True,False]

table_verite(a,b,c)