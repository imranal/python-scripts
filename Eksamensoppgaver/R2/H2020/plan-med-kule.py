from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from math import sqrt

# Planet: 2x - 3y + 7z = 5
# Kule: Sentrum (8, 5, 0) og radius 2*sqrt(62)/31


fig = plt.figure()
ax = fig.gca(projection='3d')

# Fyll inn verdier
X = np.arange(3, 9, 0.5)
Y = np.arange(1, 7, 0.5)
X, Y = np.meshgrid(X, Y)
R = 2*X - 3*Y 
Z = (5 - R)/7

# Tegn planet
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Bestem z aksen
ax.set_zlim(-2, 2)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Legg til farge
fig.colorbar(surf, shrink=0.5, aspect=5)

# Fyll inn verdier for kulen
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 2*sqrt(62)/31 * np.outer(np.cos(u), np.sin(v)) + 8
y = 2*sqrt(62)/31 * np.outer(np.sin(u), np.sin(v)) + 5
z = 2*sqrt(62)/31 * np.outer(np.ones(np.size(u)), np.cos(v)) + 0

# Tegn kulen
ax.plot_surface(x, y, z, color='b')

# Vis grafen
plt.show()