import sys
team1Nr = 0
team1 = 0
team2Nr = 0
team2 = 0
team3Nr = 0
team3= 0
team4Nr = 0
team4 = 0
team5Nr = 0
team5 = 0
team6Nr = 0
team6 = 0
team7Nr = 0
team7 = 0
team8Nr = 0
team8 = 0
team9Nr = 0
team9 = 0
team10Nr = 0
team10 = 0

with open(sys.argv[1], mode="r") as f:
	list = f.readlines()
	for l in list:
		lines = l.split(",")
		if lines[2].strip() == "360":
			team1Nr += int(lines[3])
			team1+=1
		elif lines[2].strip() == "Neon":
			team2Nr += int(lines[3])
			team2+=1
		elif lines[2].strip() == "Frontend":
			team3Nr += int(lines[3])
			team3+=1
		elif lines[2].strip() == "IT":
			team4Nr += int(lines[3])
			team4+=1
		elif lines[2].strip() == "Argon":
			team5Nr += int(lines[3])
			team5+=1

		elif lines[2].strip() == "Automation":
			team6Nr += int(lines[3])
			team6+=1

		elif lines[2].strip() == "Deleted team Krypton":
			team7Nr += int(lines[3])
			team7+=1

		elif lines[2].strip() == "ProArc":
			team8Nr += int(lines[3])
			team8+=1

		elif lines[2].strip() == "Radon":
			team9Nr += int(lines[3])
			team9+=1

		elif lines[2].strip() == "Xenon":
			team10Nr += int(lines[3])
			team10+=1
tmp = "Team one & "+str((team1Nr/team1))+" &  \\\\ \\hline \n"
tmp += "Team two & "+str((team2Nr/team2))+" &  \\\\ \\hline\n"
tmp += "Team three & "+str((team3Nr/team3))+" &  \\\\ \\hline\n"
tmp += "Team four & "+str((team4Nr/team4))+" &  \\\\ \\hline\n"
tmp += "Team five & "+str((team5Nr/team5))+" &  \\\\ \\hline\n"
tmp += "Team six & "+str((team6Nr/team6))+" &  \\\\ \\hline\n"
tmp += "Team seven & "+str((team7Nr/team7))+" &  \\\\ \\hline\n"
tmp += "Team eight & "+str((team8Nr/team8))+" &  \\\\ \\hline\n"
tmp += "Team nine  & "+str((team9Nr/team9))+" &  \\\\ \\hline\n"
tmp += "Team ten & "+str((team10Nr/team10))+" &  \\\\ \\hline\n"
print tmp

