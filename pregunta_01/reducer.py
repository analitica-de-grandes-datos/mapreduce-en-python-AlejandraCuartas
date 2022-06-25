#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
biggest_purposes = {}

def set_bigger_purpose(dictionary_purposes, actual_element):
    dictionary_purposes[actual_element] = int(dictionary_purposes.get(actual_element) or 0)  +1 
    return dictionary_purposes


if __name__=="__main__":
    for line in sys.stdin:
        set_bigger_purpose(biggest_purposes, line.replace("\n", ""))

    for purpose, amount in biggest_purposes.items():
        print(purpose + "	" + str(amount))