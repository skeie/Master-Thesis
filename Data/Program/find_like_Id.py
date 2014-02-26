import sys

class Line(object):
	startDate =""
	endDate=""
	leadtime=""
	counter=1

	def __init__ (self, startDate, endDate, leadtime):
		self.startDate = startDate
		self.endDate = endDate
		self.leadtime = leadtime

def make_line(startDate, endDate, leadtime):
	l = Line(startDate, endDate, leadtime)
	l.startDate = startDate
	l.endDate = endDate
	l.leadtime = leadtime
	return l 



id_leadtime = {}
with open(sys.argv[1], mode="r") as f:
    out = open(sys.argv[2], mode="w")
    for line in f.readlines():
    	temp = line.split(",")
    	if temp[0] in id_leadtime:
    		obj = make_line(temp[5], temp[13], temp[20])
    		id_leadtime[temp[0]].counter+=1
    		tmp = "ID: "+temp[0]+"\n" 
    		tmp+= "First: created date: "+id_leadtime[temp[0]].startDate + " end date: "+id_leadtime[temp[0]].endDate + " leadtime: "+id_leadtime[temp[0]].leadtime+"\n"
    		tmp+= "last: created date: "+obj.startDate + " end date: "+obj.endDate + " leadtime: "+obj.leadtime+"\n\n"
    		tmp+="-------------------------------------------------------\n"
    		out.write(tmp)
    	else:
    		obj = make_line(temp[5], temp[13], temp[20])
    		id_leadtime[temp[0]] = obj
    out.close()

