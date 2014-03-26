import sys


with open(sys.argv[1], mode="r") as allWIP:
	with open('all_WIP_new.csv', 'w') as f:

		tmp = ""
		for line in allWIP.readlines():
			line_split = line.split(",")
			nr = line_split[4].split("-")
			if int(nr[0]) > 2009:
				if int(nr[0]) == 2010:
					if int(nr[1]) > 2:
						tmp+=line
				else:
					tmp+=line

		f.write(str(tmp))

