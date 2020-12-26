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
from sympy import Function, Derivative, dsolve, solve, Eq, symbols, diff
t,k = symbols('t,k', real=True) # Trenger argumentet real for aa unngaa aa haantere komplekse losninger
print("\nOppgave 2 b)")

M = Function('M')(t)
M_ = Derivative(M,t)
Eqn = M_ - k*M
M0 = 100
t_ = 0
sol = dsolve(Eqn, ics={M.subs(t,t_): M0})
uttrykk = sol.rhs
print("Losningen blir:",uttrykk,"for M(%.1f) = %.1f"%(t_,M0))
M6 = 97
t_ = 6
print("Loser",uttrykk,"for k, for M(%5.2f) = %.2f"%(t_,M6))
uttrykk_2 = uttrykk.subs(t,t_)
#k_verdi = float(solve(Eq(uttrykk_2, M6),k)[-1])
k_verdi = float(solve(Eq(uttrykk_2, M6),k)[0])
uttrykk_med_k = uttrykk.subs(k,k_verdi)
print("M(t) =",uttrykk_med_k)

print("\nOppgave 2 c)")
M__ = 2
uttrykk_3 = Eq(uttrykk, M__)
t_ = float(solve(uttrykk_3, t)[0].subs(k,k_verdi)) # Av visse grunner klarer ikke solve aa lose med k_verdi
print("Det tar %f timer for stoffet aa naa %.2f mg per time"%(t_,M__))

print("\nOppgave 2 d")
uttrykk4 = diff(uttrykk,t)
t_ = solve(uttrykk4 + 0.2, t)[0].subs(k, k_verdi) #Loser M'(t) = -0.2
print("Det tar %f timer for stoffet aa regnes som ufarlig."%t_)


"""

Oppgave 3

"""
from math import pi
print("\nOppgave 3 a)")
diameter = 5.03
tot_lengde = 0

for i in range(1,51):
    diameter = diameter + 2*0.015
    tot_lengde = tot_lengde + pi*diameter
print("Etter 50 runder tilsvarer det ca. %.2f m for han er tom."%(tot_lengde/100))    


print("\nOppgave 3 b)")
from sympy.abc import n
from sympy import solve, Eq
a1 = 5.0
d = 0.03*pi
an = a1 + (n-1)*d
sn = (a1 + an)*n/2
n_verdi = int(solve(Eq(an,14),n)[0]) # bruker formel for aritmetisk rekke og løser for n
tot_lengde = float(sn.subs(n,n_verdi))
print("Bruker formel for aritmetisk rekke og loser for n. Total lengde er da ca.: %.2f m."%(tot_lengde/100))  
 
 
print("\nOppgave 3 c)")
n_verdi = int(solve(Eq(sn,50000),n)[1])
D = (an.subs(n,n_verdi) + 5)/pi
print("D = %.2f cm."%D)
