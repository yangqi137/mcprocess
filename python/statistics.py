import sys
import json
import numpy
from matplotlib import pyplot

if len(sys.argv) != 2:
    print "Useage: ", sys.argv[0], " data_file"

with open(sys.argv[1]) as f:
    data = json.load(f)

energies = data["energy"]

