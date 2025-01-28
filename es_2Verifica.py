corsi = (
    ("Milano", [
        ("gennaio", ("online", 50)),
        ("gennaio", ("in presenza", 30)),
        ("febbraio", ("online", 40)),
        ("febbraio", ("in presenza", 25)),
        ("marzo", ("online", 50)),
        ("marzo", ("in presenza", 30)),
        ("aprile", ("online", 40)),
        ("aprile", ("in presenza", 25)),
        ("maggio", ("online", 45)),
        ("maggio", ("in presenza", 20)),
        ("giugno", ("online", 35)),
        ("giugno", ("in presenza", 30)),
        
    ]),
    ("Bologna", [
        ("gennaio", ("online", 45)),
        ("gennaio", ("in presenza", 20)),
        ("febbraio", ("online", 35)),
        ("febbraio", ("in presenza", 30)),
        ("marzo", ("online", 45)),
        ("marzo", ("in presenza", 20)),
        ("aprile", ("online", 35)),
        ("aprile", ("in presenza", 30)),
        ("maggio", ("online", 45)),
        ("maggio", ("in presenza", 20)),
        ("giugno", ("online", 35)),
        ("giugno", ("in presenza", 30)),
        
    ]),
    ("Piacenza", [
        ("gennaio", ("online", 45)),
        ("gennaio", ("in presenza", 20)),
        ("febbraio", ("online", 35)),
        ("febbraio", ("in presenza", 30)),
        ("marzo", ("online", 45)),
        ("marzo", ("in presenza", 20)),
        ("aprile", ("online", 35)),
        ("aprile", ("in presenza", 30)),
        ("maggio", ("online", 45)),
        ("maggio", ("in presenza", 20)),
        ("giugno", ("online", 35)),
        ("giugno", ("in presenza", 30)),
        
    ]),
    ("Taranto", [
        ("gennaio", ("online", 45)),
        ("gennaio", ("in presenza", 20)),
        ("febbraio", ("online", 35)),
        ("febbraio", ("in presenza", 30)),
        ("marzo", ("online", 45)),
        ("marzo", ("in presenza", 20)),
        ("aprile", ("online", 35)),
        ("aprile", ("in presenza", 30)),
        ("maggio", ("online", 45)),
        ("maggio", ("in presenza", 20)),
        ("giugno", ("online", 35)),
        ("giugno", ("in presenza", 30)),
        
    ]),
    
)
def controllo_citta(corsi):
    controllo_while=True
    while controllo_while:
        city=input("inserisci il nome della citta': ")
        for citta,altro in corsi:
            if city==citta:
                controllo_while=False
            else:
                print("Errore! riporova")
    return city
def controllo_mod(corsi):
    controllo_while=True
    while controllo_while:
        mod=input("inserisci il nome della modalita': ")
        for citta, altro in corsi:
            for mese, dati in altro:
                modalita,presenze=dati
                if mod==modalita:
                    controllo_while=False
                else:
                    print("Errore! riporova")
    return mod
def analizza_partecipanti(corsi,city, mod):
    media_partecipanti=0
    max_partecipanti=0
    mese_max_partecipanti=[0]
    conta=0
    for citta, altro in corsi:
        if city==citta:
            for mese, dati in altro:
                modalita, presenze=dati
                if mod==modalita:
                    media_partecipanti+=presenze
                    conta+=1
                    if presenze>max_partecipanti:
                        max_partecipanti=presenze
                        mese_max_partecipanti=[mese]
                    elif presenze==max_partecipanti:
                        mese_max_partecipanti.append(mese)
    media_partecipanti=media_partecipanti/conta
    tuple(mese_max_partecipanti)
    return (media_partecipanti,(max_partecipanti, mese_max_partecipanti))
city=controllo_citta(corsi)
mod=controllo_mod(corsi)
print(analizza_partecipanti(corsi,city, mod))
    