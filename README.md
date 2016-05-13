Playing around with TFLearn(Tensor Flow) for some simple 2D cases
==================================================================

Circle
-------
* Create circle data
    $ python circle.py > circle_data.csv
* Visualize the circle
    $ python visualize.py circle_data.csv
* Run Deep Learning on data
    $ python train circle_dl.py circle_data.csv
* Create predicted data 
    $ python circle_dl.py predict circle_data.csv circle_predicted.csv
* Visualize predicted data
    $ python visualize.py circle_predicted.csv

We are seeing an accuracy of 98.24% in predicting circle data.

Complicated
------------
* Create complicated data
    $ python complicated.py > complicated_data.csv
* Visualize complidated data
    $ python visualize.py complicated_data.csv
* Run Deep Learning on data
    $ python complicated_dl.py train complicated_data.csv
* Create predicted data
    $ python complicated_dl.py predict complicated_data.csv complicated_predicted.csv
* Visualize predicted data
    $ python visualize.py complicated_predicted.csv

We are seeing an accuracy of 95.64% in predicting complidated data.

Complicated1
------------
* Create complicated data
    $ python complicated1.py > complicated1_data.csv
* Visualize complidated data
    $ python visualize.py complicated1_data.csv
* Run Deep Learning on data
    $ python complicated1_dl.py train complicated1_data.csv
* Create predicted data
    $ python complicated1_dl.py predict complicated1_data.csv complicated1_predicted.csv
* Visualize predicted data
    $ python visualize.py complicated1_predicted.csv

We are seeing an accuracy of 98.08% in predicting complidated data.

Resources
---------
* [TFLearn](http://tflearn.org)
* [TensorFlow](http://tensorflow.org)
* [Deep Learning Book](http://www.deeplearningbook.org/)
