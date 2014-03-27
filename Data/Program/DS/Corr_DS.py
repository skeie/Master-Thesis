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
	tmp = "\\begin{table}[!htbp] \n \centering \n \\begin{tabular}{ | l | r | r | r | r | r | r | } \n \\hline \n"
	tmp+="& N & Mean & Median & Std.Dev & Max & Min \\\\ \\hline 	\n"
	tmp+= "WIP "+writeOutTable(list,counter)+"\n"
	list = list[6:]	
	tmp+= "Throughput "+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+= "Throughput ft "+writeOutTable(list,counter)+"\n"
	list = list[6:]	
	tmp+= "Throughput bug "+writeOutTable(list,counter)+"\n"
	list = list[6:]	
	tmp+= "Bugs "+writeOutTable(list,counter)+"\n"
	list = list[6:]	
	tmp+= "Bugs finished, quarter "+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+= "Avg days backlog, bugs "+writeOutTable(list,counter)+"\n"
	list = list[6:]	
	tmp+= "Churn "+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+= "Churn ft "+writeOutTable(list,counter)+"\n"
	list = list[6:]
	tmp+= "Churn bug "+writeOutTableSpecial(list)+"\\\\ \\hline"
	tmp+= "\n\\end{tabular} \n \caption{Descriptive Statistic - Correlation - Throughput} \n \label{DS:corr:TP} \n "
	tmp+= "\\end{table}  \n\n"
	print tmp

with open(sys.argv[1], mode="r") as f:
	list = make_float(f.readlines())
	writeOut(list)