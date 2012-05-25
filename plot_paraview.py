from paraview.simple import *
#paraview.simple._DisableFirstRenderCameraReset()

Ra_vtr = XMLRectilinearGridReader(FileName=['Ra.vtr'])
Contour1 = Contour(PointMergeMethod="Uniform Binning")
Contour1.ContourBy = ['POINTS', 'Orbital(n=5,l=2,m=1)']
Contour1.Isosurfaces = [0.02]
DataRepresentation2 = Show()


RenderView1 = GetRenderView()
RenderView1.CameraViewUp = [-0.002427339904327421, 0.2246937643466518, 0.97442640578174]
RenderView1.CameraPosition = [0.23721333448610435, -9.62124134519813, 2.219160646819748]
RenderView1.CameraFocalPoint = [0.0, 1e-20, 0.0]
RenderView1.CenterOfRotation = [0.0, 1e-20, 0.0]
RenderView1.CameraClippingRange = [6.186487737063765, 14.545743147772642]


Render()
WriteImage("orbital_n1l0m0.png")
