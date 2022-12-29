from cQuadTree import quadTree
from cRetangulo import Retangulo
import pyglet

class window:

    def __init__(self, depth, funcoes, width, height, legenda="Visualizar Curva Implícita"):
        self.funcoes = funcoes      #recebe todas as equações implicitas
        self.depth = depth          #recebe a pronfudidade maxima da árvore
        self.nowDepth = depth         

        self.batchG = None
        self.batchQ = None
        self.batchR = None

        #todas essas variaveis começam com None       
        self.ret = None                         
        self.arvore = None         
        
        #variaveis de controle
        self.drawFull = False
        self.drawCurve = False
        self.drawHalf = False

        self.funcVal = -1

        self.lockG = False
        self.lockQ = False
        self.lockR = False

        def pressG():
            if self.drawFull:
                self.drawFull = False
            elif self.lockG == False:
                self.batchG = pyglet.graphics.Batch()
                self.arvore.showFull(self.arvore, self.batchG)
                self.drawFull = True
                self.lockG = True
            elif self.lockG == True:
                self.drawFull = True
            self.drawCurve = False
            self.drawHalf = False
        def pressQ():
            if self.drawCurve:
                self.drawCurve = False
            elif self.lockQ == False:
                self.batchQ = pyglet.graphics.Batch()
                self.arvore.showCurve(self.arvore, self.batchQ)
                self.drawCurve = True
                self.lockQ = True
            elif self.lockQ == True:
                self.drawCurve = True
            self.drawFull = False
            self.drawHalf = False
        def pressR():
            if self.drawHalf:
                self.drawHalf = False
            elif self.lockR == False:
                self.batchR = pyglet.graphics.Batch()
                self.arvore.showHalf(self.arvore, self.batchR)
                self.drawHalf = True
                self.lockR = True
            elif self.lockR == True:
                self.drawHalf = True
            self.drawFull = False
            self.drawCurve = False

        def on_key_press(key, modifiers): 

            #A aplicação só começa a funcionar efetivamente ao acionar a tecla P
            if key == pyglet.window.key.P:

                self.funcVal += 1
                #se estivermos na ultima função da lista de funções, o "contador" retorna pra função 0
                if self.funcVal == len(funcoes):
                    self.funcVal = 0

                self.drawFull = False
                self.drawCurve = False
                self.drawHalf = False
                self.lockG = False
                self.lockQ = False
                self.lockR = False

                #criamos as TADs necessárias e atribuimos as variaveis
                self.ret = Retangulo(width/2, width/2, height, width)   
                self.arvore = quadTree(self.ret, self.depth, self.funcoes[self.funcVal], width)
                self.arvore.plotTree(self.arvore)
       
             
            if key == pyglet.window.key.G:
                pressG()

            if key == pyglet.window.key.Q:
                pressQ()

            if key == pyglet.window.key.R:
                pressR()

            if key == pyglet.window.key.X:
                self.nowDepth -= 1
                self.arvore.delDepth(self.arvore, self.nowDepth)
                if self.drawFull:
                    self.drawFull = False
                    self.lockG = False
                    pressG()
                elif self.drawCurve:
                    self.drawCurve = False
                    self.lockQ = False
                    pressQ()
                elif self.drawHalf:
                    self.drawHalf = False
                    self.lockR = False
                    pressR()


        def on_draw():
            window.clear()
            if self.drawFull:
                self.batchG.draw()
            elif self.drawCurve:
                self.batchQ.draw()
            elif self.drawHalf:
                self.batchR.draw()


        window = pyglet.window.Window(width, height, legenda)
        window.push_handlers(on_draw)
        window.push_handlers(on_key_press)

        pyglet.app.run()
