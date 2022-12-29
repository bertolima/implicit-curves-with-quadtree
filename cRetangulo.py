from pyglet import shapes

class Retangulo:
    def __init__(self, codX, codY, tamanho, width):
        self.altura = tamanho
        self.largura = tamanho
        self.codX = codX
        self.codY = codY
        self.type = None
        self.width = width/2 
        self.ratio = 8/width 

        self.esq = codX-self.largura/2
        self.dir = codX+self.largura/2
        self.baixo = codY-self.altura/2
        self.cima = codY+self.altura/2
        self.type = None
        
    def getRet(self, batch):
        ponto = shapes.BorderedRectangle(self.codX, self.codY, self.altura, self.largura,border=1, color=(0, 0, 0), border_color=(255,255,255), batch=batch)
        ponto.anchor_position = self.altura/2, self.altura/2
        return ponto

    def colorRet(self, batch):
        if self.type == "inCurve":
            ponto = shapes.Rectangle(self.codX, self.codY, self.altura, self.largura, color=(0, 0, 255), batch=batch)
            ponto.anchor_position = self.altura/2, self.altura/2
            return ponto
        elif self.type == "outCurve":
            ponto = shapes.Rectangle(self.codX, self.codY, self.altura, self.largura, color=(255, 0, 0), batch=batch)
            ponto.anchor_position = self.altura/2, self.altura/2
            return ponto
      

    def getType(self, retangulo, function):
        cimaEsq =  function(retangulo.ratio*(retangulo.esq-retangulo.width), retangulo.ratio*(retangulo.cima-retangulo.width))
        cimaDir =  function(retangulo.ratio*(retangulo.dir-retangulo.width), retangulo.ratio*(retangulo.cima-retangulo.width))
        baixoEsq = function(retangulo.ratio*(retangulo.esq-retangulo.width), retangulo.ratio*(retangulo.baixo-retangulo.width))
        baixoDir = function(retangulo.ratio*(retangulo.dir-retangulo.width), retangulo.ratio*(retangulo.baixo-retangulo.width))

        if cimaEsq > 0 and cimaDir > 0 and baixoEsq > 0 and baixoDir > 0:
            retangulo.type = "inCurve"
            return
        elif cimaEsq < 0 and cimaDir < 0 and baixoEsq < 0 and baixoDir < 0:
            retangulo.type = "outCurve"
            return
        retangulo.type = "outCurve"

    def contemPonto(self, function):
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