tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
        ("marzo", ("elettrico", 380)),
        ("marzo", ("gas", 100)),
        ("aprile", ("elettrico", 200)),
        ("aprile", ("gas", 220)),
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo", ("elettrico", 290)),
        ("marzo", ("gas", 130)),
        ("aprile", ("elettrico", 180)),
        ("aprile", ("gas", 150)),
    ]),
    ("Padova", [
        ("gennaio", ("elettrico", 260)),
        ("gennaio", ("gas", 180)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 140)),
        ("marzo", ("elettrico", 300)),
        ("marzo", ("gas", 180)),
        ("aprile", ("elettrico", 150)),
        ("aprile", ("gas", 250)),
    ])
)
scelta=input("inserisci il nome della citta' desiderata: ")


while (scelta not in tupla_consumi_energetici):
    print("Errore")
    scelta=input("inserisci il nome della citta' desiderata: ")


    

while(risorsa!="gas" or risorsa!="elettrico"):
    risorsa=input("inserisci il nome della risorsa desiderata(gas o elettrico): ")

def analizza_consumi_energetici(scelta, risorsa):
    media_risorsa=0
    max_risorsa=0
    mese_max_risorsa=''
    conta=0
    for city,mesi in tupla_consumi_energetici:
        if city==scelta:
            for mese, (sauce,consumo) in mesi:
                if sauce==risorsa:
                    media_risorsa+=consumo
                    conta+=1
                    if consumo>max_risorsa:
                        max_risorsa=consumo
                        mese_max_risorsa=mese
    media_risorsa=media_risorsa/conta
    return (media_risorsa, (max_risorsa, mese_max_risorsa))
consumi=analizza_consumi_energetici(scelta, risorsa)
media=consumi[0]
max_ris=consumi[1][0]
mese_max=consumi[1][1]

print(f"media risorsa: {media}")
print(f"consumo max: {max_ris} ")
print(f"mese consumo max: {mese_max} ")


