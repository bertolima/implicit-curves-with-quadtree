#modulo que contém as funções de todas as curvas implicitas da aplicação.

def f1(x,y):
    return x**3+y-4
    
def f2(x,y):
    return x**4 + y**4 - x*y -8
    
def f3(x,y):
    return ((x**2+y**2 -4)**3 - x**2*y**3)
    
def f4(x,y):
    return x**7 - y**5 + x**2*y**3-(x*y)**2
    
def f5(x,y):
    return (x**2+y**2 + x*y - (x*y)**2*0.5 - 0.25)
    
def f6(x,y):
    return abs(x) + abs(y) - 2

def f7(x,y):
    return x**3+y**2 -6*x*y

def f8(x,y):
    return x**3+y**3 - 3*x*y

def f9(x,y):
    return (3*x**2-y**2)**2*y**2-(x**2+y**2)**4

def f10(x,y):
    return x**2*(4-x**2)-y**2

def f11(x,y):
    return y**3+y**2-5*y-x**2+4

def f12(x,y):
    return (3*x**2-y**2)*y**2-(x**2+y**2)**4

def funcList(funcao):
    funcao.append(f1)
    funcao.append(f2)
    funcao.append(f3)
    funcao.append(f4)
    funcao.append(f5)
    funcao.append(f6)
    funcao.append(f7)
    funcao.append(f8)
    funcao.append(f9)
    funcao.append(f10)
    funcao.append(f11)
    funcao.append(f12)

