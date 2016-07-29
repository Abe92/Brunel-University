Mathematically, __supervised learning__ consists of finding a function _f_ that maps the set of points
_E_ to a set of labels _F_, knowing a finite set of associations (_x_,_y_), which is given by our data.
This is what _generalization_ is about: after observing the pairs (<code>x<sub>i</sub></code>, <code>y<sub>i</sub></code>,
given we are able to find the corresponding _y_ by applying the function _f_ to _x_.

It is a common practice to split the set of data points into two subsets: the __training set__ and the __test set__.
We learn the function _f_ on the training set and test it on the test set. This is essential when assessing the predictive
power of a model. By training and testing a model on the same set, our model might not be able to generalize well. This is the
fundamental concept of __overfitting__.

Two particular instances of _supervised learning_ :

__Classification__ is when our labels _y_ can only take a finite set of values (categories).
Examples include:
* __Handwritten digit recognition__: x is an image with a handwritten digit; _y_ is a digit between 0 and 9
* __Spam filtering__ :x is an e-mail and _y_ is 1 or 0, depending on whether that e-mail is spam or not

__Regression__ is when our labels _y_ can take any real (continous) value.
Examples include:
* Predicting stock market data
* Predicting sales
* Detecting the age of a person from a picture
