from function import *
from cVetor import Vetor
from cWindow import window
import sys



if __name__ == "__main__":
    #width and height must be equal
    width = 512
    height = 512
    #vector that contains the implicit functions
    funcoes = Vetor(12)
    funcList(funcoes)

    #if didn't got parameter, will initialize with depth 8
    try:
        depth = int((sys.argv[1])) #controls max tree depth
    except:
        depth = 8
    
    x = window(depth, funcoes, width, height)
