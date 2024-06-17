---
layout: default
title: Exception and Errors
nav_order: 5
permalink: /pages/error&exception
---

# Errors and Exceptions

PySideExtn Library uses specific style for parameters passed to the methods. So its is common for the users to get errors due to wrong data type of info passed. So there are certain Specific Exception and ValueErrors raised. Below is the list of such Exceptions and their Reasons:



## Class : RoundProgressBar

### Exception

* **Wrong Data type Error**

Raised if the data type passed as an argument did not match the required. This error is raised by almost all of the methods in this class.



## Class : SpiralProgressBar

### Exceptions

* **Wrong Data type Errors**

Raised by **all the methods** of this class. Mainly due to wrong data type i.e. the method `setValue()` takes a `tuple` as parameter, but if you passed a `int` it raises this error. Example

```python
self.setValue(55)
```

 error raised:

``` python
Traceback (most recent call last):
  File "F:\Project\Major Projects\Project PySide2 Extensions\expt\SpiralProgressBar\exception.py", line 26, in <module>
    widget = MyWidget()
  File "F:\Project\Major Projects\Project PySide2 Extensions\expt\SpiralProgressBar\exception.py", line 18, in __init__
    self.spbN.setValue(55)
  File "F:\Project\Major Projects\Project PySide2 Extensions\expt\SpiralProgressBar\SpiralProgressBar.py", line 202, in setValue
    raise Exception("Value should be a Tuple and not " + str(type(value)))
Exception: Value should be a Tuple and not <class 'int'>
[Finished in 0.6s]
```



### ValueError

* **Tuple length more than number of Progress Bars**

In class spiral progress bar the basic idea to control each circular progress bar independently is achieved by passing a tuple. And so the length of the tuple is very important. If the tuple passed contain 5 element and if the spiral progress bar contain only 3 concentric progress bar, the 5 elements in the tuple does not make sense as the last two elements does not hold any meaning, this makes the program to throw an error.

Methods raising this error : All the method who accepts a tuple as a parameter.

* **Tuple length less than the number of Progress Bars**

Same meaning as the error raised above but vice-versa.



See: [Versions](version)

