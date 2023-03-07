import numpy as np
def openfile(filename):
    openedfile = open(filename)
    result = list()
    for line in openedfile:
        hold = line.split()
        if hold[5] == 'usage:':
            break
        hold = hold[11].split('=')[1].split(',')[0]
        hold = float(hold)
        result.append(hold)
    return np.array(result)
    
def caldis1(ls):
    result = list()
    for i in ls:
        result.append(abs(i - 0.95))
    return np.array(result)
    
def caldis2(ls):
    result = list()
    for i in ls:
        result.append(abs(i + 0.05))
    return np.array(result)
    