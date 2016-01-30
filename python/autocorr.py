import sys
import json
import numpy
from matplotlib import pyplot

if len(sys.argv) != 2:
    print "Useage: ", sys.argv[0], " data_file"

with open(sys.argv[1]) as f:
    data = json.load(f)

energies = data["energy"]
repeats = len(energies)
steps = len(energies["0"])

n0 = 700
l = 300

buf = numpy.empty([repeats, l])

for i in range(repeats):
    buf[i] = energies[str(i)][n0:(n0+l)]

autocorr = numpy.empty(l)
means = buf.mean()
print means
for i in range(l):
    prod = (buf[:, 0]-means) * (buf[:, i]-means)
    autocorr[i] = prod.mean()
pyplot.plot(autocorr)
pyplot.show()
