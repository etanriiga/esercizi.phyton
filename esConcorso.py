
concorso={}
concorso["Rossi Mario"]=[("antipasti", (8,7,9), "junior chef"),("primi", (7,8,8), "junior chef"),("secondi", (9,9,8), "junior chef"),("dessert", (8,8,9), "junior chef")]
concorso["Bianchi Luigi "]=[("antipasti", (7,7,8), "senior chef"),("primi", (8,9,7), "senior chef"),("secondi", (7,8,7), "senior chef"),("dessert", (9,8,8), "senior chef")]
concorso["Verdi Giulia "]=[("antipasti", (9,9,8), "junior chef"),("primi", (8,7,9), "junior chef"),("secondi", (8,8,8), "junior chef"),("dessert", (7,8,9), "junior chef")]
concorso["Rigamonti Etan"]=[("antipasti", (7,8,7), "junior chef"),("primi", (8,9,7), "junior chef"),("secondi", (8,7,9), "junior chef"),("dessert", (8,7,8), "junior chef")]
def aggiungi_cat():
    for nome in concorso.keys():
        import random
        n1=random.randint(1,10)
        n2=random.randint(1,10)
        n3=random.randint(1,10)

        if concorso[nome][0][2]=="junior chef":
            concorso[nome].append(("piatto unico",(n1,n2,n3),"junior chef"))
        elif concorso[nome][0][2]=="senior chef":
            concorso[nome].append(("piatto unico",(n1,n2,n3),"senior chef"))
        else:
            pass
def stampa_dati(nome):
    if nome in concorso.keys():
        print("Categoria di chef= ", concorso[nome][0][2])
        print("Cognome e nome= ", nome)

        for nome, dati in concorso:
            for piatto, punt, cat in dati:
                print(piatto+": ", punt)
                print("creatività= ", punt[1][0])
                print("gusto= ", punt[1][1])
                print("presentazione= ", punt[1][2])
                print("categoria= ", cat)
    else:
        print("non esiste questo chef")

def stampa_piatto(piatto):
    if piatto in concorso:
        for nome, dati in concorso:
            for piatto, punt, cat in dati:
                print(nome+": " )
                print("piatto: ",piatto)
                print("creatività= ", punt[1][0])
                print("gusto= ", punt[1][1])
                print("presentazione= ", punt[1][2],"\n")
    else:
        print("non esiste questo piatto")         
def tot_punt(concorso, catPiatto, catChef):
    max=[]
    tot=0
    if catPiatto in concorso:
        if catChef in concorso:
            for nome, dati in concorso:
                for piatto, punt, cat in dati:
                    if piatto==catPiatto and cat==catChef:
                      tot1=sum(punt[1][0], punt[1][1],punt[1][2])
                    if tot1>tot:
                        max.clear
                        max.append(nome, tot1)
                        tot=tot1
                    elif tot1==tot:
                        max.append(nome, tot1)
            return max
        else:
            print("errore categoria non presente")
    else:
        print("piatto non presente") 

def media_punt(concorso, catPiatto, catChef):
    media=0
    conta=0
    if catPiatto in concorso:
        if catChef in concorso:
            for nome, dati in concorso:
                for piatto, punt, cat in dati:
                    if piatto==catPiatto and cat==catChef:
                        media=sum(punt[1][0], punt[1][1],punt[1][2])
                        conta+=1
            media=media/conta
            return media
        else:
            print("errore categoria non presente")
    else:
        print("piatto non presente") 
def inserisci_dati_nuovo_chef():
    nome=input("inserisci il nome dello chef ")
    cogn=input("inserisci il cognome ")
    nominativo=(nome, cogn)
    for nome, dati in concorso:
        for piatto, numeri, category  in concorso:
            risultati.append((piatto, numeri, category))
    return nominativo, risultati



def inserisci_nuovo_chef(concorso,nominativo,risultati):
    if len(nominativo)==2 and isinstance(nominativo, tuple):
        if len(risultati)==5 and isinstance(risultati, list):
            for res in risultati:
                if len(res)==3 and isinstance(risultati[1], tuple):
                    if  res[1][0]==0 or res[1][0]==1 or res[1][0]==2 or res[1][0]==3 or res[1][0]==4 or res[1][0]==5 or res[1][0]==6 or res[1][0]==7 or res[1][0]==8 or res[1][0]==9 or res[1][0]==10 and res[1][1]==0 or res[1][1]==1 or res[1][1]==2 or res[1][1]==3 or res[1][1]==4 or res[1][1]==5 or res[1][1]==6 or res[1][1]==7 or res[1][1]==8 or res[1][1]==9 or res[1][1]==10 and res[1][2]==0 or res[1][2]==1 or res[1][2]==2 or res[1][2]==3 or res[1][2]==4 or res[1][2]==5 or res[1][2]==6 or res[1][2]==7 or res[1][2]==8 or res[1][2]==9 or res[1][2]==10:
                        n1=res[1][0]
                        n2=res[1][1]
                        n3=res[1][2]
                        categoria=res[2]
                        concorso[nominativo]=[("antipasti", (n1,n2,n3),categoria),("primi",(n1,n2,n3), categoria),("secondi", (n1,n2,n3), categoria),("dessert", (n1,n2,n3), categoria), ("piatto unico", (n1,n2,n3), categoria)]
                        return concorso
                    else:
                        print("errore") 
                else:
                    print("errore") 
        else:
            print("errore") 
    else:
        print("errore") 
aggiungi_cat
nome=input("inserisci il nome di uno chef")
print(stampa_dati(nome))
piatto=input("inserisci il nome di un piatto")
print(stampa_piatto(piatto))

catPiatto=input("inserisci la categoria del piatto")
catChef=input("inserisci la categoria dello chef")
print(tot_punt(concorso, catPiatto, catChef))

catPiatto2=input("inserisci la categoria del piatto")
catChef2=input("inserisci la categoria dello chef")
print(media_punt(concorso, catPiatto2, catChef2))

nominativo, risultati= inserisci_dati_nuovo_chef()
conscorso2=inserisci_nuovo_chef(concorso,nominativo,risultati)
concorso.update(conscorso2)
print(concorso)