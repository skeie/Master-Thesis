import sys
list = []




def splitVariable (var):
	if "*" in var:
		tempz = var.split("*")
		return float(tempz[0].strip())
	else:
		return float(var)

def stars(tempz):
	tempz = tempz.split("*")
	if len(tempz) == 2:
		return "*"
	elif len(tempz) == 3:
		return "**"
	else:
		return ""


output = ""
with open(sys.argv[1], mode="r") as f:
	lines = f.readlines()

	for l, i in enumerate(lines):
		temp = 0
		lines_first_splitted = lines[l].split("\\\\")[0]
		tmp = str(lines_first_splitted)
		tmp = tmp.split("&")
		for nr, val in enumerate(tmp):
			try:
				split = splitVariable(val)
				num = float(split)
				if -0.00001 < num < 0.00001:
					output+="0 &"
				else:
					tempz = ("%.1f" % num)
					if tempz.split('.')[1] == '0':
						output+= tempz.split('.')[0]+" & "
					else:		
						output += str(tempz)+stars(val)+" & "
			except Exception, e:
				tempo = str(e).split(":")[1]
				if tempo.strip() != "-":
					output = output[:-2]
					output+="\\\\ \\hline \n"
					output+= str(e).split(":")[1]+" & "
				else:
					output+="- & "
				pass
	output = output[:-2]
	output+= "\\\\ \\hline"
	print output
			


		





		


		