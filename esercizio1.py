pioggia=(("Milano", [("Gennaio", 100),("febbraio", 120),("marzo","N/D" ),("aprile", 120),
        ("maggio","N/D" ),("giugno", 200),("luglio", "N/D"),("agosto", 200),
        ("settembre", "N/D"),("ottobre", 100),("novembre ", 200),("dicembre", 120)]),
           
        ("Brescia", [("Gennaio", 100),("febbraio", 350),("marzo", 200),("aprile", 100),
        ("maggio", 200),("giugno", 120),("luglio", 200),("agosto", "N/D"),
        ("settembre", 100),("ottobre","N/D" ),("novembre ", 120),("dicembre", 120)]),
           
        ("Lecco", [("Gennaio","N/D" ),("febbraio", 120),("marzo", 100),("aprile","N/D" ),
        ("maggio","N/D" ),("giugno", 100),("luglio", 120),("agosto", 120),
        ("settembre", 120),("ottobre", 200),("novembre ","N/D" ),("dicembre", 100)]))

scelta=print(input("di quale capoluogo vuoi vedere i mm di pioggia? Milano,Bresciao o Lecco?"))

def analizza (scelta, pioggia):
    somma=0
    conta=0
    max=0
    min=999999999999999
    for citta, precip in pioggia:
        if scelta==citta:
            for mese,millim in precip:
                print(mese,": ",millim,"mm")
                if millim=="N/D":
                    print("valore non disponibile il mese ",mese)
                    
                else:
                    somma+=millim
                    conta+=1
                if millim<min:
                    min=millim
                    month=mese
                if millim>max:
                    max=millim
                    wulan=mese
    somma=somma/conta
    valori=(somma,(max,wulan),(min,month))
    return valori(somma,(max,wulan),(min,month))
valori=analizza(scelta,pioggia)
print("la media per la citta' ", scelta, " e': ",valori(somma))
                
    

