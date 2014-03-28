import sys
TP =[]
TP_B =[]
TP_FT = []
Bug_new =[]
FT_new = []
B_sum = 0
TP_sum = 0


def measure():
	B_sum = 0
	TP_sum = 0
	for i, e in enumerate(TP):
		tmp = float(e)-float(TP_B[i].split("\\")[0])
		Bug_new.append(["%.1f" % tmp])
		B_sum+= tmp
		try:
			tmp = float(e)-float(TP_FT[i].split("\\")[0])
			FT_new.append(["%.1f" % tmp])
			TP_sum+= tmp
		except:
			FT_new.append("-")
	print B_sum,TP_sum
	writeOut()


def writeOut():
	tmp = "\\begin{table}[!htbp] \n \centering \n \\begin{tabular}{|r|r|} \n \\hline"
	tmp+="Bug & Feature \\\\ \\hline\n"
	for i,e in enumerate(Bug_new):
		tmp += str(Bug_new[i][0])+" & "+str(FT_new[i][0])+"\\\\ \\hline \n"
	tmp+=str(["%.1f" % B_sum]) +" & "+str(["%.1f" % TP_sum])
	tmp+= "\n\\end{tabular} \n \caption{Difference between throughput for team eight} \n \label{DS:Difference} \n "
	tmp+= "\\end{table}  \n\n"
	print tmp


with open(sys.argv[1], mode="r") as T:
	with open(sys.argv[2], mode="r") as B:
		with open(sys.argv[3], mode="r") as FT:	
			TP = T.readlines()
			TP_B = B.readlines()
			TP_FT = FT.readlines()
			measure()

			
			