Atomplot
========

Notes about VTK formats
-----------------------

To generate VTK from Python or Fortran, use the legacy ASCII VTK format. It is
easy to write and can be manually checked.
Then use it as it is in ParaView, or convert it to the newest XML binary format
using::

    ./vtk2xml.py xx.vtk

This will generate ``xx.vtr`` (the extension will depend on the type of data in
``xx.vtk``).
