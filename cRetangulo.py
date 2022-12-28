from pyglet import shapes

class Retangulo:
    def __init__(self, codX, codY, tamanho, width):
        #atributos bases de um retangulo: altura, largura, as coordenadas de onde serão posicionados e o batch é necessário para posterior utilização do pyglet de forma mais otimizada
        #o type é também uma variavel de controle relacionada a parte visual, pode ser definido como "inCurve" ou "outCurve", que diz se o retangulo em questao está pra dentro ou pra fora
        #da curva
        self.altura = tamanho
        self.largura = tamanho
        self.codX = codX
        self.codY = codY
        self.type = None
        self.width = width/2 #utilizado para converter as coordenadas pixel p cartesianas
        self.ratio = 8/width #fator de conversão de coordenadas pixel para as cartesianas

        #variaveis necessarias para ter os as coordenadas dos 4 pontos extremos do retangulo em questao
        self.esq = codX-self.largura/2
        self.dir = codX+self.largura/2
        self.baixo = codY-self.altura/2
        self.cima = codY+self.altura/2
        
    def getRet(self, batch):
        ponto = shapes.BorderedRectangle(self.codX, self.codY, self.altura, self.largura,border=1, color=(0, 0, 0), border_color=(255,255,255), batch=batch)
        ponto.anchor_position = self.altura/2, self.altura/2 
        return ponto

    def getType(self, function):
        #esse metodo julga qual o type do retangulo em questao, note que caso esse metodo seja chamado, é impossivel que o retangulo seja type=None
        cimaEsq =  function(self.ratio*(self.esq-self.width), self.ratio*(self.cima-self.width))
        cimaDir =  function(self.ratio*(self.dir-self.width), self.ratio*(self.cima-self.width))
        baixoEsq = function(self.ratio*(self.esq-self.width), self.ratio*(self.baixo-self.width))
        baixoDir = function(self.ratio*(self.dir-self.width), self.ratio*(self.baixo-self.width))

        if cimaEsq > 0 and cimaDir > 0 and baixoEsq > 0 and baixoDir > 0:
            self.type = "inCurve"
            return
        elif cimaEsq < 0 and cimaDir < 0 and baixoEsq < 0 and baixoDir < 0:
            self.type = "outCurve"
        self.type = "outCurve"

    def contemPonto(self, function):
        #esse metodo julga se a curva passa pelo retangulo em questao, as coordenadas X e Y dos 4 pontos do retangulo sao submetidas a equação implicita e, caso haja
        #igualdade nos valores de pontos opostos ou de pontos vizinhos, o metodo retorna True, caso contrario, o sinal do resultado dos pontos do retangulo aplicado 
        #a equação nos dira se ela pertece ou nao ao retangulo, caso todos pontos tenham sinal iguais, a curva não passa, portanto retorna False
        #Casso essa condição nao seja cumprida, retorna imediatamente True
        cimaEsq =  function(self.ratio*(self.esq-self.width), self.ratio*(self.cima-self.width))
        cimaDir =  function(self.ratio*(self.dir-self.width), self.ratio*(self.cima-self.width))
        baixoEsq = function(self.ratio*(self.esq-self.width), self.ratio*(self.baixo-self.width))
        baixoDir = function(self.ratio*(self.dir-self.width), self.ratio*(self.baixo-self.width))

        if cimaEsq == baixoDir and cimaDir == baixoEsq:
            return True
        if cimaEsq == cimaDir and  baixoEsq == baixoDir:
            return True
        if cimaEsq > 0 and cimaDir > 0 and baixoEsq > 0 and baixoDir > 0:
            self.type = "inCurve"
            return False
        if cimaEsq < 0 and cimaDir < 0 and baixoEsq < 0 and baixoDir < 0:
            self.type = "outCurve"
            return False
        
        return True
