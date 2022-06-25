#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def clear_spaces(x):
    x = x.replace("\n", "")
    x = x.replace("\r", "")
    return x

def purpose_column(x):
    return clear_spaces(x[1].split("-")[1])

if __name__=="__main__":
    for line in sys.stdin:
        line = line.replace("'","")
        result = line.split('   ')
        print(purpose_column(result))