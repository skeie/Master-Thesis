import sys

Throughput = []
Throughput_ft = []
Throughput_bug = []
leadtime = []
precent_bugs = []
Average_days_in_backlog_bugs = []
WIP = []
Churn = []
Churn_ft = []
Churn_bugs = []
Churn_average = []
Bugs = []


def diagonal_data(list, index):
	print list
	WIP.append(list[0])

	Throughput.append(list[1])
	Throughput_ft.append(list[2])
	Throughput_bug.append(list[3])
	Bugs.append(list[4])

	precent_bugs.append(list[5])
	Average_days_in_backlog_bugs.append(list[6])
	leadtime.append(list[7])


	Churn.append(list[8])
	Churn_ft.append(list[9])
	Churn_bugs.append(list[10])

def makeFloat(list):
	index = None
	for i,l in enumerate(list):
		t = str(l)
		if t.strip() is "1":
			index = i
		try:
			num = float(l)
			if -0.00001 < num < 0.00001:
				list[i] = "0"
			else:
				list[i] = "%.2f" % num
				#if list[i].split('.')[1] == '00':
					#list[i] = '0'
		except:
			pass

	if index != None:
		print "S"
		#del list[index]

def writeOutList(list):
	temp = " "
	for l in list:
		temp +=str(l)+"& "
	temp = temp.strip()
	temp = temp[:-1] #need to remove the last &
	temp +="\\\\ \\hline \n"
	return temp

def writeToFile():
	tmp = "\\begin{table}[!htbp] \n \centering \n \\begin{tabular}{|l|r|r|r|r|r|r|r|r|r|r|} \n\\hline \n"
	tmp+=" &  \\bf{WIP} & \\bf{TP} & \\bf{TP_ft} & \\bf{TP_bug} & \\bf{Bugs} & \\bf{Bugs, qrt} & \\bf{Avg backlog bugs} & \\bf{Lead time} & \\bf{Churn} & \\bf{Churn ft} & \\bf{Churn bug}\\\\ \\hline\n"
	tmp+= "WIP &"+writeOutList(WIP)
	tmp+= "Throughput &"+ writeOutList(Throughput)
	tmp+= "Throughput Feature &" + writeOutList(Throughput_ft)
	tmp+= "Throughput bug &"+writeOutList(Throughput_bug)		
	tmp+= "Bugs &"+writeOutList(Bugs)
	tmp+= "Bugs finished, quarter &"+writeOutList(precent_bugs)
	tmp+= "Avg days in backlog, bugs &"+writeOutList(Average_days_in_backlog_bugs)
	tmp+= "Lead time &" + writeOutList(leadtime)
	tmp+= "Churn &"+writeOutList(Churn)
	tmp+= "Churn feature &" + writeOutList(Churn_ft)
	tmp+= "Churn bug &"+writeOutList(Churn_bugs)
	tmp+= "\n\\end{tabular} \n \caption{Correlation - Leadtime} \n \label{corr:WIP} \n "
	tmp+= "\\centerline {* Correlation is significant at the 0.05 level (2-tailed).} \n"
	tmp+= "\\centerline{** Correlation is significant at the 0.01 level (2-tailed).} \n"
	tmp+= "\\centerline{c. Cannot be computed because at least one of the variables is constant.} \n"
	tmp+= "\\end{table}  \n\n"
	print tmp


with open(sys.argv[1],mode="r") as three:

	for line in three.readlines():
		if "Pearson Correlation" in line:
			line = line.split(",")
   			line = line[2:]
			makeFloat(line)
			diagonal_data(line, 0)

writeToFile()

