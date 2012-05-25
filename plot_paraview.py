from paraview.simple import *
#paraview.simple._DisableFirstRenderCameraReset()

Ra_vtr = XMLRectilinearGridReader(FileName=['Ra.vtr'])
Contour1 = Contour(PointMergeMethod="Uniform Binning")
Contour1.ContourBy = ['POINTS', 'Orbital(n=5,l=2,m=1)']
Contour1.Isosurfaces = [0.02]
DataRepresentation2 = Show()
Render()
WriteImage("orbital_n1l0m0.png")
