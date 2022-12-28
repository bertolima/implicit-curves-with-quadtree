from cRetangulo import Retangulo
from cVetor import Vetor
import pyglet

class quadTree:
    def __init__(self, retangulo, profundidade_max, funcao, width, profundidade=0):

        self.funcao = funcao
        self.profundidade = profundidade
        self.retangulo = retangulo
        self.profundidade_max = profundidade_max
        self.shapeList = []
        self.width = width
        

        self.dividido = False       

        self.norteEsq = None
        self.norteDir = None
        self.sulDir = None
        self.sulEsq = None

        self.plotTree(self)

    def divisao(self, quadtree):

        codX, codY = quadtree.retangulo.codX, quadtree.retangulo.codY
        altura, largura = quadtree.retangulo.altura/2, quadtree.retangulo.largura/2

        quadtree.norteEsq = quadTree(Retangulo(codX-largura/2, codY+altura/2, altura, quadtree.width), quadtree.profundidade_max, quadtree.funcao, quadtree.width, quadtree.profundidade+1)
        quadtree.norteDir = quadTree(Retangulo(codX+largura/2, codY+altura/2, altura, quadtree.width), quadtree.profundidade_max, quadtree.funcao, quadtree.width,quadtree.profundidade+1)
        quadtree.sulDir = quadTree(Retangulo(codX+largura/2, codY-altura/2, altura, quadtree.width), quadtree.profundidade_max, quadtree.funcao, quadtree.width,quadtree.profundidade+1)
        quadtree.sulEsq= quadTree(Retangulo(codX-largura/2, codY-altura/2, altura, quadtree.width), quadtree.profundidade_max, quadtree.funcao, quadtree.width,quadtree.profundidade+1)

        quadtree.dividido = True #


    def plotTree(self, quadtree):

        if quadtree.profundidade == quadtree.profundidade_max:
            return
        if quadtree.retangulo.contemPonto(self.funcao):
            quadtree.divisao(quadtree)

        if quadtree.dividido:

            if quadtree.norteEsq.retangulo.contemPonto(self.funcao):
                quadtree.plotTree(quadtree.norteEsq)
            if quadtree.norteDir.retangulo.contemPonto(self.funcao):
                quadtree.plotTree(quadtree.norteDir)
            if quadtree.sulDir.retangulo.contemPonto(self.funcao):
                quadtree.plotTree(quadtree.sulDir)
            if quadtree.sulEsq.retangulo.contemPonto(self.funcao):
                quadtree.plotTree(quadtree.sulEsq)

    def showFull(self, quadtree, batch):

        if quadtree.norteEsq == None and quadtree.norteDir == None and quadtree.sulDir == None and quadtree.sulEsq == None:
            return

        self.shapeList.append(quadtree.retangulo.getRet(batch))

        if self.dividido:
            self.shapeList.append(quadtree.norteEsq.retangulo.getRet(batch))
            self.shapeList.append(quadtree.norteDir.retangulo.getRet(batch))
            self.shapeList.append(quadtree.sulDir.retangulo.getRet(batch))
            self.shapeList.append(quadtree.sulEsq.retangulo.getRet(batch))

            quadtree.showFull(quadtree.norteEsq, batch)
            quadtree.showFull(quadtree.norteDir, batch)
            quadtree.showFull(quadtree.sulDir, batch)
            quadtree.showFull(quadtree.sulEsq, batch)



    # def showCurve(self, quadtree):

    #     if quadtree.profundidade == quadtree.profundidade_max:
    #         self.shapeList.append(quadtree.retangulo.getRet())
    #         return

    #     if quadtree.retangulo.contemPonto(self.funcao):
    #         quadtree.divisao(quadtree)

    #     if quadtree.dividido:

    #         if quadtree.norteEsq.retangulo.contemPonto(self.funcao):
    #             quadtree.showCurve(quadtree.norteEsq)
    #         if quadtree.norteDir.retangulo.contemPonto(self.funcao):
    #             quadtree.showCurve(quadtree.norteDir)
    #         if quadtree.sulDir.retangulo.contemPonto(self.funcao):
    #             quadtree.showCurve(quadtree.sulDir)
    #         if quadtree.sulEsq.retangulo.contemPonto(self.funcao):
    #             quadtree.showCurve(quadtree.sulEsq)

    # def showHalf(self, quadtree):

    #     if quadtree.profundidade == quadtree.profundidade_max:
    #         quadtree.retangulo.getType(self.funcao)
    #         self.shapeList.append(quadtree.retangulo.getRet())
    #         return
    #     if quadtree.retangulo.contemPonto(self.funcao):
    #         self.shapeList.append(quadtree.retangulo.getRet())
    #         quadtree.divisao(quadtree)

    #     if quadtree.dividido:

    #         if quadtree.norteEsq.retangulo.contemPonto(self.funcao):
    #             quadtree.showHalf(quadtree.norteEsq)
    #         else:
    #             quadtree.norteEsq.retangulo.getType(self.funcao)
    #             self.shapeList.append(quadtree.norteEsq.retangulo.getRet())

    #         if quadtree.norteDir.retangulo.contemPonto(self.funcao):
    #             quadtree.showHalf(quadtree.norteDir)
    #         else:
    #             quadtree.norteDir.retangulo.getType(self.funcao)
    #             self.shapeList.append(quadtree.norteDir.retangulo.getRet())

    #         if quadtree.sulDir.retangulo.contemPonto(self.funcao):
    #             quadtree.showHalf(quadtree.sulDir)
    #         else:
    #             quadtree.sulDir.retangulo.getType(self.funcao)
    #             self.shapeList.append(quadtree.sulDir.retangulo.getRet())

    #         if quadtree.sulEsq.retangulo.contemPonto(self.funcao):
    #             quadtree.showHalf(quadtree.sulEsq)
    #         else:
    #             quadtree.sulEsq.retangulo.getType(self.funcao)
    #             self.shapeList.append(quadtree.sulEsq.retangulo.getRet())
