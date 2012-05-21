try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

xx_vtk = GetActiveSource()
RenderView1 = GetRenderView()
DataRepresentation1 = Show()
DataRepresentation1.Representation = 'Outline'
DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]

a1_Orbital_PVLookupTable = GetLookupTableForArray( "Orbital", 1, NanColor=[0.25, 0.0, 0.0], RGBPoints=[0.0011552225332707167, 0.23, 0.299, 0.754, 0.5172088146209717, 0.706, 0.016, 0.15], VectorMode='Magnitude', ColorSpace='Diverging', ScalarRangeInitialized=1.0 )

a1_Orbital_PiecewiseFunction = CreatePiecewiseFunction()

RenderView1.CameraViewUp = [-0.355570020481162, 0.4609809493934253, 0.8130599761588087]
RenderView1.CameraPosition = [35.291987126832666, -41.44138348142183, 38.93004429573497]
RenderView1.CameraClippingRange = [31.85793261404685, 111.22028336008259]
RenderView1.CameraParallelScale = 17.320508075688775

DataRepresentation1.Representation = 'Surface With Edges'
DataRepresentation1.ColorArrayName = 'Orbital'
DataRepresentation1.LookupTable = a1_Orbital_PVLookupTable

Render()
