import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def edo(y0, t, k, m, F): 
    u, omega = y0 # y é o vetor [u, omega]
    dydt = [omega, F*math.cos(math.sqrt(k)*t)-k/m*u] # dydt é o vetor contendo as EDOs
    return dydt

# Constantes do sistema
m = c1
k = c2
F = c3
# Condições iniciais
y0 = [u0, omega0] # u(0)=u0   omega(0)=omega0 (lembre-se, omega é a derivada primeira de u)

t = np.linspace(Início, Final, QntPontos) # Estes são os pontos usados para gerar o gráfico

sol = odeint(edo, y0, t, args=(k, m, F)) # A função odeint gera a solução

print(sol)
# A solução é uma matriz(101,2). A primeira coluna é u(t), e a segunda é omega(t)

#Apesar da solução nos fornecer valores para u e para omega, vamos apenas visualizar o gráfico de u(t)
#plt.plot(t, sol[:, 1], 'g', label='omega(t)') Para visualizar omega(t)
plt.plot(t, sol[:, 0], 'b', label='u(t)') 
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()