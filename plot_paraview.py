from paraview.simple import *
#paraview.simple._DisableFirstRenderCameraReset()

Ra_vtr = XMLRectilinearGridReader(FileName=['Ra.vtr'])
Contour1 = Contour(PointMergeMethod="Uniform Binning")
Contour1.ContourBy = ['POINTS', 'Orbital(n=1,l=0,m=0)']
Contour1.Isosurfaces = [0.4829863905906677]
DataRepresentation2 = Show()
Render()
WriteImage("orbital_n1l0m0.png")
