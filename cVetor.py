#Simples implementação de vetor pra não ter que usar o do python...

class Vetor:  
    def __init__(self, n):
        self.nObj = 0
        self.contador = 0
        
        if n < 1:
            self.vet = []
        else:
            self.vet = [0] * n
            self.nObj = n

    def inserir(self, item):
        self.vet[self.contador] = item
        self.contador += 1

    def getItem(self, posicao):
        return self.vet[posicao]

    def getTam(self):
        return self.nObj

