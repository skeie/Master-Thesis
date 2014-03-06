import sys
fn1 = sys.argv[1]
fn2 = sys.argv[2]

with open(fn1) as f:
    lines = sorted([tuple(l.split(",")) for l in f.readlines()], key=lambda l:int(l[1]))
    to_del = int(len(lines)*0.1)
    lines = lines[to_del:len(lines)-to_del]

with open(fn2) as f2:
    lines2 = sorted([tuple(l.split(",")) for l in f2.readlines()], key=lambda l:int(l[2]))
    low = int(lines2[int(len(lines2)*0.1)][2])
    high = int(lines2[int(len(lines2)*0.9)][2])

    new_lines = []
    print low, high
    for l in lines:
        if low <= int(l[2]) <= high:
            new_lines.append(l)

with open(fn1.split(".")[0]+"_10percent.csv", mode="w") as out:
    for line in new_lines:
        out.write(",".join(line))
    out.close()


