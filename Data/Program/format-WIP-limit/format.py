Combine = []
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



import sys
import xlrd


def printOut(list):
	tmp = "NEW \n"
	tmp+="\\begin{tabular}{ | r | r |}\n \\hline \n"
	tmp+= "\\bf{Year - Quarter} & \\bf{WIP-limit} \\\\ \\hline\n" 
	for i in list:
		temp = str(i)
		temp = temp.split(":")[1]
		try:
			num = float(temp)
			tmp += "& "+temp+"\\\\ \\hline \n"
		except:
			halo = 1
	print tmp +"\n"



with open(sys.argv[1],"r") as source:
	wb = xlrd.open_workbook('Avg_WIP.xlsx')
	worksheet = wb.sheet_by_name('Sheet1')
	num_rows = worksheet.nrows - 1
	curr_row = -1
	while curr_row < num_rows:
		curr_row += 1
		row = worksheet.row(curr_row)
		Combine.append(row[0])
		three.append(row[1])
		Argon.append(row[2])
		Automation.append(row[3])
		front.append(row[4])
		IT.append(row[5])
		Krypton.append(row[6])
		Neon.append(row[7])
		ProArc.append(row[8])
		Radon.append(row[9])
		Xenon.append(row[10])
		print row

	printOut(Combine)
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




