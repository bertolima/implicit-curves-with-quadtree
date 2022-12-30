from cQuadTree import quadTree
from cRetangulo import Retangulo
import pyglet

class window:

    def __init__(self, depth, funcoes, width, height, legenda="Visualizar Curva Implícita"):
        self.funcoes = funcoes      #receive implicit functions
        self.depth = depth          #receive max tree depth     

        self.batchG = None
        self.batchQ = None
        self.batchR = None
      
        self.ret = None                         
        self.arvore = None         
        
        self.drawFull = False
        self.drawCurve = False
        self.drawHalf = False
        self.lockG = False
        self.lockQ = False
        self.lockR = False
        self.lockGen = False
        self.lockChange = False

        self.funcVal = -1

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

            if key == pyglet.window.key.P:

                self.funcVal += 1
                if self.funcVal == len(funcoes):
                    self.funcVal = 0

                self.drawFull = False
                self.drawCurve = False
                self.drawHalf = False
                self.lockG = False
                self.lockQ = False
                self.lockR = False

                self.ret = Retangulo(width/2, width/2, height, width)   
                self.arvore = quadTree(self.ret, self.depth, self.funcoes[self.funcVal], width)
                self.arvore.plotTree(self.arvore)
                self.lockGen = True
                self.lockChange = False
       
            if key == pyglet.window.key.W:
                if self.lockGen:
                    pressG()
                    self.lockChange = True

            if key == pyglet.window.key.Q:
                if self.lockGen:
                    pressQ()
                    self.lockChange = True

            if key == pyglet.window.key.E:
                if self.lockGen:
                    pressR()
                    self.lockChange = True

            if key == pyglet.window.key.Z:
                if self.lockChange:
                    if self.depth > 0:
                        self.depth -= 1
                        self.arvore.subDepth(self.arvore, self.depth)
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

            if key == pyglet.window.key.X:
                if self.lockChange:
                    if self.depth < 10:
                        self.depth += 1
                        self.arvore.addDepth(self.arvore, self.depth)
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
