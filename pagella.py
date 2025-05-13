class Pagella:
    def __init__(self,lista):
        self.lista=lista
    def __repr__(self,num):
        return f"VOTO: {self.lista[num]}"
    def media(self):
        somma=0
        cont=0
        for i in self.lista:
            somma=somma+self.lista[i]
            cont+=1
        if somma!=0:
            return somma/cont
        else: 
            print("impossibile eseguire la media")
    def __getitem__(self, indice):
        return self.lista[indice]
    def __eq__(self,p2):
        if len(self.lista)!=len(p2):
            print("erore")
            return
        controllo=False
        if self.lista==p2:
            controllo=True
            return controllo
        else:
            return controllo
    def __sub__(self,p2):
        if len(self.lista)!=len(p2):
            print("erore")
            return
        for i in p2:
            if(self.lista[i]==p2[i]):
                self.lista.remove(i)
                p2.remove(i)
    