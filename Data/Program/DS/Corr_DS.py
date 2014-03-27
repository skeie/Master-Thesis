import sys
def make_float(list):
	new_list = []
	for line in list:
		line = line.split(",")
		for i, col in enumerate(line):
			try:
				num = float(col)
				if -0.00001 < num < 0.00001:
					new_list.append(["0"])
				else:
					new_list.append(["%.1f" % num])
			except:
				pass
	
	return new_list


def formatElement(list):
	tmp =""
	for i, e in enumerate(list):
		if i == 9: 
			return tmp
		tmp += str(e)


def writeOut(list):
	tmp = "WIP " + formatElement(list)
	list = list[9:]
	print tmp, "hello",list




with open(sys.argv[1], mode="r") as f:
	list = make_float(f.readlines())
	writeOut(list)