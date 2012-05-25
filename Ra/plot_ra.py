from pylab import plot, savefig, legend, xlim, clf
from numpy import loadtxt, size

R = [float(x) for x in open("R.txt").read().split()]

for l in [0, 1, 2, 3]:
    print "Plotting l =", l
    clf()
    eigs = loadtxt("eigs%d.txt" % l)
    if l == 0:
        nmax = 7
    elif l == 1:
        nmax = 6
    elif l == 2:
        nmax = 5
    elif l == 3:
        nmax = 4
    #nmax = size(eigs, 1)
    #nmax = 5
    for n in range(l+1, nmax+1):
        i = n-l-1
        plot(R, eigs[:, i], label="n = %d" % n)
    legend()
    #xlim([0, 1])
    savefig("eigs%d.png" % l)
