# Learning from data

cited from: _IPython Interactive Computing and Visualization Cookbook_
                        _Chapter 8: Machine Learning_
                               Packt Publishing
                        
In machine learning, most data can be represented as a _table of numerical values_.
Every _row_ is called an __observation__, a __sample___, or a __data point___.
Every _column_ is called a __feature__ or a __variable__.

Let's call _N_ the number of rows (or the number of points) and _D_ the number of columns
(or number of features). The number _D_ is also called the __dimensionality__ of the data.
The reason is that we can view this table as a set _E_ of __vectors__ in a space with _D_
dimensions (or __vector space__). Here, a vector __x__ contains _D_ numbers (<code>X<sub>1</sub></code>,....,<code>X<sub>D</sub></code>),
also called __components__.

We generally make the distinction between supervised learning and unsupervised learning:
* __Supervised learning__ is when we have a __label__ _y_ associated with a data point _x_.
  The goal is to _learn_ the mapping from _x_ to _y_ from our data. The data give us this mapping
  for a finite set of points, but what we want is to _generalize_ this mapping to the full set _E_.
  
* __Unsupervised learning__ is when we don't have any labels. What we want to do is discover some form
  of hidden structure in the data.
