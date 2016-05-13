import sys
import math
import numpy as np

def complicated_val(x,y):
    result = x + x*math.sin(x) - 3 - y
    return result > 0

def main(argv):
    for xval in np.linspace(-1, 10, num=50):
        for yval in np.linspace(-8, 15, num=50):
            if complicated_val(xval, yval):
                print('{},{},{}'.format(xval,yval,1))
            else:
                print('{},{},{}'.format(xval,yval,0))

if __name__ == "__main__":
    main(sys.argv)
