import sys
import csv
with open(sys.argv[1],"rb") as source:
    rdr= csv.reader( source )
    with open("result","wb") as result:
        wtr= csv.writer( result )
        for r in rdr:
            wtr.writerow( (r[0], r[1], r[5], r[8],r[11],r[20],r[22],r[23],r[24],r[27]) )