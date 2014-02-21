import sys
import os 
import re

fn = sys.argv[1]
with open(fn) as f:
    lines = sorted([tuple(l.split(",")) for l in f.readlines()], key=lambda l:int(l[1]))
    to_del = int(len(lines)*0.1)
    lines = lines[to_del:len(lines)-to_del]
    name = os.path.basename(sys.argv[1])
    filename = re.split('[.]', name)
    out = open(filename[0]+"_10percent.csv", mode="w")
    for line in lines:
        out.write(",".join(line))
    out.close()
