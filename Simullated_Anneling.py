#Alunos:
#Vitor Fernandes Gonçalves da Cruz Ra 120116
#Arthur Belini Pini 118999
#Pedro Lucas Keizo Honda 119188
#Algoritimo Simullated Anneling para a maximização da função objetivo -x**2+50*x +30
import random,math
import numpy  as np
from matplotlib import pyplot as plt
NUMBITS =8#numero de bits maximo
Nint = 10
t0 = 500
tf = 10
alpha = 0.81
solucoesx= []
solucoesy= []
f_x = []
temperaturas = []

def get_vizinhos(x):
    y = []
    x = bin(x)
    x = list(x)
    k = x.copy()
    if(len(x)-2<NUMBITS):

        for i in range(abs(NUMBITS - (len(x)-2))):
            x.insert(2,'0')
            k = x.copy()
    for i in range(2,len(x)):
        if x[i]=='0' :
            k[i]  ='1'
            y.append(k)
        elif x[i]=='1':
             k[i]  ='0'
             y.append(k)

        k = x.copy()

    x = random.choice(y)
    x = ''.join(x)
    return int(x,2)

#função objetivo
def f(x):
    return -x**2+50*x +30

def  simulated_anneling(f,alpha,Nint,t_0,s,tf):
    s_otimo = s
    iterT = 0
    t = t_0
    while(t>tf):
        while(iterT<Nint):
            iterT  =iterT +1
            s_linha = get_vizinhos(s)
            delta = f(s_linha)  - f(s)
            print(f'f({s_linha}) = {f(s_linha)}'+ ' , '+f"f({s}) = {f(s)}",f" s_otimo = {s_otimo}")
            if(delta>0):
                s = s_linha
                if(f(s_linha)>f(s_otimo)):s_otimo = s_linha
            else:
                x = random.random()
                if(pow(x<(math.e),(-delta/t))):s = s_linha
        solucoesy.append(f(s_otimo))
        solucoesx.append(s_otimo)
        t = alpha*t#resfriamento
        iterT = 0
    s = s_otimo

    return s

def main():
    s = 50#de acordo com os bits
    k = simulated_anneling(f,alpha,Nint,t0,s,tf)
    print()
    print("Solução ótima:"+str(k))
    plt.plot(25,f(25),color='red',marker ='o',label = 'Solucão ótima - Já conhecida')
    plt.plot(k,f(k),color='green',marker ='o',label = 'solução ótima-Algoritmo')
    plt.plot(solucoesx,solucoesy,label ='Soluções')
    plt.ylabel('F(x)')
    plt.xlabel('X -soluções')
    plt.gca().invert_xaxis()
    plt.legend()

    plt.show()
main()
