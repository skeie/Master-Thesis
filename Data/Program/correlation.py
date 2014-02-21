import sys

def swag(tekst, i):
    if len(tekst[i]) > 1:
        return i
    else:
        swag(tekst, i+1)


def removeHline(text):
    if "\\\\ \hline" in text:
        text = text[:-10]
    return text



def findStar(list):
    for i,element in enumerate(list):
        if "*" in element:
            index.append(i)
            elements.append(element)
def colums():
    text =""
    for element in elements:
        text+="|l"
    return text
            

firstLine = None
current = None
index = []
elements = []
with open(sys.argv[1], mode="r") as f:
    out = open(sys.argv[2], mode="w")
    firstLine = [x.strip() for x in f.readline().split("&")]
    for line in f.readlines():
        cols = line.split(" & ")
        findStar(cols)
        for i, col in enumerate(cols):
            if len(index) > 0:
                t = colums()
                tmp = "\\begin{table}[!htbp] \n \centering \n \\begin{tabular}{"+t+"|l|} \n\\hline \n"
                for a,i in enumerate(index):
                    if a == 0:
                        tmp+= "Correlation "
                       
                    first = firstLine[swag(firstLine, i)].split("\_")
                    fi = removeHline(' '.join(first))
                    tmp+=" & " + fi
                tmp +=" \\\\ \\hline \n"
                tmp += cols[0]


                for a, i in enumerate(elements):
                    tmp += " & " + i 
                tmp +=" \\\\ \\hline \n"
                tmp +="\n\\end{tabular} \n \caption{Team one - Correlation - "+cols[0]+"} \n \\end{table}  \n\n"
                out.write(tmp)
                index = []
                elements = []
out.close()
