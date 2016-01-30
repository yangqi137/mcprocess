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

buf = numpy.empty([repeats, steps])
for i in range(repeats):
    buf[i] = energies[str(i)]
avgs = buf.mean(0)
pyplot.plot(avgs)
pyplot.show()
