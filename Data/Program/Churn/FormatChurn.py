import sys
tree60 = []
Neon = []
Frontend = []
it = []
argon = []
automation = []
krypton  = []
proarc = []
radon = []
xenon = []
new_list =[]

class Line(object):
	BorFT = ""
	churn = 0
	leadtime = 0
	team = ""
	date =""
	q = ""
	def __init__(self, BorFT, churn, leadtime, team,date,q):
		self.BorFT = BorFT
		self.churn = churn
		self.leadtime = leadtime
		self.team = team
		self.date = date
		self.q = q

def make_line(BorFT, churn, leadtime, team, lst, date,q):
    lne = Line(BorFT, churn, leadtime, team, date,q)
    lst.append(lne)
def test(lst, line):
	for l in lst:
		if line[5] == l.date:
			if line[6] == l.BorFT:
				int(l.churn)+=int(line[2])
				int(l.leadtime)+=int(line[3])

	make_line(line[6], line[2], line[3], line[1], lst, line[5], line[4])




with open(sys.argv[1], mode="r") as f:
	out = open("output.csv", "w")

	counter = 0
	for l in f.readlines():
		lines = l.split(",")
		if lines[1].strip() == "360":
			test(tree60, lines)
		elif lines[1].strip() == "Neon":
			test(Neon, lines)
		elif lines[1].strip() == "Frontend":
			test(Frontend, lines)
		elif lines[1].strip() == "IT":
			test(it, lines)
		elif lines[1].strip() == "Argon":
			test(argon, lines)

		elif lines[1].strip() == "Automation":
			test(automation, lines)

		elif lines[1].strip() == "Krypton":
			test(krypton, lines)

		elif lines[1].strip() == "ProArc":
			test(proarc, lines)

		elif lines[1].strip() == "Radon":
			test(radon, lines)

		elif lines[1].strip() == "Xenon":
			test(xenon, lines)
	new_list = tree60+Neon+Frontend+it+argon+automation+krypton+proarc+radon+xenon
	for l in new_list:
		tmp = l.BorFT+","+l.churn+","+l.leadtime+","+l.team+","+l.date+","+l.q
		out.write(tmp)
	out.close()