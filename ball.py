t = 11.00
d = 0.0019
D = 0.061
s = 0.1465
rho = 960.5
m = 0.00003276
g = 9.7940
ut = 0.06
ud = 0.0000056
uD = 0.000036
us = 0.00090
urho = 1
um = 0.000000002
nd = - g * D / 18 * (6 * m / (3.1416) * ((D + 4.8 * d) / (d**2 * (D + 2.4 * d)**2)) + rho * ((2 * D * d + 2.4 * d**2) / (D + 2.4 * d)**2)) * t / s
nD = g / 18 * (6 * m / (3.1416 * d) - rho * d**2) * t / s * (2.4 * d / (D + 2.4 * d)**2)
ns = -g / 18 * (6 * m / (3.1416 * d) - rho * d**2) * t / s**2 * (D / (D + 2.4 * d))
nt = g / 18 * (6 * m / (3.1416 * d) - rho * d**2) / s * (D / (D + 2.4 * d))
nrho = - g / 18 * t * d**2 / s * (D / (D + 2.4 * d))
nm = (g / 18) * (6 / (3.1416 * d)) * (t / s) * (D / (D + 2.4 * d))
print(nd)
print(nD)
print(ns)
print(nt)
print(nrho)
print(nm)
print()
print(nd * ud)
print(nD * uD)
print(ns * us)
print(nt * ut)
print(nrho * urho)
print(nm * um)
print()
eta = ((nd * ud)**2 + (nD * uD)**2 + (ns * us)**2 + (nt * ut)**2 + (nrho * urho)**2 + (nm * um)**2)**0.5
print(eta)