import random
import tflearn

def load_data(in_filename):
    with open(in_filename, 'r') as in_file:
        xvals = []
        yvals = []
        for line in in_file:
            line = line.strip()
            if line == '':
                continue
            parts = line.split(',')
            length = len(parts)
            inp_vals = [float(x) for x in parts[:length-1]]
            if parts[length - 1] == '0':
                result_vals = [0]
            else:
                result_vals = [1]
            xvals.append(inp_vals)
            yvals.append(result_vals)
        return xvals, yvals

def load_hot(in_filename):
    with open(in_filename, 'r') as in_file:
        xvals = []
        yvals = []
        for line in in_file:
            line = line.strip()
            if line == '':
                continue
            parts = line.split(',')
            length = len(parts)
            inp_vals = [float(x) for x in parts[:length-1]]
            if parts[length - 1] == '0':
                result_vals = [1,0]
            else:
                result_vals = [0,1]
            xvals.append(inp_vals)
            yvals.append(result_vals)
        return xvals, yvals

def load_xvals(in_filename):
    with open(in_filename, 'r') as in_file:
        xvals = []
        for line in in_file:
            line = line.strip()
            if line == '':
                continue
            parts = line.split(',')
            inp_vals = [float(x) for x in parts]
            xvals.append(inp_vals)
        return xvals

def randomize(xvals, yvals):
    length = len(xvals)
    indices = [i for i in range(length)]
    random.shuffle(indices)
    xvals = [xvals[i] for i in indices]
    yvals = [yvals[i] for i in indices]
    return xvals, yvals

def predict(xvals, network, model_file):
    model = tflearn.DNN(network)
    model.load(model_file)
    result = []
    for val in model.predict(xvals):
        if val[0] < 0.5:
            result.append(0)
        else:
            result.append(1)
    return result

def predict_hot(xvals, network, model_file):
    model = tflearn.DNN(network)
    model.load(model_file)
    result = []
    for val in model.predict(xvals):
        if val[0] > 0.5:
            result.append(0)
        else:
            result.append(1)
    return result

def write_predictions(xvals, predictions, out_filename):
    with open(out_filename, 'w') as out_file:
        for xrow,y in zip(xvals, predictions):
            xrow = [str(x) for x in xrow]
            xval = ','.join(xrow)
            out_file.write('{},{}\n'.format(xval,y))

def get_accuracy(yvals, predictions):
    correct = 0
    wrong = 0
    for actual, predicted in zip(yvals, predictions):
        if actual[0] == predicted:
            correct += 1
        else:
            wrong += 1
    accuracy = correct * 100/(correct + wrong)
    return accuracy

def get_accuracy_hot(yvals, predictions):
    correct = 0
    wrong = 0
    for actual, predicted in zip(yvals, predictions):
        if (actual[0] == 1 and predicted == 0) or \
            (actual[1] == 1 and predicted == 1):
            correct += 1
        else:
            wrong += 1
    accuracy = correct * 100/(correct + wrong)
    return accuracy
