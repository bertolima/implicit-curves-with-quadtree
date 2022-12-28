from cQuadTree import quadTree
from cRetangulo import Retangulo
import pyglet

class window:

    def __init__(self, depth, funcoes, width, height, legenda="Visualizar Curva Implícita"):
        self.funcoes = funcoes      #recebe todas as equações implicitas
        self.depth = depth          #recebe a pronfudidade maxima da árvore

        #todas essas variaveis começam com None
        self.batchG = None          #armazena os desenhos da TAD completa
        self.batchQ = None          #armazena os desenhos somente da curva implicita
        self.batchR = None          #armazena os desenhos da analise espacial da curva
        self.retG = None            #armazena os retangulos que representarao a TAD
        self.retQ = None            #armazena os retangulos que representarao a curva
        self.retR = None            #armazena os retangulos que representarao a analise espacial da curva(vermelho ou azul)
        self.arvoreG = None         #arvore que vai representar a TAD toda
        self.arvoreQ = None         #arvore que vai representar a curva
        self.arvoreR = None         #arvore que vai representar a analise espacial

        #variaveis de controle
        self.drawFull = False
        self.drawCurve = False
        self.drawHalf = False
        self.ver1 = False
        self.ver2 = False
        self.ver3 = False
        self.ver4 = False
        self.ver5 = False
        self.ver6 = False
        self.ver7 = False
        self.ver8 = False
        self.numero = -1

        def on_key_press(key, modifiers): 
            #A aplicação só começa a funcionar efetivamente ao acionar a tecla P
            if key == pyglet.window.key.P:
                self.ver8 = False       #essa variavel bloqueia as ações das teclas Z e X
                self.numero += 1
                self.ver4 = True        #essa variavel bloqueia as ações das teclas G, R e Q

                #se estivermos na ultima função da lista de funções, o "contador" retorna pra função 0
                if self.numero == self.funcoes.getTam():
                    self.numero = 0

                #sempre que pressionamos P, é necessário que "zeremos" os estados das outras variaveis relacionados ao desenho das figuras
                self.ver1 = False
                self.ver2 = False
                self.ver3 = False
                self.drawFull = False
                self.drawCurve = False
                self.drawHalf = False

                #criamos o Batch respectivo a cada representação de imagem
                self.batchG = pyglet.graphics.Batch()
                self.batchQ = pyglet.graphics.Batch()
                self.batchR = pyglet.graphics.Batch()

                #criamos as TADs necessárias e atribuimos as variaveis
                self.retG = Retangulo(width/2, width/2, height, width, batch=self.batchG)   
                self.arvoreG = quadTree(self.retG, self.depth, self.funcoes.getItem(self.numero), width)
                self.retQ = Retangulo(width/2, width/2, height, width, batch=self.batchQ)   
                self.arvoreQ = quadTree(self.retQ, self.depth, self.funcoes.getItem(self.numero), width)  
                self.retR = Retangulo(width/2, width/2, height, width, batch=self.batchR)   
                self.arvoreR = quadTree(self.retR, self.depth, self.funcoes.getItem(self.numero), width)  

            # G é responsável pela exibição da TAD em todos os seus níveis                
            if key == pyglet.window.key.G:
                #ver4 só é True caso P tenha sido pressionado antes, logo, se P não tiver sido pressionado, essa tecla não vai fazer nada.
                if self.ver4 is False:
                    return
                #caso todas verificações sejam False, o código executa o método que vai realizar a plotagem da curva em seu respecto tipo de exibição(nesse caso Full)
                if self.drawFull is False:
                    #ver5 é uma verificação referente ao nível de refinamento, caso seja True, significa que o refinamento da curva foi alterado em outro local do código#
                    #portanto é necessario que a construção dos objetos seja feita novamente com os novos parametros de refinamento.
                    if self.ver5 is False:
                        if self.ver1 is False:
                            self.arvoreG.showFull(self.arvoreG)
                            self.ver1 = True
                    else:
                        self.ver1 = True

                        self.retG = Retangulo(width/2, width/2, height, width, batch=self.batchG)   
                        self.arvoreG = quadTree(self.retG, self.depth, self.funcoes.getItem(self.numero), width)
                        self.arvoreG.showFull(self.arvoreG)

                        self.ver5 = False
                        
                    self.drawHalf = False
                    self.drawCurve = False
                    self.drawFull = True     
                #caso drawFull seja true, e apertamos a tecla novamente, drawFull se tornará False, fazendo com que a respectiva imagem desapareça da tela
                else:
                    self.drawFull = False
                self.ver8 = True

            #As teclas Q e R funcionam da mesma maneira da G, a unica diferença é o tipo de imagem plotada.

            if key == pyglet.window.key.Q:
                if self.ver4 is False:
                    return
                if self.drawCurve is False:
                    if self.ver6 is False:
                        if self.ver2 is False:
                            self.arvoreQ.showCurve(self.arvoreQ)
                            self.ver2 =  True
                    else:
                        self.ver2 =  True

                        self.retQ = Retangulo(width/2, width/2, height, width, batch=self.batchQ)   
                        self.arvoreQ = quadTree(self.retQ, self.depth, self.funcoes.getItem(self.numero), width) 
                        self.arvoreQ.showCurve(self.arvoreQ)

                        self.ver6 = False

                    self.drawFull = False
                    self.drawHalf = False
                    self.drawCurve = True
                else:
                    self.drawCurve = False
                self.ver8 = True

            if key == pyglet.window.key.R:
                if self.ver4 is False:
                    return
                if self.drawHalf is False:
                    if self.ver7 is False:
                        if self.ver3 is False:
                            self.arvoreR.showHalf(self.arvoreR)
                            self.ver3 = True
                    else:
                        self.ver3 = True

                        self.retR = Retangulo(width/2, width/2, height, width, batch=self.batchR)   
                        self.arvoreR = quadTree(self.retR, self.depth, self.funcoes.getItem(self.numero), width)
                        self.arvoreR.showHalf(self.arvoreR)
                        
                        self.ver7 = False

                    self.drawFull = False
                    self.drawCurve = False
                    self.drawHalf = True
                else:
                    self.drawHalf = False
                self.ver8 = True
                    
            #Essa tecla é responsável por diminuir o nível de refinamento da exibição da curva
            if key == pyglet.window.key.Z:
                #ver8 sempre se torna False ao pressionar P, e se torna True ao pressionar G, Q ou R. Portanto, só é permitido trocar o refinamento de uma curva, após 
                #a plotagem de alguma imagem.
                #A mudança de refinamento pode ser vista em tempo real...
                if self.ver8 is False:
                    return
                #a pronfudidade minima da arvore é 0, portanto o nível 0 representa um quadrado do mesmo tamanho da janela aberta
                if self.depth > 0:
                    #é necessario criar novos Batch pra que, ao trocar o refinamento, seja possivel exibir isso na janela
                    self.batchG = pyglet.graphics.Batch()
                    self.batchQ = pyglet.graphics.Batch()
                    self.batchR = pyglet.graphics.Batch()
                    self.depth -= 1
                    #no caso de alguma das exibições ja estiver ativa, iremos criar uma nova TAD com os novos parametros de refinamento, e imediatamente, essa nova TAD será
                    #exibida na janela, desse modo a mudança de refinamento funciona.
                    if self.drawFull:
                        self.retG = Retangulo(width/2, width/2, height, width, batch=self.batchG)   
                        self.arvoreG = quadTree(self.retG, self.depth, self.funcoes.getItem(self.numero), width)
                        self.arvoreG.showFull(self.arvoreG)
                        self.ver6 = True
                        self.ver7 = True
                    elif self.drawCurve:
                        self.retQ = Retangulo(width/2, width/2, height, width, batch=self.batchQ)   
                        self.arvoreQ = quadTree(self.retQ, self.depth, self.funcoes.getItem(self.numero), width) 
                        self.arvoreQ.showCurve(self.arvoreQ)
                        self.ver5 = True
                        self.ver7 = True
                    elif self.drawHalf:
                        self.retR = Retangulo(width/2, width/2, height, width, batch=self.batchR)   
                        self.arvoreR = quadTree(self.retR, self.depth, self.funcoes.getItem(self.numero), width)
                        self.arvoreR.showHalf(self.arvoreR)
                        self.ver5 = True
                        self.ver6 = True
            #funciona da mesma maneira da tecla Z, a diferença que ao inves de decrementar a profundidade, aqui nós incrementamos, o limite de refinamento é 10,
            #no README está explicado o porque disso.
            if key == pyglet.window.key.X:
                if self.ver8 is False:
                    return
                if self.depth > -1 and self.depth < 10:
                    self.batchG = pyglet.graphics.Batch()
                    self.batchQ = pyglet.graphics.Batch()
                    self.batchR = pyglet.graphics.Batch()
                    self.depth += 1
                    if self.drawFull:
                        self.retG = Retangulo(width/2, width/2, height, width, batch=self.batchG)   
                        self.arvoreG = quadTree(self.retG, self.depth, self.funcoes.getItem(self.numero), width)
                        self.arvoreG.showFull(self.arvoreG)
                        self.ver6 = True
                        self.ver7 = True
                        
                    elif self.drawCurve:
                        self.retQ = Retangulo(width/2, width/2, height, width, batch=self.batchQ)   
                        self.arvoreQ = quadTree(self.retQ, self.depth, self.funcoes.getItem(self.numero), width) 
                        self.arvoreQ.showCurve(self.arvoreQ)
                        self.ver5 = True
                        self.ver7 = True
                    elif self.drawHalf:
                        self.retR = Retangulo(width/2, width/2, height, width, batch=self.batchR)   
                        self.arvoreR = quadTree(self.retR, self.depth, self.funcoes.getItem(self.numero), width)
                        self.arvoreR.showHalf(self.arvoreR)
                        self.ver5 = True
                        self.ver6 = True

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
