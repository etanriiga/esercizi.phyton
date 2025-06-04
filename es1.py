voti={'italiano':(7,6),'storia':(5,7),'tpsi':(6,8)}
def leggiChiave():
    materia=str(input("inserisci il nome della materia: "))
    if (materia in voti):
        print("errore, materia già presente ")
        return
    return materia
def leggiScritto():
    while True:
        votoScritto=int(input("inserisci il voto scritto della materia: "))
        if (votoScritto>0 and votoScritto<=10):
            return votoScritto
        print("valore inserito errato, reinserisici")
        
def leggiOrale():
    while True:
        votoOrale=int(input("inserisci il voto orale della materia: "))
        if (votoOrale>0 and votoOrale<=10):
            return votoOrale
        print("valore inserito errato, reinserisici")

def aggiungivoto():
    while True:
        chiave=leggiChiave()
        if (chiave==""):
            break
        votoScr=leggiScritto()
        votoOr=leggiOrale()


        voti[chiave]=(votoScr,votoOr)
        while True:
            scelta=int(input("vuoi inserire altre materie? 1 'Si' 2 'No': "))
            if (scelta==1 or scelta==2):
                break
            else:
                print("valore inserito errato")
        if (scelta==2):
            break
aggiungivoto()
def leggiMedScr():
    votiSc=0
    sommaScr=0
    for chiave in voti.keys():
        votoSc, votoOr= voti[chiave]
        votiSc+=1
        sommaScr+=votoSc
    return sommaScr/votiSc

        
def leggiMedOr():
    votiO=0
    sommaO=0
    for chiave in voti.keys():
        votoSc, votoOr= voti[chiave]

        votiO+=1
        sommaO+=votoOr
    return sommaO/votiO
def leggiMedTot():
    votiTot=0
    sommaTot=0
    for chiave in voti.keys():
        votoSc, votoOr= voti[chiave]
        votiTot+=2
        sommaTot+=votoOr+votoSc
    return sommaTot/votiTot

def medie():
    
    mediaScr=leggiMedScr()
    mediaOr=leggiMedOr()
    mediaTot=leggiMedTot()
    medie=(mediaScr,mediaOr,mediaTot)
    return medie
medie()
print(medie())