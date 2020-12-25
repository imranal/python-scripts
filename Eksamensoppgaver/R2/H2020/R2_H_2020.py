"""
Eksamen R2 H2020 - Del 2
"""

#######################################
############## Oppgave 1 ##############
#######################################
from sympy import solve
from sympy.abc import x

# Oppgave 1 a)
ant_steg = 9
start = 5000
slutt = 2500
steg = (start - slutt)/ant_steg
s1 = start
s2 = start

for i in range(ant_steg):
    s1 = s1 - steg
    s2 = s2 + s1
print('Oppgave 1 a)')
print('Modell 1:',int(s2),'tonn')


# Oppgave 1 b)
uttrykk = x**ant_steg - 1/2
losning = solve(uttrykk)
prosent = 0
# velg positiv reell løsning for likning x^10 = 1/2
for losn in losning:
    if losn.is_real and losn>0:
        prosent = losn
        break

s1 = start
s2 = start

for i in range(ant_steg):
    s1 = prosent*s1
    s2 = s2 + s1
print('\nOppgave 1 b)')
print('Modell 2:','%.2f'%(s2),'tonn')

# Oppgave 1 c)
uttrykk = 1/(1-x) - 10
losning = solve(uttrykk)
p = float(losning[0])

ant_steg = 10000 # tilsvarer uendlig mange år
start = 5000
s1 = start
s2 = start
for i in range(ant_steg):
    s1 = p*s1
    s2 = s2 + s1
print('\nOppgave 1 c)')
print("Etter",ant_steg,'aar, ser vi at summen', s2,'konverger mot 50000.'+ 
'\nDette forekommer naar vi setter p til aa vaere:',p)



#######################################
############## Oppgave 2 ##############
#######################################
from sympy import Function, Derivative, dsolve, solve, diff, sqrt, pi
from sympy.abc import g, L, t

print('\nOppgave 2 b)')
V = Function('V')(t)
V_ = Derivative(V,t)
V__ = Derivative(V_,t)
print("Loser differensiallikningen med SymPy dsolve:")
eqn = V__+(g/L)*V
Eqn = eqn.subs([(g,9.81),(L,0.2)])
sol = dsolve(Eqn, ics={V.subs(t,0): 0.15, V_.subs(t, 0): 0})
print('V(t) =',sol.rhs)


print('\nOppgave 2 c)')
print("Vi kan lose oppgaven paa to maater:")
print("1) Loser V(t) = 0.15 for t med SymPy solve:")
T1 = solve(sol.rhs - 0.15, t)
print("\tDen ikke-trivielle losningen er da: T =",T1[1])
print("2) Vi regner ut svingetiden ved aa bruke formelen: T = 2*pi*sqrt(L/g)")
T2 = float(2*pi*sqrt(L/g).subs([(g,9.81),(L,0.2)]))
print("\tT = ",T2)



print('\nOppgave 2 d)')
print("Vi kan igjen lose oppgaven paa to maater:")
eqnL = dsolve(eqn, ics={V.subs(t,0): 0.15, V_.subs(t, 0): 0})
uttrykk1 = eqnL.rhs.subs(t,2)
print("1) Loser V(t) = 0.15 for t = 2 og L som ukjent med SymPy solve:\n","0.15 = ",uttrykk1)
L1 = float(solve(uttrykk1 - 0.15, L)[0].subs(g,9.81))
print("\tLosningen er da: T =",L1)
print("2) For aa bestemme L for svingetid paa 2 sekunder, kan vi lose: T = 2*pi*sqrt(L/g)")
uttrykk2 = 2*pi*sqrt(L/g) - 2
l = float(solve(uttrykk2,L)[0].subs([(g,9.81),(L,0.2)]))
print("\tL =",l)



#######################################
############## Oppgave 3 ##############
#######################################
from sympy.physics.vector import ReferenceFrame
from sympy.abc import t, a, b, c, x, y, z 

N = ReferenceFrame('N')

print('\nOppgave 3 a)')
print("Planet alpha er gitt ved ax + by + cz + d = 0, der a = 2, b = -3, c = 7 og d = -5.")
print("La radius til kula vaere r med sentrum i S(8, 5, 0). Siden kula tangerer planet, finner vi radiusen ved aa bruke folgende formel:")
print("r = abs(a*8 + b*5 + c*0)/sqrt(a**2 + b**2 + c**2)")
r = abs(2*8 - 3*5 + 0*7 - 5)/sqrt(2**2 + 3**2 + 7**2)
print("r = ",r,"=","%.3f"%float(r))

print('\nOppgave 3 b)')
# Punktene
A = 1*N.x + 2*N.y - 5*N.z
B = 5*N.x - 2*N.y + N.z
C = t*N.x + N.y +4*N.z
T = 7*N.x + 6*N.y - 3*N.z

AB = A - B
AC = A - C
print("Kryssproduktet med vektorene (A-B) og (A-C) blir:")
kryssprodukt = AB.cross(AC)
print(kryssprodukt)

planet = (x*N.x + y*N.y + z*N.z - A).dot(kryssprodukt)
# Leser av og setter inn manuelt for a, b, c og d
print("Da er planet ax + by + cz + d = 0 gitt ved folgende uttrykk:")
print(planet,"= 0") #-30*x + (4*t - 8)*(z + 5) + (6*t - 42)*(y - 2) + 30
a = -30
b = 6*t - 42
c = 4*t - 8
d = 5*(4*t - 8) + (6*t - 42)*(-2) + 30

print("Bruker formel:")
print("((a,b,c).dot(T) + d)/sqrt(a**2 + b**2 + c**2), som er gitt som 2, til aa lose likningen for t:")
Eqn = (kryssprodukt.dot(T) + d)/sqrt(kryssprodukt.dot(kryssprodukt))
print(Eqn, "= 0")
losning = solve(Eqn-2)
print("t  =",losning[0])


#######################################
############## Oppgave 4 ##############
#######################################
from sympy.abc import x
from sympy import integrate, sin, pi, diff, sqrt

print('\nOppgave 4 a)')
f = -0.3*sin(1.9*x - 4.1) + 0.25
a = 0
b = 1.5
print("Loser integralet V = pi*integral([f(x)]^2 dx)")
V1 = pi*integrate(f**2,(x,a,b))
print("V = ",float(V1),"dm^3")

print('\nOppgave 4 b)')
g = f + 0.03
print("Loser forst integralet V = pi*integral([g(x)]^2 dx)")
V2 = pi*integrate(g**2,(x,a,b))
print("Finner differansen mellom volum fra g og f.")
volum_material = float(V2 - V1)
print("Volumet til materialet glasset er laget av (uten stetten):", volum_material)

print('\nOppgave 4 c)')
print('Vi kan finne en tilnaermet verdi til overflatearealet ved aa dele volumet fra oppgave b med tykkelsen:',volum_material/0.03)

print('\nOppgave 4 d)')
# Deriverer g mhp. x
dgdx = diff(g,x)
g_dgdx = 2*pi*g*sqrt(1 + dgdx**2)
# Setter inn i formelen for overflate av en rotert funksjon om x-aksen
#overflate_glass = integrate(g_x) 
# SymPy klarer ikke å integrere uttrykket, bruker numerisk integrasjon isteden:

from sympy import lambdify
from scipy.integrate import quad
G = lambdify(x, g_dgdx)
overflate_glass = quad(G, a, b,)
print("Overflate arealet til glasset er", overflate_glass[0],"dm^2")


"""
$ python R2H2020.py
Oppgave 1 a)
Modell 1: 37500 tonn

Oppgave 1 b)
Modell 2: 36226.68 tonn

Oppgave 1 c)
Etter 10000 aar, ser vi at summen 49999.99999999999 konverger mot 50000.
Dette forekommer naar vi setter p til aa vaere: 0.9

Oppgave 2 b)
Loser differensiallikningen med SymPy dsolve:
V(t) = 0.15*cos(7.00357051795725*t)

Oppgave 2 c)
Vi kan lose oppgaven paa to maater:
1) Loser V(t) = 0.15 for t med SymPy solve:
        Den ikke-trivielle losningen er da: T = 0.897140293093275
2) Vi regner ut svingetiden ved aa bruke formelen: T = 2*pi*sqrt(L/g)
        T =  0.8971402930932747

Oppgave 2 d)
Vi kan igjen lose oppgaven paa to maater:
1) Loser V(t) = 0.15 for t = 2 og L som ukjent med SymPy solve:
 0.15 =  0.075*exp(2*sqrt(-g/L)) + 0.075*exp(-2*sqrt(-g/L))
        Losningen er da: T = 0.9939608115313336
2) For aa bestemme L for svingetid paa 2 sekunder, kan vi lose: T = 2*pi*sqrt(L/g)
        L = 0.9939608115313336

Oppgave 3 a)
Planet alpha er gitt ved ax + by + cz + d = 0, der a = 2, b = -3, c = 7 og d = -5.
La radius til kula vaere r med sentrum i S(8, 5, 0). Siden kula tangerer planet, finner vi radiusen ved aa bruke folgende formel:
r = abs(a*8 + b*5 + c*0)/sqrt(a**2 + b**2 + c**2)
r =  2*sqrt(62)/31 = 0.508

Oppgave 3 b)
Kryssproduktet med vektorene (A-B) og (A-C) blir:
- 30*N.x + (6*t - 42)*N.y + (4*t - 8)*N.z
Da er planet ax + by + cz + d = 0 gitt ved folgende uttrykk:
-30*x + (4*t - 8)*(z + 5) + (6*t - 42)*(y - 2) + 30 = 0
Bruker formel:
((a,b,c).dot(T) + d)/sqrt(a**2 + b**2 + c**2), som er gitt som 2, til aa lose likningen for t:
(32*t - 364)/sqrt((4*t - 8)**2 + (6*t - 42)**2 + 900) = 0
t  = 17

Oppgave 4 a)
Loser integralet V = pi*integral([f(x)]^2 dx)
V =  0.7146232596726707 dm^3

Oppgave 4 b)
Loser forst integralet V = pi*integral([g(x)]^2 dx)
Finner differansen mellom volum fra g og f.
Volumet til materialet glasset er laget av (uten stetten): 0.10141992578048477

Oppgave 4 c)
Vi kan finne en tilnaermet verdi til overflatearealet ved aa dele volumet fra oppgave b med tykkelsen: 3.3806641926828256

Oppgave 4 d)
Overflate arealet til glasset er 3.748403859275869 dm^2
"""