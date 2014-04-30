three = []
Argon= []
Automation= []
front = []
IT = []
Krypton= []
Neon= []
ProArc= []
Radon= []
Xenon= []
quarter =[None]*15
quarter[0]= "2010-3"
quarter[1]="2010-4"
quarter[2]="2011-1"
quarter[3]="2011-2"
quarter[4]="2011-3"
quarter[5]="2011-4"
quarter[6]="2012-1"
quarter[7]="2012-2"
quarter[8]="2012-3"
quarter[9]="2012-4"
quarter[10]="2013-1"
quarter[11]="2013-2"
quarter[12]="2013-3"
quarter[13]="2013-4"
quarter[14]="Mean"


import sys
import xlrd


def printOut(list):
	tmp = "NEW \n"
	tmp+="\\begin{tabular}{ | r | r |}\n \\hline \n"
	tmp+= "\\bf{Year - Quarter} & \\bf{TP} \\\\ \\hline\n" 
	for nr, i in enumerate(list):
		temp = str(i)
		temp = temp.split(":")[1]
		try:
			num = float(temp)
			tmp += quarter[nr]+"& "+temp+"\\\\ \\hline \n"
		except:
			halo = 1
	print tmp +"\n"



with open(sys.argv[1],"r") as source:
	wb = xlrd.open_workbook('TP_per_worker.xlsx')
	worksheet = wb.sheet_by_name('Sheet1')
	num_rows = worksheet.nrows - 1
	curr_row = -1
	while curr_row < num_rows:
		curr_row += 1
		row = worksheet.row(curr_row)
		three.append(row[0])
		Argon.append(row[1])
		Automation.append(row[2])
		front.append(row[3])
		IT.append(row[4])
		Krypton.append(row[5])
		Neon.append(row[6])
		ProArc.append(row[7])
		Radon.append(row[8])
		Xenon.append(row[9])
		print row

	printOut(three)
	printOut(Argon)
	printOut(Automation)
	printOut(front)
	printOut(IT)
	printOut(Krypton)
	printOut(Neon)
	printOut(ProArc)
	printOut(Radon)
	printOut(Xenon)




