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
Team = []

def diagonal_data(list, index):
	WIP.append(list[0])

	Throughput.append(list[1])
	Throughput_ft.append(list[2])
	Throughput_bug.append(list[3])

	precent_bugs.append(list[4])
	Average_days_in_backlog_bugs.append(list[5])
	leadtime.append(list[6])


	Churn.append(list[7])
	Churn_ft.append(list[8])
	Churn_bugs.append(list[9])
	Team.append(list[10])
	print list[10]

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
		del list[index]
	

def writeOutList(list):
	temp = " "
	for l in list:
		temp +=str(l)+"& "
	temp = temp.strip()
	temp = temp[:-1] #need to remove the last &
	temp +="\\\\ \\hline \n"
	return temp
def writeOutList_new(list):
	temp = " "
	for l in list:
		temp +=str(l)+"\n"
	temp = temp.strip()
	temp = temp[:-1] #need to remove the last &
	return temp
def formatItem(item):
	if "*" in item:
		if "-" in item:
			item = "-0"+item.split("-")[1]
			return item.split("*")[0] 
		else:
			return "0"+item.split("*")[0]
	elif "c" in item:
		return "0"
	else:
		return item



def writeToFile():
	tmp = "\\begin{table}[!htbp] \n \centering \n \\begin{tabular}{|l|r|r|r|r|r|r|r|r|r|r|} \n\\hline \n"
	tmp+=" &  \\bf{T1} & \\bf{T2} & \\bf{T3} & \\bf{T4} & \\bf{T5} & \\bf{T6} & \\bf{T7} & \\bf{T8} & \\bf{T9} & \\bf{T10}\\\\ \\hline\n"
	tmp+= "WIP &"+writeOutList(WIP)
	tmp+= "Throughput &"+ writeOutList(Throughput)
	tmp+= "Throughput Feature &" + writeOutList(Throughput_ft)
	tmp+= "Throughput bug &"+writeOutList(Throughput_bug)
	tmp+= "Bugs finished, quarter &"+writeOutList(precent_bugs)
	tmp+= "Avg days in backlog, bugs &"+writeOutList(Average_days_in_backlog_bugs)
	tmp+= "Leadtime &" + writeOutList(leadtime)
	tmp+= "Churn &"+writeOutList(Churn)
	tmp+= "Churn feature &" + writeOutList(Churn_ft)
	tmp+= "Churn bug &"+writeOutList(Churn_bugs)
	tmp+= "Team size & "+ writeOutList(Team)
	tmp+= "\n\\end{tabular} \n \caption{Correlation - Leadtime} \n \label{corr:WIP} \n "
	tmp+= "\\centerline {* Correlation is significant at the 0.05 level (2-tailed).} \n"
	tmp+= "\\centerline{** Correlation is significant at the 0.01 level (2-tailed).} \n"
	tmp+= "\\centerline{c. Cannot be computed because at least one of the variables is constant.} \n"
	tmp+= "\\end{table}  \n\n"
	
	print tmp
def writeToDS():
	tmp = 'WIP, Throughput, Throughput_ft, Throughput_bug, precent_bugs, Average_days_in_backlog_bugs, leadtime, Churn, Churn_ft, Churn_bugs, Team_size\n'
	for i in xrange(len(Throughput)):
		tmp += formatItem(WIP[i]) + ", " + formatItem(Throughput[i]) + ", "+formatItem(Throughput_ft[i])+","+formatItem(Throughput_bug[i])+","+formatItem(precent_bugs[i])+","+formatItem(Average_days_in_backlog_bugs[i])+","+formatItem(leadtime[i])+","+formatItem(Churn[i])+","+formatItem(Churn_ft[i])+","+formatItem(Churn_bugs[i])+formatItem(Team[i])+"\n"
	with open('output.csv', 'w') as f:
		f.write(tmp)






with open(sys.argv[1],mode="r") as three:
	with open(sys.argv[2],mode="r") as Neon:
		with open(sys.argv[3], mode="r") as Frontend:
			with open(sys.argv[4], mode="r") as IT:
				with open(sys.argv[5], mode="r") as Argon:
					with open(sys.argv[6], mode="r") as Automation:
						with open(sys.argv[7], mode="r") as Krypton:
							with open(sys.argv[8], mode="r") as ProArc:
								with open(sys.argv[9], mode="r") as Radon:
									with open(sys.argv[10], mode="r") as Xenon:

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

										for line in Krypton.readlines():
											if input in line:
												if "Pearson Correlation" in line:
													line = line.split(",")
													line = line[2:]
													makeFloat(line)
													diagonal_data(line, 0)


										for line in ProArc.readlines():
											if input in line:
												if "Pearson Correlation" in line:
													line = line.split(",")
													line = line[2:]
													makeFloat(line)
													diagonal_data(line, 0)

										for line in Radon.readlines():
											if input in line:
												if "Pearson Correlation" in line:
													line = line.split(",")
													line = line[2:]
													makeFloat(line)
													diagonal_data(line, 0)

										for line in Xenon.readlines():
											if input in line:
												if "Pearson Correlation" in line:
													line = line.split(",")
													line = line[2:]
													makeFloat(line)
													diagonal_data(line, 0)
writeToFile()
writeToDS()

											


				
