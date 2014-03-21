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
def writeOutTable(list, nr):
	tmp =""
	for i, element in enumerate(list):
		if i == nr:
			tmp+="\\\\ \\hline"
			return tmp
		else:
			tmp += " & "+str(element[0])

def writeOutTableSpecial(list):
	tmp =""
	for i, element in enumerate(list):
		tmp += " & "+str(element[0])
	return tmp

def writeOut(list):
	counter = 6
	tmp = "\\begin{table}[!htbp] \n \centering \n \\begin{tabular}{ | l | r | r | r | r | r | r | } \n \\hline"
	tmp+= "\n Quarter &	N &	Mean &	Median & Std.Dev & Max	& Min \\\\ \\hline\n"

	tmp+= "2010-3 "+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+="2010-4"+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+="2011-1"+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+="2011-2"+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+="2011-3"+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+="2011-4"+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+="2012-1"+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+="2012-2"+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+="2012-3"+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+="2012-4"+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+="2013-1"+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+="2013-2"+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+="2013-3"+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+="2013-4"+writeOutTableSpecial(list)+"\\\\ \\hline"
	tmp+= "\n\\end{tabular} \n \caption{Descriptive Statistic - Bugs} \n \label{DS:Bugs:"+input+"} \n "
	tmp+= "\\end{table}  \n\n"

	print tmp


with open(sys.argv[1], mode="r") as f:
	input =str(raw_input()) 
	list = make_float(f.readlines())
	writeOut(list)
	
			