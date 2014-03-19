import sys
import csv
import xlrd
idList =[]

def unicodeList(list):
	new_list = []
	for i, t in enumerate(list): 
		if isinstance(t, float):
			new_list.append(str(t).encode('utf-8'))
		else:
	  		new_list.append(t.encode('utf-8'))
	return new_list




def csv_from_excel():

    wb = xlrd.open_workbook(sys.argv[1])
    sh = wb.sheet_by_name("Scrum & Kanban Data")
    your_csv_file = open('your_csv_file.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
    	if sh.row_values(rownum)[0] != idList:
    		if sh.row_values(rownum)[22] != " ":
    			if sh.row_values(rownum)[22] != "":
					tmp =  sh.row_values(rownum)
					tmp = unicodeList(tmp)
					wr.writerow(tmp)
					idList.append(sh.row_values(rownum)[0])

	       



with open(sys.argv[1],"rb") as source:
    csv_from_excel()
    with open('your_csv_file.csv', 'rb') as csvfile:
	    rdr= csv.reader(csvfile)
	    with open("result.csv","wb") as result:
	        wtr= csv.writer( result )
	        for r in rdr:
	            wtr.writerow( (str(r[0]), r[1], r[5], r[8],r[11],r[22],r[24],r[25],r[26], r[29]) )