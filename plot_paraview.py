import sys
import os
from paraview.simple import *
#paraview.simple._DisableFirstRenderCameraReset()

def get_nlm(i):
    j = 0
    for l in [0, 1, 2, 3]:
        if l == 0:
            nmax = 7
        elif l == 1:
            nmax = 6
        elif l == 2:
            nmax = 5
        elif l == 3:
            nmax = 4
        for n in range(l+1, nmax+1):
            for m in range(-l, l+1):
                if j == i:
                    return n, l, m
                j += 1

os.system("mkdir -p img")
i = int(sys.argv[1])
n, l, m = get_nlm(i)
print "Processing:", n, l, m

Ra_vtr = XMLRectilinearGridReader(FileName=['Ra.vtr'])
Contour1 = Contour(PointMergeMethod="Uniform Binning")
Contour1.ContourBy = ['POINTS', 'Orbital(n=%d,l=%d,m=%d)' % (n, l, m)]
Contour1.Isosurfaces = [0.02]
DataRepresentation2 = Show()


RenderView1 = GetRenderView()
RenderView1.CameraViewUp = [-0.002427339904327421, 0.2246937643466518, 0.97442640578174]
RenderView1.CameraPosition = [0.23721333448610435, -9.62124134519813, 2.219160646819748]
RenderView1.CameraFocalPoint = [0.0, 1e-20, 0.0]
RenderView1.CenterOfRotation = [0.0, 1e-20, 0.0]
RenderView1.CameraClippingRange = [6.186487737063765, 14.545743147772642]


Render()
WriteImage("img/orbital_n%dl%dm%d.png" % (n, l, m))
