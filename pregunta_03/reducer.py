#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__=="__main__":
    for line in sys.stdin:
        line = line.replace("\n","")
        if '*' in line:
            print(line.split("*")[1]+ "," +line.split("*")[0])