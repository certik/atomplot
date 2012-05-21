from numpy import (arange, size, empty, linspace, sqrt, arctan2, exp, sin, cos,
        pi)
import numpy as np
from scipy.special import sph_harm, genlaguerre
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

rmax = 8.
N = 10  # Number of elements in the radial direction
x = linspace(-rmax, rmax, 2*N)
y = linspace(-rmax, rmax, 2*N)
z = linspace(-rmax, rmax, 2*N)
NX = size(x)
NY = size(y)
NZ = size(z)
# Create a nodal variable
n = 4
l = 3
nodal = empty((2*l+1, NX*NY*NZ), dtype="double")
for k in range(NZ):
   for j in range(NY):
       for i in range(NX):
           r, theta, phi = cart2sph(x[i], y[j], z[k])
           for m in range(-l, l+1):
               nodal[m, k*NX*NY+j*NX+i] = f(n, l, m, r, theta, phi)
vars = []
for m in range(-l, l+1):
    vars.append(("Orbital(l=%d,m=%d)" % (l, m), 1, 1, list(nodal[m, :])))
visit_writer.WriteRectilinearMesh("xx.vtk", 0, list(x), list(y), list(z), vars)
