class Macchina():
    def __init__(self, targa, marca, modello, anno):
        self.targa=targa
        self.marca=marca
        self.modello=modello
        self.anno=anno
        # Inizializza gli attributi della macchina

    def __str__(self):
        return f"targa= {self.targa}\nmarca= {self.marca}\nmodello= {self.modello}\nanno= {self.anno}\n\n"
        # Restituisce una descrizione leggibile della macchina

class Garage():
    
    def __init__(self):
        self.lista=[]
        # Inizializza la lista delle macchine

    def aggiungi_macchina(self, macchina):
        for macc in self.lista:
            if macc== macchina:
                print("macchina già presente")
                return
        self.lista.append(macchina)
        print("macchina aggiunta")
        return  # Aggiunge una macchina alla lista

    def rimuovi_macchina(self, targa1):
        for macc in self.lista:
            if macc.targa==targa1:
                self.lista.remove(macc)
                print("macchina rimossa")
                return
        print("macchina non presente")
        return  # Rimuove una macchina in base alla targa

    def elenco_macchine(self):
        print("di seguito tutte le macchine\n")
        if (self.lista.__len__==0):
            print("nessuna macchina presente nella lista")
        else:
            for macc in self.lista:
                print(macc)
        # Mostra tutte le macchine nel garage

    def cerca_macchina(self, targa):
        for macc in self.lista:
            if macc.targa== targa:
                print("macchina trovata ed è la seguente: ")
                print(macc)
                return
        print("macchina non trovata")
        return
        # Cerca e restituisce le informazioni di una macchina tramite la targa
garage=Garage()
macchina1=Macchina("AA333BBB", "Seat","Cupra",2020)
macchina2=Macchina("AA444BBB", "fiat","punto",1999)
macchina3=Macchina("AA111BBB", "lamborghini","urus",2007)
ans=1
while (ans!=0):
    ans=int(input("sicrivi cosa vuoi fare: 1) aggiungi machina, 2) rimuovi macchina, 3) elenco macchine, 4) cerca macchina, 0) esci"))
    if ans==0:
        pass
    if ans==1:
        garage.aggiungi_macchina(macchina1)
    if ans==2:
        garage.rimuovi_macchina(macchina1.targa)
    if ans==3:
        garage.elenco_macchine()
    if ans==4:
        garage.cerca_macchina(macchina1.targa)






