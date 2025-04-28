import numpy as np
import matplotlib.pyplot as plt

# Définition de la fonction f(x)
def f(x, mu=0, sigma=1):
    return (1 / (2 * np.pi)) * np.exp(-((x - mu)**2) / sigma**2)

# Création des valeurs de x
x = np.linspace(-5, 5, 400)
y = f(x)

# Tracer la courbe
plt.plot(x, y)
plt.grid(True)
plt.show()
