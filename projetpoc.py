# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Atelier():
    "les attributs d'un automate sont le nom, les differents automates generes et l'alphabet associe"
    def __init__ (self,nom,Automate,Symbole):
        self.nom = nom
        self.Automate = []
        self.Symbole = []
    
    def __str__ (self):
        return "{} {} {}".format(self.nom, self.Automate, self.Symbole)
    
    def __repr__ (self):
        return"Atelier : {}".format(self)       
        
        
class Transition():
    "les attributs des transitions sont les etats et l'alphabet"
    def __init__(self,Eamont,Eaval,Symb):
        self.Eamont= Eamont
        self.Eaval=Eaval
        self.Etiquette=Symb
        Eamont.ajouterTS(self)
        
    def __str__(self):
        return "({}, {}, {})".format(self.Eamont, self.Eaval, self.Etiquette)
    
    def __repr__ (self):
        return "Transition : {}".format(self)
    

class Etat():
    "les attributs d'un etat sont le fait qu'il soit initial ou final"
    def __init__(self,nom,initial,final):
        self.nom = nom
        self.initial=initial
        self.final=final
        self.TS=[]
        self.TE=[]
        self.etatatteintpour={}
        self.etatsatteintpour={}
        self.indeterminisme=None
        
    def __str__(self):
        return "{}".format(self.nom)
    
    def __repr__(self):
        return "Etat : {}".format(self)
    
    def ajouterTS(self,T1):
        self.TS.append(T1)
        
    def ajouterTE(self,T2):
        self.TE(self,T2)


class Symbole():
    "l'attribut d'un symbole n'est que son nom"
    def __init__(self,nom):
        self.nom = nom
        
    def __str__(self):
        return "{}".format(self.nom)
    
    def __repr__(self):
        return "Symbole : {}".format(self)
    
    def __It__(self,other):
        return self.nom<other.nom
    
class Automate():
    "l'attribut d'un autonomate c'est son nom"
    def __init__(self,nom):
        self.nom=nom
        self.etats=[]
        self.evenements=[]
        self.transitions=[]
        self.etatnommé=dict()
        self.evenementnommé=dict()
        self.EI=[]
        self.EF=[]
        
    def __str__(self):
        return"{}".format(self.nom)
        
    def __repr__(self):
        return"Automate:{}".format(self)
        
    def affichagetextuelle(self):
        "affichage des symboles"
        print("Automate:",self.nom)
        if len(self.evenements)==1:
            print("-",len(self.evenements),"symbole existant :", str(self.evenements))
        else:
            print("-",len(self.evenements),"symboles existants :",str(self.evenements))
        
        "affichage des etats"
        if len(self.etats)==1:
            print("-",len(self.etats),"etat existant :",str(self.etats))
        else:
            print("-",len(self.etats),"etats existants :",str(self.etats))
        
        "affichage des transitions"
        if len(self.transitions)==1:
            print("-",len(self.transitions),"transition existante :", str(self.transitions))
        else:
            print("-",len(self.transitions),"transitions existantes :", str(self.transitions))
        
        "affichage des etats initiaux"
        N=[]
        for i in self.EI:
            if i not in N:
                N.append(i)
            if len(N)==0:
                print("il n'existe pas d'états initiaux")
            elif len(N)==1:
                print("- un etat initial existant:", str(N))
            else:
                print("-",len(N),"états initiaux existants:",str(N))
                
        "affichage des etats finaux"
        NN=[]
        for i in self.EF:
            if i not in NN:
                NN.append(i)
            if len(NN)==0:
                print("il n'existe pas d'états finaux")
            elif len(NN)==1:
                print("- un etat final existant:", str(NN))
            else:
                print("-",len(NN),"états finaux existants:",str(NN))            
                
    def ajouteretat(self,nom,estInitial,estFinal):
        if nom not in self.etatnommé.keys():
            nouveletat=Etat(nom,estInitial,estFinal)
        self.etats.append(nouveletat)
        if estInitial:
            self.EI.append(nouveletat)
        if estFinal:
            self.EF.append(nouveletat)
        self.etatnommé[nom]=nouveletat           
            
    def ajouterevenement(self,nom):
        if nom not in self.evenementnommé.keys():
            nouvelevenement=Symbole(nom)
            self.evenements.append(nouvelevenement)
            self.evenementnommé[nom]=nouvelevenement
        
        
    def ajoutertransition(self,nomEamont,nomEaval,nomSymbole):
        Symb=self.evenementnommé[nomSymbole]
        Eamont=self.etatnommé[nomEamont]
        Eaval=self.etatnommé[nomEaval]
        nouvelletransition=Transition(Eamont,Eaval,Symb)
        self.transitions.append(nouvelletransition)
            
            
###################################################################################################
Test4=('AF_p14_Det',['a','b'],[0,1,2],[0],[2],[(0,0,'a'),(0,0,'b'),(0,1,'a'),(1,2,'a'),(1,2,'b')])

nomAutomate, nomSymbole, nomsEtats, nomEI, nomEF, donneesTransitions=Test4
    
############Construction de l'automate#####################
a1=Automate(nomAutomate)
for nom in nomSymbole :
    a1.ajouterevenement(nom)
for nom in nomsEtats :
    estInitial= nom in nomEI
    estFinal= nom in nomEF
    a1.ajouteretat(nom, estInitial, estFinal)
for triplet in donneesTransitions :
    nomEamont, nomEaval, nomSymbole = triplet
    a1.ajoutertransition( nomEamont, nomEaval, nomSymbole)
    
a1.affichagetextuelle()


###########Deterministe ou non#######################
if len(nomEI) != 1:
    print("cet automate n'est pas deterministe")
else:
    deterministe = True
    for donne1 in donneesTransitions:
        i=0
        for donne2 in donneesTransitions:
            if donne1[0] == donne2[0]:
                if  donne1[2] == donne2[2]:
                    i =  i+1
        if i>1:
            deterministe = False
    if deterministe == False:
        print("cet automate n'est pas deterministe")
    else:
        print('cet automate est deterministe')
###########Standard ou non#########
Standard = True    
if len(nomEI) != 1:
    print("cet automate n'est pas standard")
    Standard = False
else:
    for donne in donneesTransitions:
        if donne[1] == nomEI[0]:
            Standard = False
    if Standard == True:
        print('cet automate est standard')
    else:
        print("cet automate n'est pas standard")
        
##############standariser l'automate###################

if Standard == False:
    print("maintenant on va standariser l'automate")
    nvDonne = []
    d = 'd'
    for i in nomEI:
        for donne in donneesTransitions:
            if donne[0] == i:
                nvEtat = (d,donne[1],donne[2])
                nvDonne.append(nvEtat)
    donneesTransitions = donneesTransitions + nvDonne
    nomEI=[]
    nomEI.append(d)
    print("voici votre automate standarisé:")
    print(donneesTransitions)
    print("voici votre nouveau etat initial:")
    print(nomEI)