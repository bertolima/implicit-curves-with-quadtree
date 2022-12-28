from cRetangulo import Retangulo
from cVetor import Vetor

class quadTree:
    def __init__(self, retangulo, profundidade_max, funcao, width, profundidade=0):
        #retangulo é um objeto da classe retangulo, profundidade_max pode ser interpretado como a quantidade maxima de divisoes que a Tree pode fazer
        #funcao se refere a equação implicita da curva que será gerada a partir da Tree
        self.funcao = funcao
        self.profundidade = profundidade
        self.retangulo = retangulo
        self.profundidade_max = profundidade_max
        self.shapeList = Vetor(100)     #aqui criamos um vetor com 100 posições pra podermos armazenar os "desenhos" dos retangulos no Batch do pyglet
        self.width = width              

        #verifica se a Tree já foi dividida ou nao
        self.dividido = False       

        #esses são os "filhos" da Tree
        self.norteEsq = None
        self.norteDir = None
        self.sulDir = None
        self.sulEsq = None

    def divisao(self, quadtree):
        #como vou realizar a divisao em varias Tree e não somente nessa, o parametro quadTree deve ser generalizado
        #preciso pegar as coordenadas e altura/largura da Tree(retangulo) em questao, pra poder definir corretamente a altura/largura e coordenadas de seus filhos.
        codX, codY = quadtree.retangulo.codX, quadtree.retangulo.codY
        altura, largura = quadtree.retangulo.altura/2, quadtree.retangulo.largura/2

        #note que o processo se dará de forma recursiva. Quando eu divido uma Tree, seus filhos também se tornam Tree, mas note que tem dimensoes e coordenadas diferentes
        #alem disso a profundidade atual tem que ser acrescida de +1, a funcao, profundidade_max e o batch do retangulo se mantem da Tree pai pras Tree filho
        quadtree.norteEsq = quadTree(Retangulo(codX-largura/2, codY+altura/2, altura, quadtree.width, batch=quadtree.retangulo.batch), quadtree.profundidade_max, quadtree.funcao, quadtree.width, quadtree.profundidade+1)
        quadtree.norteDir = quadTree(Retangulo(codX+largura/2, codY+altura/2, altura, quadtree.width, batch=quadtree.retangulo.batch), quadtree.profundidade_max, quadtree.funcao, quadtree.width,quadtree.profundidade+1)
        quadtree.sulDir = quadTree(Retangulo(codX+largura/2, codY-altura/2, altura, quadtree.width, batch=quadtree.retangulo.batch), quadtree.profundidade_max, quadtree.funcao, quadtree.width,quadtree.profundidade+1)
        quadtree.sulEsq= quadTree(Retangulo(codX-largura/2, codY-altura/2, altura, quadtree.width, batch=quadtree.retangulo.batch), quadtree.profundidade_max, quadtree.funcao, quadtree.width,quadtree.profundidade+1)

        #quando a tree for dividida uma vez, eu preciso sinalizar(vai ser importante mais pra frente)
        quadtree.dividido = True #


        #cada um dos metodos a seguir diz respeito a uma forma de representação da Tree, showFull() vai mostrar a estrutura inteira da Tree
        #showCurve vai mostrar exclusivamente a Tree em que os filhos dessa Tree são folhas, portanto sao iguais a None, em termos graficos, significa que a representação vai ser
        #apenas da curva implicita
        #showHalf vai representar a parte de fora e de dentro da curva(por isso a classe Retangulo pode ter retangulos vermelhos ou azuis.)

    def showFull(self, quadtree):
        #verifica se a arvore ja chegou na pronfudidade maxima, esse é o problema base da recursão
        if quadtree.profundidade == quadtree.profundidade_max:
            return
        #aqui vamos verificar se o retangulo(que representa a arvore) tem alguma parte da curva passando por si
        #caso tenha, vamos inserir na shapeList e isso vai ficar armazenado no Batch do pyglet, além disso vamos chamar o método da divisao
        #perceba que caso não tenha, esse método não vai fazer nada (isso significa que não vai haver mais divisões no retangulo, pois a curva nao passa nele)
        if quadtree.retangulo.contemPonto(self.funcao):
            self.shapeList.inserir(quadtree.retangulo.getRet())
            quadtree.divisao(quadtree)

        #caso a curva pertença a Tree(retangulo), o metodo da divisao vai ser chamado e teremos o self.divido = True
        #note que ele precisa ser generalizado, por isso nao usamos o self. 
        if quadtree.dividido:

            #vamos inserir todos os filhos no Batch para representação grafica
            self.shapeList.inserir(quadtree.norteEsq.retangulo.getRet())
            self.shapeList.inserir(quadtree.norteDir.retangulo.getRet())
            self.shapeList.inserir(quadtree.sulDir.retangulo.getRet())
            self.shapeList.inserir(quadtree.sulEsq.retangulo.getRet())

            #aqui é onde a recursão ocorre de fato
            #vamos verificar se a curva passa por algum dos filhos que já são Tree(retangulo), mas são menores que a Tree(retangulo) pai.
            #caso a curva passe, chamamos o método showFull() novamente, e ele vai julgar novamente todo esse processo todo e fazer a divisao, e checar tudo novamente...
            #caso não passe, não há mais necessidade de dividir, pois a arvore não passa aqui
            if quadtree.norteEsq.retangulo.contemPonto(self.funcao):
                quadtree.showFull(quadtree.norteEsq)
            if quadtree.norteDir.retangulo.contemPonto(self.funcao):
                quadtree.showFull(quadtree.norteDir)
            if quadtree.sulDir.retangulo.contemPonto(self.funcao):
                quadtree.showFull(quadtree.sulDir)
            if quadtree.sulEsq.retangulo.contemPonto(self.funcao):
                quadtree.showFull(quadtree.sulEsq)

    def showCurve(self, quadtree):
        #ocorre de maneira semelhante do método acima, a diferença é que as unicas Tree(retangulo) que são adicionadas ao Batch, são aquelas que tem a pronfudidade = profundidade_max
        #isso significa que está no seu maior numero de divisoes e, portanto, de refinamento, logo essas Trees(retangulos) irão exibir a propria curva implicita.
        if quadtree.profundidade == quadtree.profundidade_max:
            self.shapeList.inserir(quadtree.retangulo.getRet())
            return

        if quadtree.retangulo.contemPonto(self.funcao):
            quadtree.divisao(quadtree)

        if quadtree.dividido:

            if quadtree.norteEsq.retangulo.contemPonto(self.funcao):
                quadtree.showCurve(quadtree.norteEsq)
            if quadtree.norteDir.retangulo.contemPonto(self.funcao):
                quadtree.showCurve(quadtree.norteDir)
            if quadtree.sulDir.retangulo.contemPonto(self.funcao):
                quadtree.showCurve(quadtree.sulDir)
            if quadtree.sulEsq.retangulo.contemPonto(self.funcao):
                quadtree.showCurve(quadtree.sulEsq)

    def showHalf(self, quadtree):
        #ocorre de maneira semelhante aos dois métodos acima, a diferença é que antes de adicionar a Tree ao Batch, eu chamo o método getType do retangulo presente na Tree,
        #esse metodo me diz se a área do retangulo está dentro ou fora da curva, e com base nisso teremos retangulos vermelhos ou azuis.
        if quadtree.profundidade == quadtree.profundidade_max:
            quadtree.retangulo.getType(self.funcao)
            self.shapeList.inserir(quadtree.retangulo.getRet())
            return
        if quadtree.retangulo.contemPonto(self.funcao):
            self.shapeList.inserir(quadtree.retangulo.getRet())
            quadtree.divisao(quadtree)

        if quadtree.dividido:

            if quadtree.norteEsq.retangulo.contemPonto(self.funcao):
                quadtree.showHalf(quadtree.norteEsq)
            else:
                quadtree.norteEsq.retangulo.getType(self.funcao)
                self.shapeList.inserir(quadtree.norteEsq.retangulo.getRet())

            if quadtree.norteDir.retangulo.contemPonto(self.funcao):
                quadtree.showHalf(quadtree.norteDir)
            else:
                quadtree.norteDir.retangulo.getType(self.funcao)
                self.shapeList.inserir(quadtree.norteDir.retangulo.getRet())

            if quadtree.sulDir.retangulo.contemPonto(self.funcao):
                quadtree.showHalf(quadtree.sulDir)
            else:
                quadtree.sulDir.retangulo.getType(self.funcao)
                self.shapeList.inserir(quadtree.sulDir.retangulo.getRet())

            if quadtree.sulEsq.retangulo.contemPonto(self.funcao):
                quadtree.showHalf(quadtree.sulEsq)
            else:
                quadtree.sulEsq.retangulo.getType(self.funcao)
                self.shapeList.inserir(quadtree.sulEsq.retangulo.getRet())
