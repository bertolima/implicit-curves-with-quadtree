from function import *
from cVetor import Vetor
from cWindow import window
import sys



if __name__ == "__main__":
    #depth controla a pronfudidade maxima inicial da Tree
    depth = int(sys.argv[1])
    funcoes = Vetor(12)
    #esses dois parametros controlam o tamanho das janelas e dos quadrados que representarão as curvas implicitas.
    #É DE EXTREMA IMPORTÂNCIA QUE ELES SEJAM IGUAIS, CASO CONTRÁRIO A VISUALIZAÇÃO SERÁ PREJUDICADA.
    #Além disso, se a curva for restrita por valores muito baixos em coordenadas cartesianas, e utilizarmos tamanhos muito grandes de janela, por conta do fato de conversão entre
    #as coordenadas, as curvas que são limitadas por esse valores baixos serão prejudicadas
    width = 512
    height = 512

    funcList(funcoes)
    x = window(depth, funcoes, width, height)
