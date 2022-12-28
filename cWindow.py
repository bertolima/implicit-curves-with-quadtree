from cQuadTree import quadTree
from cRetangulo import Retangulo
import pyglet

class window:

    def __init__(self, depth, funcoes, width, height, legenda="Visualizar Curva Implícita"):
        self.funcoes = funcoes      #recebe todas as equações implicitas
        self.depth = depth          #recebe a pronfudidade maxima da árvore

        self.batchG = None

        #todas essas variaveis começam com None       
        self.ret = None                         
        self.arvore = None         
        
        #variaveis de controle
        self.drawFull = False
        self.drawCurve = False
        self.drawHalf = False
        self.numero = -1

        def on_key_press(key, modifiers): 

            #A aplicação só começa a funcionar efetivamente ao acionar a tecla P
            if key == pyglet.window.key.P:

                self.numero += 1
                #se estivermos na ultima função da lista de funções, o "contador" retorna pra função 0
                if self.numero == len(funcoes):
                    self.numero = 0

                self.drawFull = False
                self.drawCurve = False
                self.drawHalf = False

                #criamos as TADs necessárias e atribuimos as variaveis
                self.ret = Retangulo(width/2, width/2, height, width)   
                self.arvore = quadTree(self.ret, self.depth, self.funcoes[self.numero], width)
       
             
            if key == pyglet.window.key.G:
                self.batchG = pyglet.graphics.Batch()
                self.arvore.showFull(self.arvore, self.batchG)
                self.drawFull = True

            if key == pyglet.window.key.Q:
                self.batchG = pyglet.graphics.Batch()
                self.arvore.showCurve(self.arvore, self.batchG)
                self.drawCurve = True

            if key == pyglet.window.key.R:
                self.batchG = pyglet.graphics.Batch()
                self.arvore.showHalf(self.arvore, self.batchG)
                self.drawHalf = True



        def on_draw():
            window.clear()
            if self.drawFull:
                self.batchG.draw()
            elif self.drawCurve:
                self.batchG.draw()
            elif self.drawHalf:
                self.batchG.draw()


        window = pyglet.window.Window(width, height, legenda)
        window.push_handlers(on_draw)
        window.push_handlers(on_key_press)

        pyglet.app.run()
