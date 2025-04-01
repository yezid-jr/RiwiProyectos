import numpy as np
import matplotlib.pyplot as plt

# Parámetros
t = np.linspace(0, 2 * np.pi, 1000)

# Ecuaciones paramétricas
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# # Crear el gráfico
plt.figure(figsize=(6,6))
plt.plot(x, y, color='red', linewidth=2)

# # Configurar el gráfico
plt.title("Corazón en Python")
plt.axis('equal')
plt.fill(x,y, 'r', alpha=(0.6))

plt.text(0, -20, "hola ", fontsize=14, ha='center', va='center')
# # Mostrar el gráfico
plt.show()
#hola mundo
