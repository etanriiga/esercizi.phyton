tupla_partite = (
    ("Real Madrid", "Milan", 1, 3),
    ("Milan", "inter", 25, 0),
    ("Verona", "sassuolo", 2, 4),
    ("Palermo", "Salernitana", 0, 3),
    ("Al Nassr", "Inter miami", 0, 20),
    ("catania", "genoa", 2, 4),
    ("juve", "napoli", 0, 0)
)
squadra=input("scegli una squadra: ")

def media_gol_partite(tupla_partite):
    media=0
    conta=0
    for squadra1,squadra2,punti1,punti2 in tupla_partite:
        media+=punti1+punti2
        conta+=1
    media=media/conta
    return media
media_partite=media_gol_partite(tupla_partite)

def media_gol_squadra(tupla_partite, squadra):
    mediaSquadra=0
    conta=0
    for squadra1,squadra2,punti1,punti2 in tupla_partite:
        if squadra1==squadra:
            mediaSquadra+=punti1
            conta+=1
        elif squadra2==squadra:
            mediaSquadra+=punti2
            conta+=1
    mediaSquadra=mediaSquadra/conta
    return mediaSquadra
mediaSquad=media_gol_squadra(tupla_partite, squadra)
def partita_con_piu_gol(tupla_partite):
    massimo=0
    max=["",""]
    for squadra1,squadra2,punti1,punti2 in tupla_partite:
        if punti1+punti2>massimo:
            max=["",""]
            max.append=[squadra1,squadra2]
    return max[squadra1,squadra2]

piuGol=partita_con_piu_gol(tupla_partite)
squadra1=piuGol[0]
squadra2=piuGol[1]
def partita_con_meno_gol(tupla_partite):
    minimo=999999999
    min=["",""]
    for squadra1,squadra2,punti1,punti2 in tupla_partite:
        if punti1+punti2<minimo:
            min=["",""]
            min.append=[squadra1,squadra2]
    return min[squadra1,squadra2]
menoGol=partita_con_meno_gol(tupla_partite)
squadra3=menoGol[0]
squadra4=menoGol[1]
opzione=input("cosa vuoi fare? 1: media gol partite; 2: media gol di una squadra; 3: partita con piu gol; 4: partita con meno gol")
if (opzione==1):
    print("media partite: ",media_partite)
elif (opzione==2):
    print("media gol di una squadra: ",mediaSquad)
elif (opzione==3):
    print("la partita con piu' gol si è disputata tra ",squadra1," e ",squadra2)
elif (opzione==4):
    print("la partita con meno gol si è disputata tra ",squadra3," e ",squadra4)
else:
    print("opzione non disponibile")








