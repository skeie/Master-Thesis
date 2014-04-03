import sys
Dates = []
New_lines = []
with open(sys.argv[1], mode="r") as f:
	out = open("output.csv", "w")

	counter = 0
	for l in f.readlines():
		lines = l.split(",")
		if lines[5] not in Dates:
			Dates.append(lines[5])
			out.write(l)
	out.close()
			

