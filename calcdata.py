from numpy import (arange, size, empty, linspace, sqrt, arctan2, exp, sin, cos,
        pi, loadtxt, log)
import numpy as np
from scipy.special import sph_harm, genlaguerre
from scipy.interpolate import UnivariateSpline
import visit_writer

def sph2cart(r, theta, phi):
    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)
    return x, y, z

def cart2sph(x, y, z):
    xy = x**2 + y**2
    r = sqrt(xy + z**2)
    theta = arctan2(sqrt(xy), z)
    phi = arctan2(y, x)
    if phi < 0:
        phi += 2*pi
    return r, theta, phi

print "Loading data..."
_R = [float(x) for x in open("Ra/R.txt").read().split()]
_eigs = [loadtxt("Ra/eigs%d.txt" % l) for l in [0, 1, 2, 3]]
print "Done."

def R(n, l, r):
    assert n > l
    a0 = 0.3
    return (2*r/n/a0)**l * exp(-r/n/a0) * genlaguerre(n-l-1,2*l+1)(2*r/n/a0)

def Ylm(l, m, theta, phi):
    assert l >= abs(m)
    return sph_harm(m, l, phi, theta)

def rho(n, l, m, r, theta, phi):
    return abs(R(n, l, r) * Ylm(l, m, theta, phi))**2


def f(n, l, m, r, theta, phi):
    return rho(n, l, m, r, theta, phi)

def f2(n, l, m, r, theta, phi, Rnl):
    return abs(Rnl * Ylm(l, m, theta, phi))**2

def mesh_exp(rmin, rmax, a, N):
    beta = log(a) / (N - 1)
    alpha = (rmax - rmin) / (exp(beta*N) - 1)
    i = linspace(1, N+1, N+1)
    return alpha * (exp(beta*(i-1))-1) + rmin

rmax = 25.
N = 10  # Number of elements in the radial direction
x = empty(2*N+1, dtype="double")
x[N:2*N+1] = mesh_exp(0, rmax, 400, N)
x[0:N+1] = -mesh_exp(0, rmax, 400, N)[::-1]
print x
y = x
z = x
NX = size(x)
NY = size(y)
NZ = size(z)
# Create a nodal variable
vars = []
nodal = empty(NX*NY*NZ, dtype="double")
for l in [0, 1, 2, 3]:
    if l == 0:
        nmax = 7
    elif l == 1:
        nmax = 6
    elif l == 2:
        nmax = 5
    elif l == 3:
        nmax = 4
    for n in range(l+1, nmax+1):
        Rnl = UnivariateSpline(_R, _eigs[l][:, n-l-1], k=3)
        for m in range(-l, l+1):
            print n, l, m
            for k in range(NZ):
               for j in range(NY):
                   for i in range(NX):
                       r, theta, phi = cart2sph(x[i], y[j], z[k])
                       nodal[k*NX*NY+j*NX+i] = f2(n, l, m, r, theta, phi,
                               Rnl(r))
            vars.append(("Orbital(n=%d,l=%d,m=%d)" % (n, l, m), 1, 1,
                list(nodal)))
visit_writer.WriteRectilinearMesh("Ra.vtk", 0, list(x), list(y), list(z), vars)
