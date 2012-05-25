from paraview.simple import *
# Create a simple pipeline
sph = Sphere()
elev = Elevation(sph)
Show(elev)
Render()
# Set the representation type of elev
dp = GetDisplayProperties(elev)
dp.Representation = 'Points'
# Here is how you get the list of representation types
dp.GetProperty("Representation").Available
Render()
# Change the representation to wireframe
dp.Representation = 'Wireframe'
Render()
# Let’s get some information about the output of the elevation
# filter. We want to color the representation by one of it’s
# arrays.
# Second array = Elevation. Interesting. Let’s use this one.
ai = elev.PointData[1]
ai.GetName()
# What is its range?
ai.GetRange()
# To color the representation by an array, we need to first create
# a lookup table.  We use the range of the Elevation array
dp.LookupTable = MakeBlueToRedLT(0, 0.5)
dp.ColorAttributeType = 'POINT_DATA'
dp.ColorArrayName = 'Elevation' # color by Elevation
Render()
WriteImage("image.png")

print "Writing to file:"
writer = CreateWriter("ff.vtk")
writer.UpdatePipeline()
print "Done"
