import sys
import numpy as np

def circle_val(x,y):
    result = x*x + y*y - 5
    return result > 0

def main(argv):
    for xval in np.linspace(-3, 3, num=50):
        for yval in np.linspace(-3, 3, num=50):
            if circle_val(xval, yval):
                print('{},{},{}'.format(xval,yval,1))
            else:
                print('{},{},{}'.format(xval,yval,0))

if __name__ == "__main__":
    main(sys.argv)
