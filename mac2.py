try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

xx_vtk = GetActiveSource()
RenderView1 = GetRenderView()
DataRepresentation1 = Show()
DataRepresentation1.Representation = 'Outline'
DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]

Slice1 = Slice( SliceType="Plane" )

RenderView1.CameraViewUp = [0.0, 0.0, 1.0]
RenderView1.CameraPosition = [0.0, -66.92130429902464, 0.0]
RenderView1.CameraClippingRange = [46.35209125603439, 92.97512386351]
RenderView1.CameraFocalPoint = [0.0, 1e-20, 0.0]
RenderView1.CameraParallelScale = 17.320508075688775
RenderView1.CenterOfRotation = [0.0, 1e-20, 0.0]

Slice1.SliceOffsetValues = [0.0]
Slice1.SliceType = "Plane"

a1_Orbitall2m2_PVLookupTable = GetLookupTableForArray( "Orbital(l=2,m=-2)", 1, NanColor=[0.25, 0.0, 0.0], RGBPoints=[0.00021071397350169718, 0.23, 0.299, 0.754, 0.6468487977981567, 0.706, 0.016, 0.15], VectorMode='Magnitude', ColorSpace='Diverging', ScalarRangeInitialized=1.0 )

a1_Orbitall2m2_PiecewiseFunction = CreatePiecewiseFunction()

DataRepresentation2 = Show()
DataRepresentation2.ColorArrayName = 'Orbital(l=2,m=-2)'
DataRepresentation2.LookupTable = a1_Orbitall2m2_PVLookupTable
DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]

RenderView1.CameraClippingRange = [40.68727838600876, 100.1059561446227]

Slice1.SliceType.Normal = [0.0, 1.0, 0.0]

RenderView1.CameraViewUp = [0.0, 0.0, 1.0]
RenderView1.CameraPosition = [0.0, -81.96345860884203, 0.0]
RenderView1.CameraClippingRange = [55.41088209961214, 115.58538260730603]
RenderView1.CameraFocalPoint = [0.0, 1e-20, 0.0]
RenderView1.CameraParallelScale = 21.213704090440476

Render()
