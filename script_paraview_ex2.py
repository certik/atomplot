try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

xx_vtk = LegacyVTKReader( FileNames=['/home/ondrej/repos/atomplot/xx.vtk'] )

RenderView1 = GetRenderView()
DataRepresentation1 = Show()
DataRepresentation1.Representation = 'Outline'
DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]

Clip1 = Clip( ClipType="Plane" )

a1_Orbitall3m0_PVLookupTable = GetLookupTableForArray( "Orbital(l=3,m=0)", 1, NanColor=[0.25, 0.0, 0.0], RGBPoints=[3.1525646591035184e-06, 0.23, 0.299, 0.754, 54.84083557128906, 0.706, 0.016, 0.15], VectorMode='Magnitude', ColorSpace='Diverging', ScalarRangeInitialized=1.0 )

a1_Orbitall3m0_PiecewiseFunction = CreatePiecewiseFunction()

RenderView1.CameraViewUp = [0.12833973181369285, 0.8442055935847236, -0.5204285051745859]
RenderView1.CameraPosition = [-22.582979971750884, 27.91427101323882, 39.711679763110816]
RenderView1.CameraClippingRange = [26.176766636208647, 88.10712946939637]
RenderView1.CameraParallelScale = 13.856406460551018

DataRepresentation1.Representation = 'Surface With Edges'
DataRepresentation1.ColorArrayName = 'Orbital(l=3,m=0)'
DataRepresentation1.LookupTable = a1_Orbitall3m0_PVLookupTable

Clip1.Scalars = ['POINTS', 'Orbital(l=3,m=-1)']
Clip1.ClipType = "Plane"

a1_Orbitall3m3_PVLookupTable = GetLookupTableForArray( "Orbital(l=3,m=-3)", 1, NanColor=[0.25, 0.0, 0.0], RGBPoints=[2.596137278487731e-07, 0.23, 0.299, 0.754, 19.327486038208008, 0.706, 0.016, 0.15], VectorMode='Magnitude', ColorSpace='Diverging', ScalarRangeInitialized=1.0 )

a1_Orbitall3m3_PiecewiseFunction = CreatePiecewiseFunction()

DataRepresentation2 = Show()
DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]
DataRepresentation2.ScalarOpacityFunction = a1_Orbitall3m3_PiecewiseFunction
DataRepresentation2.ColorArrayName = 'Orbital(l=3,m=-3)'
DataRepresentation2.ScalarOpacityUnitDistance = 1.5644997847960056
DataRepresentation2.LookupTable = a1_Orbitall3m3_PVLookupTable

RenderView1.CameraClippingRange = [20.054266587135796, 95.81409561157099]

DataRepresentation1.Visibility = 0

RenderView1.CameraViewUp = [0.38850742829545465, 0.8929611730813896, -0.22733746177953335]
RenderView1.CameraPosition = [-40.559315801324594, 24.09100697465176, 25.313638712927865]
RenderView1.CameraClippingRange = [19.740023649956957, 96.20966272595997]

Render()
