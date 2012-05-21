# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

from os.path import join, abspath, dirname

# The offscreen Engine.
from mayavi.api import OffScreenEngine

# Usual MayaVi imports
from mayavi.scripts.util import get_data_dir
from mayavi.sources.api import VTKXMLFileReader
from mayavi.modules.api import Outline, ScalarCutPlane, Streamline


def main():
    # Create the MayaVi offscreen engine and start it.
    e = OffScreenEngine()
    # Starting the engine registers the engine with the registry and
    # notifies others that the engine is ready.
    e.start()

    # Create a new scene.
    win = e.new_scene()

    # Now setup a normal MayaVi pipeline.
    src = VTKXMLFileReader()
    src.initialize("/home/ondrej/Downloads/fire_ug.vtu")
    e.add_source(src)
    e.add_module(Outline())
    e.add_module(ScalarCutPlane())
    e.add_module(Streamline())
    win.scene.isometric_view()
    # Change the size argument to anything you want.
    win.scene.save('offscreen.png', size=(800, 800))


if __name__ == '__main__':
    main()
