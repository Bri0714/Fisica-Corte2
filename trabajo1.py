# librerias pertinente
import numpy as np
import matplotlib.pyplot as plt


# ---Parametros
m = 0.1
b = 0.8          # Coeficiente de fricción con el medio.
Tm = 8.        # Tiempo má
g = 9.8         # Aceleración de la gravedad
L = 0.5          # Longitud del pendulo
dt = 0.001  # Incremento en el tiempo en s.
# ---Condiciones iniciales
Tho = 0.3  # --posición en
wo = 0.0  # --velocidad en metros/segundo

# ---Función aceleración


def a(w, Th, t):
    bo = b/m
    alpha = -bo*w-(g/L)*np.sin(Th)
    return round(alpha, 2)
# ----
# print("prueba= ",a(2,0.5,2))


# --Ciclo principal
X, T = [], []  # --Listas de posición angular y tiempo
V = []  # --VELOCIDAD angular
A = []  # --Aceleracion anguar
t = 0
x, v = Tho, wo
while t <= Tm:
    T.append(t)
    X.append(x)
    V.append(v)
    kx1 = v*dt  # inicio de paso de rungekutta 4 orden  No se toca leyes de la naturaleza
    kv1 = a(v, x, t)*dt
    kx2 = (v+0.5*kv1)*dt
    kv2 = a(v+0.5*kv1, x+0.5*kx1, t+0.5*dt)*dt
    kx3 = (v+0.5*kv2)*dt
    kv3 = a(v+0.5*kv2, x+0.5*kx2, t+0.5*dt)*dt
    kx4 = (v+kv3)*dt
    kv4 = a(v+kv3, x+kx3, t+dt)*dt
    x = x+(kx1+2*kx2+2*kx3+kx4)/6.0
    v = v+(kv1+2*kv2+2*kv3+kv4)/6.0  # fin de paso de rungekutta 4 orden
    t = t+dt

#plt.plot(T,X) # Tiempo vs ángulo
#plt.xlabel('$t(s)$',fontsize=14)
#plt.ylabel(r'$\theta(rad)$',fontsize=14)
#plt.grid()
#plt.show()

#Energia cinetica 
Ec = 0.5*m*(L**2)*(np.array(V)**2)
print(Ec)

#Energia potencial
Ep = m*g*L*(1-np.cos(np.array(X)))
print(Ep)

#Energia mecanica
Em = Ec+Ep
print(Em)

'''#Grafica de energia cinetica vs el tiempo
plt.plot(T,Ec)
plt.xlabel('$t(s)$',fontsize=14)
plt.ylabel(r'$Ec(J)$',fontsize=14)
plt.grid()
plt.show()'''

'''#Grafica de energia potencial vs el tiempo
plt.plot(T,Ep)
plt.xlabel('$t(s)$',fontsize=14)
plt.ylabel(r'$Ep(J)$',fontsize=14)
plt.grid()
plt.show()'''

'''#Grafica de energia mecanica vs el tiempo
plt.plot(T,Em)
plt.xlabel('$t(s)$',fontsize=14)
plt.ylabel(r'$Em(J)$',fontsize=14)
plt.grid()
plt.show()'''

'''#Grafica de energia mecanica vs angulo
plt.polar(X,Em)
plt.xlabel(r'$\theta(rad)$',fontsize=14)
plt.ylabel('Ep(J)', fontsize=14, labelpad=30)
plt.title('Grafica de energia mecanica en funcion del angulo ')
plt.grid()
plt.show()'''

#Grafica de energia potencial vs angulo
plt.polar(X,Ep)
plt.xlabel(r'$\theta(rad)$',fontsize=14)
plt.ylabel('Ep(J)', fontsize=14, labelpad=30)
plt.title('Grafica de energia potencial en funcion del angulo ')
plt.grid()
plt.show()

'''#Grafica de energia cinetica vs angulo
plt.polar(X,Ec)
plt.xlabel(r'$\theta(rad)$',fontsize=14)
plt.ylabel('Ec(J)', fontsize=14, labelpad=30)
plt.title('Grafica de energia cinetica en funcion del angulo ')
plt.grid()
plt.show()'''
