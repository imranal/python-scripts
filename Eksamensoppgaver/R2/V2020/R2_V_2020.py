"""
Trignometrisk regresjon:
y = a*sin(b*x + c) + d
"""
from scipy.optimize import curve_fit
from numpy import array, linspace, sin

def f(x,a,b,c,d):
    return a*sin(b*x + c) + d

def reg_sin(x,y,vis=False): 
    popt, pcov = curve_fit(f,x,y)
    a,b,c,d = popt
    
    from sympy import Symbol, sin
    print("Folgende funksjon passer med dataen:")
    uttrykk = a*sin(b*Symbol('x') + c) + d
    print(uttrykk)
    
    if vis:
        from matplotlib.pyplot import plot, scatter, show
        plot(x,f(x,a,b,c,d),c='g')
        scatter(x,y,c='r')
        show()
    
x = linspace(1,12,12)
y = array([1540,1480,1320, 1050, 800, 750, 660, 730, 940, 1170, 1300, 1520])
reg_sin(x,y,vis=True)