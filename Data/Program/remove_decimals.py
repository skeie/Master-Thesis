import sys

with open(sys.argv[1], mode="r") as f:
    out = open(sys.argv[2], mode="w")
    for line in f.readlines():
        cols = line.split(" & ")
        for i, col in enumerate(cols):

            try:
                num = float(col)
                if -0.00001 < num < 0.00001:
                    cols[i] = "0"
                elif -1 < num < 1:
                    cols[i] = "%.3f" % num
            except:
                pass

            if "hline" in col:
                if len(col.split(" ")) is 3:
                    try:
                        num = float(col.split(" ")[0])
                        if -0.00001 < num < 0.00001:
                            cols[i] = "0" + " ".join(col.split(" ")[1:])
                        elif -1 < num < 1:
                            cols[i] = ("%.3f" % num) + " ".join(col.split(" ")[1:])
                    except:
                        pass

        out.write(" & ".join(cols))
    out.close()




