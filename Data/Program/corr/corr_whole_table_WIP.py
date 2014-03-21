import sys

Bugs = []
Throughput = []
Throughput_ft = []
Throughput_bug = []
Bugs = []
precent_bugs = []
Average_days_in_backlog_bugs = []
Leadtime = []
Churn = []
Churn_ft = []
Churn_bugs = []
Churn_average = []

def diagonal_data(list, index):
	Throughput.append(list[0])
	Throughput_ft.append(list[1])
	Throughput_bug.append(list[2])

	Bugs.append(list[3])
	precent_bugs.append(list[4])
	Average_days_in_backlog_bugs.append(list[5])

	Leadtime.append(list[6]) 

	Churn.append(list[7])
	Churn_ft.append(list[8])
	Churn_bugs.append(list[9])

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
		except:
			pass

	if index != None:
		del list[index]
	

def writeOutList(list):
	temp = " "
	for l in list:
		temp +=str(l)+"& "
	temp = temp.strip()
	temp = temp[:-1] #need to remove the last &
	temp +="\\\\ \\hline \n"
	return temp


def writeToFile():
	tmp = "\\begin{table}[!htbp] \n \centering \n \\begin{tabular}{|l|r|r|r|r|r|r|} \n\\hline \n"
	tmp+=" & T1 & T2 & T3 & T4 & T5 & T6 \\\\ \\hline\n"
	tmp+= "Throughput &"+ writeOutList(Throughput)
	tmp+= "Throughput Feature &" + writeOutList(Throughput_ft)
	tmp+= "Throughput bug &"+writeOutList(Throughput_bug)
	tmp+= "Bugs &" + writeOutList(Bugs)
	tmp+= "Bugs finished in the same quarter &"+writeOutList(precent_bugs)
	tmp+= "The average days for bugs in backlog &"+writeOutList(Average_days_in_backlog_bugs)
	tmp+= "Leadtime &"+writeOutList(Leadtime)
	tmp+= "Churn &"+writeOutList(Churn)
	tmp+= "Churn feature &" + writeOutList(Churn_ft)
	tmp+= "Churn bug &"+writeOutList(Churn_bugs)
	tmp+= "\n\\end{tabular} \n \label{corr:WIP} \n \caption{Correlation - WIP} \n "
	tmp+= "\\centerline {* Correlation is significant at the 0.05 level (2-tailed).} \n"
	tmp+= "\\centerline{** Correlation is significant at the 0.01 level (2-tailed).} \n"
	tmp+= "\\centerline{c. Cannot be computed because at least one of the variables is constant.} \n"
	tmp+= "\\end{table}  \n\n"
	
	print tmp




with open(sys.argv[1], mode="r") as three:
	with open(sys.argv[2], mode="r") as Neon:
		with open(sys.argv[3], mode="r") as Frontend:
			with open(sys.argv[4], mode="r") as IT:
				with open(sys.argv[5], mode="r") as Argon:
					with open(sys.argv[6], mode="r") as Automation:
						input = str(raw_input())
							

						

						for line in three.readlines():
							if input in line:
								if "Pearson Correlation" in line:
									line = line.split(",")
									line = line[2:]
									makeFloat(line)
									diagonal_data(line, 0)
							
						for line in Neon.readlines():
							if input in line:
								if "Pearson Correlation" in line:
									line = line.split(",")
									line = line[2:]
									makeFloat(line)
									diagonal_data(line, 0)


						for line in Frontend.readlines():
							if input in line:
								if "Pearson Correlation" in line:
									line = line.split(",")
									line = line[2:]
									makeFloat(line)
									diagonal_data(line, 0)

						for line in IT.readlines():
							if input in line:
								if "Pearson Correlation" in line:
									line = line.split(",")
									line = line[2:]
									makeFloat(line)
									diagonal_data(line, 0)

						for line in Argon.readlines():
							if input in line:
								if "Pearson Correlation" in line:
									line = line.split(",")
									line = line[2:]
									makeFloat(line)
									diagonal_data(line, 0)


						for line in Automation.readlines():
							if input in line:
								if "Pearson Correlation" in line:
									line = line.split(",")
									line = line[2:]
									makeFloat(line)
									diagonal_data(line, 0)

							


writeToFile()
				
