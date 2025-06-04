voti={'Mario':[(7,8),(6,8),(9,10)],'Giacomo':[(7,7),(6,5),(9,8)],
      'Gionata':[(7,8),(6,8),(9,10)],'Francesco':[(7,7),(6,5),(9,8)],
      'Salmo':[(7,8),(6,8),(9,10)],'Antonio':[(7,7),(6,5),(9,8)],
      'Elena':[(7,8),(6,8),(9,10)],'Sayf':[(7,7),(6,5),(9,8)]
      }

def medie(nome):

    sommaTot=0
    sommaScr=0
    sommaOr=0
    mediaTot=0
    mediaSc=0
    mediaO=0
    for studenti in voti.keys():
        (mateS,mateO), (fisicaS,fisicaO), (chimicaS,chimicaO)=voti[nome]
 
        sommaTot+=mateS+mateO+fisicaS+fisicaO+chimicaS+chimicaO
        sommaScr+=mateS+fisicaS+chimicaS
        sommaOr+=mateO+fisicaO+chimicaO

        
    mediaTot=sommaTot/6
    mediaSc=sommaScr/3
    mediaO=sommaOr/3
    votiStud=(mediaSc,mediaO,mediaTot)
    return votiStud
while True:
    nome=str(input("inserisci il nome dello studente di cui vuoi visualizare la media scritta, orale e totale"))
    if (nome not in voti):
        print("errore nell'inserimento")
    print(medie(nome))
    while True:
        scelta=int(input("vuoi sapere altre medie? 1 'Si' 2 'No': "))
        if (scelta==1 or scelta==2):
              break
        else:
            print("valore inserito errato")
    if (scelta==2):
        break