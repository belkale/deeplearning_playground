Playing around with TFLearn(Tensor Flow) for some simple 2D cases
==================================================================

Here are the steps we follow
* Create data
* Visualize data
* Run Deep Learning on data
* Create predicted data 
* Visualize predicted data

Circle
-------

We are seeing an accuracy of 98.24% in predicting circle data.

    $ python circle.py > circle_data.csv
    $ python visualize.py circle_data.csv
    $ python train circle_dl.py circle_data.csv
    $ python circle_dl.py predict circle_data.csv circle_predicted.csv
    $ python visualize.py circle_predicted.csv

Complicated
------------
We are seeing an accuracy of 95.64% in predicting complidated data.

    $ python complicated.py > complicated_data.csv
    $ python visualize.py complicated_data.csv
    $ python complicated_dl.py train complicated_data.csv
    $ python complicated_dl.py predict complicated_data.csv complicated_predicted.csv
    $ python visualize.py complicated_predicted.csv


Complicated1
------------
We are seeing an accuracy of 98.08% in predicting complidated data.

    $ python complicated1.py > complicated1_data.csv
    $ python visualize.py complicated1_data.csv
    $ python complicated1_dl.py train complicated1_data.csv
    $ python complicated1_dl.py predict complicated1_data.csv complicated1_predicted.csv
    $ python visualize.py complicated1_predicted.csv


Resources
---------
* [TFLearn](http://tflearn.org)
* [TensorFlow](http://tensorflow.org)
* [Deep Learning Book](http://www.deeplearningbook.org/)
