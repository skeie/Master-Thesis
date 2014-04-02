import sys
TP =[]
TP_B =[]
TP_FT = []
Bug_new =[]
FT_new = []
B_sum = 0
TP_sum = 0
Quarter =["2010-3","2010-4","2011-1",
"2011-2","2011-3","2011-4","2012-1",
"2012-2","2012-3","2012-4","2013-1",
"2013-2","2013-3","2013-4"]

def measure():
	tmp = 0
	for l in TP:
		l = l.split("&")
		tmp += int(l[2].split("\\")[0])
	print "Total &", tmp," \\\\ \\hline"

def writeOut():
	tmp = "\\begin{table}[!htbp] \n \centering \n \\begin{tabular}{|l|r|r|} \n \\hline"
	tmp+="\n Quarter& Bug & Feature \\\\ \\hline\n"
	for i,e in enumerate(Bug_new):
		tmp += Quarter[i]+" & " +str(Bug_new[i][0])+" & "+str(FT_new[i][0])+"\\\\ \\hline \n"
	tmp+="Total & "
	tmp+= "\n\\end{tabular} \n \caption{Difference between throughput for team eight} \n \label{DS:Difference} \n "
	tmp+= "\\end{table}  \n\n"
	print tmp


with open(sys.argv[1], mode="r") as T:
	TP = T.readlines()
	measure()

			
			