tupla_partite = (
    ("GiocatoreA", "GiocatoreB", 3, 2),
    ("GiocatoreC", "GiocatoreD", 2, 3),
    ("GiocatoreB", "GiocatoreC", 3, 0),
    ("GiocatoreA", "GiocatoreD", 3, 1),
    ("GiocatoreB", "GiocatoreD", 2, 3),
)
def media_set_partita(tupla_partite):
    media=0
    for giocatore1, giocatore2, set1, set2 in tupla_partite:
        media=media+ set1+ set2
    return media/len(tupla_partite)
def media_set_giocatore(tupla_partite, giocatore): 
    media=0
    conta=0
    for giocatore1, giocatore2, set1, set2 in tupla_partite:
        if giocatore1==giocatore:
            media=media+ set1
            conta+=1
        elif giocatore2==giocatore:
            media=media+ set2
            conta+=1
    return media/conta
def match_piu_combattuto(tupla_partite):
    match=[]
    max=0
    for giocatore1, giocatore2, set1, set2 in tupla_partite:
        if set1+ set2>max:
            max=set1+ set2
            match=["prima partita:",giocatore1, giocatore2]
        elif set1+ set2==max:
            match.append(["altra partita: ",giocatore1, giocatore2])
    return tuple(match)
def match_meno_combattuto(tupla_partite):
    match=[]
    min=100
    for giocatore1, giocatore2, set1, set2 in tupla_partite:
        if set1+ set2<min:
            min=set1+ set2
            match=["prima partita:",giocatore1, giocatore2]
        elif set1+ set2==min:
            match.append(["altra partita: ",giocatore1, giocatore2])
    return tuple(match)
def percentuale_vittorie_giocatore(tupla_partite, giocatore):
    giocate=0
    vinte=0
    perc=0
    for giocatore1, giocatore2, set1, set2 in tupla_partite:
        if giocatore1==giocatore:
            if set1>set2:
                vinte+=1
                giocate+=1
            else:
                giocate+=1
        elif giocatore2==giocatore:
            if set2>set1:
                vinte+=1
                giocate+=1
            else:
                giocate+=1
    perc=(vinte/giocate)*100
    return perc
def controllo_nome():
    controllo_while=True
    while controllo_while:
        nome=input("inserisci il nome del giocatore: ")
        for n1, n2, *punti in tupla_partite:
            if nome==n1 or nome==n2:
                controllo_while=False
            else:
                print("Errore! riporova")
            
    return nome

controllo_while=True
while controllo_while:
    print("1-media set partite")
    print("2-media set di un giocatore")
    print("3-match piu' combattuto")
    print("4-match meno combattuto")
    print("5-percentuale vittorie giocatore")
    print("0-Fine")
    opzione=int(input("scegli un'opzione: "))
    print(opzione)
    if opzione==1:
        print("media set partite: ", media_set_partita(tupla_partite))
    elif(opzione==2):
        giocatore=controllo_nome()
        print("media set di un giocatore: ", media_set_giocatore(tupla_partite, giocatore))
    elif(opzione==3):
        print(match_piu_combattuto(tupla_partite))
    elif(opzione==4):
        print(match_meno_combattuto(tupla_partite))
    elif(opzione==5):
        giocatore=controllo_nome()
        print("percentuale vittorie giocatore ",giocatore,": ",percentuale_vittorie_giocatore(tupla_partite, giocatore),"%")
    elif(opzione==0):
        controllo_while=False

