import sys
import math
import numpy as np

def complicated_val(x,y):
    val1 = (x-3)*(x-3) + (y+4)*(y+4) + y*math.sin(x) - 16
    val2 = (x+4)*(x+4) + (y-2)*(y-2) + x*math.cos(y) - 9
    if val1 < 0 or val2 < 0:
        return True
    else:
        return False

def main(argv):
    for xval in np.linspace(-10, 10, num=50):
        for yval in np.linspace(-10, 10, num=50):
            if complicated_val(xval, yval):
                print('{},{},{}'.format(xval,yval,1))
            else:
                print('{},{},{}'.format(xval,yval,0))

if __name__ == "__main__":
    main(sys.argv)
