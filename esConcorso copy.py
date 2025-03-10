
concorso={}
concorso["Rossi Mario"]=[("antipasti", (8,7,9), "junior chef"),("primi", (7,8,8), "junior chef"),("secondi", (9,9,8), "junior chef"),("dessert", (8,8,9), "junior chef")]
concorso["Bianchi Luigi "]=[("antipasti", (7,7,8), "senior chef"),("primi", (8,9,7), "senior chef"),("secondi", (7,8,7), "senior chef"),("dessert", (9,8,8), "senior chef")]
concorso["Verdi Giulia "]=[("antipasti", (9,9,8), "junior chef"),("primi", (8,7,9), "junior chef"),("secondi", (8,8,8), "junior chef"),("dessert", (7,8,9), "junior chef")]
concorso["Rigamonti Etan"]=[("antipasti", (7,8,7), "junior chef"),("primi", (8,9,7), "junior chef"),("secondi", (8,7,9), "junior chef"),("dessert", (8,7,8), "junior chef")]
def aggiungi_cat():

    import random
    n1=random.randint(1,10)
    n2=random.randint(1,10)
    n3=random.randint(1,10)
    for nome in concorso.keys():
        if concorso[nome][0][2]=="junior chef":
            concorso[nome].append(("piatto unico",(n1,n2,n3),"junior chef"))
        else:
            concorso[nome].append(("piatto unico",(n1,n2,n3),"senior chef"))
    pass
def stampa_dati(nome):
    if nome in concorso.keys():
        print("Categoria di chef= ", concorso[nome][0][2])
        print("Cognome e nome= ", nome)

        for nome, dati in concorso.items():    
            for piatto, punt, cat in dati:
                print(piatto+": ", punt)
                print("creatività= ", punt[0])
                print("gusto= ", punt[1])
                print("presentazione= ", punt[2])
                print("categoria= ", cat)
        pass
    else:
        print("non esiste questo chef")

def stampa_piatto(piatto):
    conta=0
    for nome, dati in concorso.items():
        
        for plate, punt, cat in dati:
            if piatto==plate:
                print(nome+": " )
                print("piatto: ",piatto)
                print("creatività= ", punt[0])
                print("gusto= ", punt[1])
                print("presentazione= ", punt[2])
                conta=1
                print("\n")
    if conta==0:
         print("non esiste questo piatto")


    
    pass         
                
    
    
def tot_punt(concorso, catPiatto, catChef):
    max=[]
    tot=0
    
    for nome, dati in concorso.items():
        for piatto, punt, cat in dati:
            if piatto==catPiatto and cat==catChef:
                tot1=punt[0]+ punt[1]+punt[2]
                if tot1>tot:
                    max.clear()
                    max.append(nome)
                    max.append(tot1)
                    tot=tot1
                elif tot1==tot:
                    max.append(nome)
                    max.append(tot1)
    if len(max)==0:
        print("non esiste questa categoria")
    else:
        return max
   
        

def media_punt(concorso, catPiatto, catChef):
    media=0
    conta=0
    
    for nome, dati in concorso.items():
        for piatto, punt, cat in dati:
            if piatto==catPiatto and cat==catChef:
                media=punt[0]+ punt[1]+punt[2]
                conta+=1
    if media==0:
        print("non esiste questa categoria")
    else:
        media=media/conta
        return media
def inserisci_dati_nuovo_chef():
    nome=input("inserisci il nome dello chef ")
    cogn=input("inserisci il cognome ")
    nominativo=(nome, cogn)
    risultati=[]
    piatto=input("inserisci il nome di un piatto: ")
    numeri=input("inserisci i punteggi di creatività, gusto e presentazione separati da uno spazio: ")
    numeri=numeri.split()
    category=input("inserisci la categoria del piatto: ")
    risultati.append((piatto))
    risultati.append((numeri))
    risultati.append((category))
    return nominativo, risultati



def inserisci_nuovo_chef(conscorso,nominativo,risultati):
    if len(nominativo)==2 and isinstance(nominativo, tuple):
        if len(risultati)==3 and isinstance(risultati, list):
            for res in risultati:
                
                res=risultati[1]
                if len(res)==3 and isinstance(res, tuple):
                    if  isinstance(res[0], int)  or isinstance(res[1], int)  or isinstance(res[2], int) :
                        n1=res[1][0]
                        n2=res[1][1]
                        n3=res[1][2]
                        categoria=res[2]
                        conscorso[nominativo]=[("antipasti", (n1,n2,n3),categoria),("primi",(n1,n2,n3), categoria),("secondi", (n1,n2,n3), categoria),("dessert", (n1,n2,n3), categoria), ("piatto unico", (n1,n2,n3), categoria)]
                        return conscorso
                    else:
                        print("errore4") 
                else:
                    print("errore3") 
        else:
            print("errore2") 
    else:
        print("errore1") 
aggiungi_cat()

nome=input("inserisci il nome di uno chef: ")
print(stampa_dati(nome))
piatto=input("inserisci il nome di un piatto: ")
print(stampa_piatto(piatto))

catPiatto=input("inserisci la categoria del piatto: ")
catChef=input("inserisci la categoria dello chef: ")
print(tot_punt(concorso, catPiatto, catChef))

catPiatto2=input("inserisci la categoria del piatto: ")
catChef2=input("inserisci la categoria dello chef: ")
print(media_punt(concorso, catPiatto2, catChef2))

nominativo, risultati= inserisci_dati_nuovo_chef()
conscorso2=inserisci_nuovo_chef(concorso,nominativo,risultati)
concorso.update(conscorso2)
print(concorso)