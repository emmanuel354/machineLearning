#installing pip https://phoenixnap.com/kb/install-pip-windows
#installing numpy https://phoenixnap.com/kb/install-numpy

import numpy as np
import sys
import time

def createNumpArr():
    a = np.array([(1,2,3,4,5), (6,7,8,9, 10)])
    print(a)
    
def numpySpaceTest(x):
    """
        this is a test to see how numpy is more convinent
        than list interms of space
    """
    # lets see how fast numpy is compared to list
    s = range(x)
    #space occupied by list(multiply size occpied by one element by number of elemets)
    print("space occupied by list: {}".format(sys.getsizeof(5)*len(s)))
    #create numpy arrays and see size
    d = np.arange(x)
    print("space occupied by numpy array: {}".format(d.size*d.itemsize))
def numpTimeTest():
    """
        compares computing time for list and arrays
    """
    s = 1000000
    list1 = range(s)
    list2 = range(s)

    A1 = np.arange(s)
    A2 = np.arange(s)

    start = time.time()
    #sum list
    result = [(x,y) for x,y in zip(list1, list2)]
    #time list, time is converted to nano seconds
    print("time taken for list : {}".format((time.time()-start)*1000))
    #sum numpy
    start = time.time()
    result = A1+A2
    print("time taken for numpy : {}".format((time.time()-start)*1000))
def dimType():
    """
    check on the number of dimensions
    """
    dim = np.array([(1,2,3),(3,4,5),(5,6,7)])
    print("dim is an {} dimensional array".format(dim.ndim))
def elementSiz():
    """
    check size on numpy
    """
    s = np.array([(1,2,3),(3,4,5),(5,6,7)])
    print("each element occupies {} bytes".format(s.itemsize))

def elem():
    """
    check number of elements
    """
    num = np.array([(1,2,3),(3,4,5),(5,6,7)])
    print("the number of elements in the array num is {}".format(num.size))

def shep():
    """
    numbers of columns to rows
    """
    shep = np.array([(1,2,3,5),(3,4,5,77),(5,6,7,43)])
    values = np.array(shep.shape)
    print("the number of columns is {} rows are {}".format(values[0], values[1]))


