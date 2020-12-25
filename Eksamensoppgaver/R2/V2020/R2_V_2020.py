def reg_sin(x,y,vis=False):
    """
    Trignometrisk regresjon:
    y = a*sin(b*x + c) + d
    """ 
    from numpy import sin
    def f(x,a,b,c,d):
        return a*sin(b*x + c) + d
    
    from scipy.optimize import curve_fit
    popt, pcov = curve_fit(f,x,y)
    a,b,c,d = popt
    
    # Skriver ut tilnærmingen til verdiene
    from sympy import Symbol, sin
    print("Folgende funksjon passer med dataen:")
    uttrykk = a*sin(b*Symbol('x') + c) + d
    print(uttrykk)
    
    if vis:
        from matplotlib.pyplot import plot, scatter, show
        plot(x,f(x,a,b,c,d),c='g')
        scatter(x,y,c='r')
        show()

"""

Oppgave 1

"""
from numpy import array, linspace, argmax
print("Oppgave 1 a)")
x = linspace(1,12,12)
y = array([1540,1480,1320, 1050, 800, 750, 660, 730, 940, 1170, 1300, 1520])
reg_sin(x,y)


print("\nOppgave 1 b)")
from numpy import sin # Obs! Pass på hvilken sinus funksjon som blir brukt (dvs. enten numpy eller sympy sitt)
f =  1300 + 730*sin(0.52*x + 1.07)
print("Regner ut verdiene for hver maaned og tar differensen mellom maanedene. Slik kan vi se hvor det er storst okning.")
f_verdier = f[1:] - f[:-1]
print(f_verdier)
print("Det var storst okning i maaned nr",argmax(f_verdier)+1)


print("\nOppgave 1 c)")
from sympy import sin, integrate
from sympy.abc import t
I = integrate(1300 + 730*sin(0.52*t + 1.07),(t,0,12))
print("Intregralet blir: I = ",I)
print("Vi kan sammenligne dette med summen av de 12 forste maaneder ved aa bruke uttrykket:")
f_sum = sum(f[:])
print(f_sum, ", der forksjellen mellom integralet og summen blir:",I-f_sum)


print("\nOppgave 1 d)")
from numpy import sin
p = 0.85 + 0.17*sin(0.52*x + 1.07)
aarlig_energi_kostnad = sum(p[:]*f[:])
print("Den aarlige energikostnaden blir: %.2f kr."%aarlig_energi_kostnad)


"""

Oppgave 2

"""
from sympy import Function, Derivative, dsolve
from sympy.abc import t, k
print("Oppgave 2 a)")

M = Function('M')(t)
M_ = Derivative(M,t)
Eqn = M_ - k*M
#sol = dsolve(Eqn, ics={M.subs(t,0): 100, M.subs(t, 6): 97})
