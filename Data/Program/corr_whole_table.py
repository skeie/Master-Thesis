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
	print list, index
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
	Churn_average.append(list[10])


with open(sys.argv[1], mode="r") as fOne:
	with open(sys.argv[2], mode="r") as fTwo:
		#out = open(sys.argv[2], mode="w")
		tmp = "T1 & T2 & T3 & T4 & T5 & T6 \\\\ \\hline \n"
		firstLine = [x.strip() for x in fOne.readline().split("&")]
		firstLineTwo = [x.strip() for x in fTwo.readline().split("&")]


		for line in fOne.readlines():
			if "WIP" in line:
				line = line.split("&")
				line = line[2:]
				diagonal_data(line, 0)
				print line

		for line in fTwo.readlines():
			if "WIP" in line:
				line = line.split("&")
				line = line[2:]
				diagonal_data(line, 1)
				
