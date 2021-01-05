from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from math import sqrt

# Planet: 7x - 14y - 14z = -21
# Kule: Sentrum (-13, -15, -2) med radius r = 8

fig = plt.figure()
ax = fig.gca(projection='3d')

# Fyll inn verdier
X = np.arange(-22, 10, 0.5)
Y = np.arange(-22, 10, 0.5)
X, Y = np.meshgrid(X, Y)
R = 7*X - 14*Y 
Z = (-21 - R)/-14


# Tegn planet
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Bestem z aksen
ax.set_zlim(-15, 8)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Tegn linja
#r = (-6*t - 1)*X + (-7*t - 1)*Y + (2 - 2*t)*Z
t = np.linspace(-2, 4, 100)
z = 2 - 2*t
x = -7*t - 1
y = -6*t - 1
ax.plot (x,y,z)


# Legg til farge
fig.colorbar(surf, shrink=0.5, aspect=5)

# Fyll inn verdier for kulen
r = 8
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = r * np.outer(np.cos(u), np.sin(v)) - 13
y = r * np.outer(np.sin(u), np.sin(v)) - 15
z = r * np.outer(np.ones(np.size(u)), np.cos(v)) - 2

# Tegn kulen
ax.plot_surface(x, y, z, color='b')

# Vis grafen
plt.show()