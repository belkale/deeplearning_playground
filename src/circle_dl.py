import sys
import numpy as np
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression

import utils

def build_network():
    network = tflearn.input_data(shape=[None, 2])
    network = tflearn.fully_connected(network, 64, activation='relu', regularizer='L2', weight_decay=0.001)
    network = tflearn.fully_connected(network, 1, activation='sigmoid')
    network = tflearn.regression(network, optimizer='sgd', learning_rate=0.3,
                           loss='mean_square')
    return network

def train(in_file):
    xvals, yvals = utils.load_data(in_file)
    xvals, yvals = utils.randomize(xvals, yvals)
    network = build_network()
    model = tflearn.DNN(network)
    model.fit(xvals, yvals, n_epoch=200, validation_set=0.2)
    model.save('circle.tflearn')

def predict(in_file, out_file):
    xvals, yvals = utils.load_data(in_file)
    network = build_network()
    predictions = utils.predict(xvals, network, 'circle.tflearn')
    print('Accuracy: {}%'.format(utils.get_accuracy(yvals, predictions)))
    utils.write_predictions(xvals, predictions, out_file)

def main(argv):
    if argv[1] == 'train':
        train(argv[2])
    elif argv[1] == 'predict':
        predict(argv[2], argv[3])
    else:
        raise ValueError('Unknown operation {}'.format(argv[1]))

if __name__ == "__main__":
    main(sys.argv)
