import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def edo(y, t, k, m, gamma): 
    u, omega = y # y é o vetor [u, omega]
    dydt = [omega, -gamma/m*omega -k/m*u] # dydt é o vetor contendo as EDOs
    return dydt

# Constantes do sistema
m = 1
k = 10
gamma=2

# Condições iniciais
y0 = [-2, 0.0] # u(0)=-2   omega(0)=0 (lembre-se, omega é a derivada primeira de u)

t = np.linspace(0, 10, 101) # Estes são os pontos usados para gerar o gráfico

sol = odeint(edo, y0, t, args=(k, m, gamma)) # A função odeint gera a solução

print(sol)
# A solução é uma matriz(101,2). A primeira coluna é u(t), e a segunda é omega(t)

#Apesar da solução nos fornecer valores para u e para omega, vamos apenas visualizar o gráfico de u(t)
#plt.plot(t, sol[:, 1], 'g', label='omega(t)') Para visualizar omega(t)
plt.plot(t, sol[:, 0], 'b', label='u(t)') 
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()