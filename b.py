# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

print "loading"
from os.path import join, abspath, dirname

# The offscreen Engine.
from mayavi.api import OffScreenEngine

# Usual MayaVi imports
from mayavi.scripts.util import get_data_dir
from mayavi.sources.api import VTKXMLFileReader
from mayavi.modules.api import Outline, ScalarCutPlane, Streamline

from mayavi import mlab
import numpy as np
from scipy.special import sph_harm

def main():
    print "start"
    # Create the MayaVi offscreen engine and start it.
    e = OffScreenEngine()
    # Starting the engine registers the engine with the registry and
    # notifies others that the engine is ready.
    e.start()

    # Create a new scene.
    win = e.new_scene()


    # Create a sphere
    r = 0.3
    pi = np.pi
    cos = np.cos
    sin = np.sin
    N = 100
    phi, theta = np.mgrid[0:pi:1j*N, 0:2*pi:1j*N]

    x = r*sin(phi)*cos(theta)
    y = r*sin(phi)*sin(theta)
    z = r*cos(phi)

    mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(400, 300))
    mlab.clf()
    # Represent spherical harmonics on the surface of the sphere
    for l in range(0, 4):
        for m in range(-l, l+1):
            print l, m
            s = abs(sph_harm(m, l, theta, phi))**2

            mlab.mesh(s*x-m, s*y-l, s*z+1.3, scalars=s, colormap='Spectral')
