import sys
import matplotlib.pyplot as plt

def read_line(line):
    line = line.strip()
    parts = line.split(',')
    return float(parts[0]), float(parts[1]), int(parts[2])
def main(argv):
    x_1 = []
    y_1 = []
    x_0 = []
    y_0 = []
    with open(argv[1], 'r') as in_file:
        for line in in_file:
            x,y,val = read_line(line)
            if val == 1:
                x_1.append(x)
                y_1.append(y)
            else:
                x_0.append(x)
                y_0.append(y)
        plt.scatter(x_0, y_0, color='blue', marker='+')
        plt.scatter(x_1, y_1, color='red', marker='x')
        plt.show()

if __name__ == "__main__":
    main(sys.argv)
