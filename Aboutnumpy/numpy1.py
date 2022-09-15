#installing pip https://phoenixnap.com/kb/install-pip-windows
#installing numpy https://phoenixnap.com/kb/install-numpy

import numpy as np
import sys
import time

def createNumpArr():
    """
    creating an array using numpy
    """
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
    return 

def reshep():
    """
    re arrange rows and column
    """
    shepR = np.array([(1,2,3,5),(3,4,5,77),(5,6,7,43)])
    shep()
    #lets rearrange
    shepR = shepR.reshape(4, 3)
    values = np.array(shepR.shape)
    print("now we have {} columns and {} rows".format(values[0], values[1]))
def randValues():
    """
    give random values in array form
    linspace(1st value, 2nd value, number of values)
    """
    b = np.linspace(1,2,6)
    c = np.linspace(1,5,12)
    print("between 1 and 2 : {}".format(b))
    print("between 1 and 5 : {}".format(c))
def maxVal():
    """
    find maximum value in an array
    """
    a = np.arange(100)
    maxVal = a.max()
    print("for elements in the array\n\t {}\n the largest value is {}".format(a, maxVal))

def minVal():
    """
    find minimum value in an array
    """
    a = np.arange(100)
    minVal = a.min()
    print("for elements in the array\n\t {}\n the largest value is {}".format(a, minVal))

def sumVal():
    """
    find minimum value in an array
    """
    a = np.arange(100)
    sumVal = a.sum()
    print("for elements in the array\n\t {}\n the sum of values is {}".format(a, sumVal))

def sumAxis():
    """
    colums:axis 0, rows axis:1
    computes sum on each axis
    """
    valu = np.array([(1,2,3),(3,4,5)])
    print("sum on columns is : {}".format(valu.sum(axis=0)))
    print("sum on rows is : {}".format(valu.sum(axis=1)))

def squareR():
    """
        find squar_root of elements in an array
    """
    valu = np.array([(4,16,25),(9,100,121)])
    print("the square root of values are : {}".format(np.sqrt(valu)))

def stndDev():
    """
        standard deviation
        give the difference bwn mean and elements
    """
    valu = np.array([(4,16,25),(9,100,121)])
    print("the standard deviation of value are : {}".format(np.std(valu)))

def sumArrays():
    """
        sums elements of 2 arrays
    """
    valu1 = np.array([(1,2,3),(3,4,5)])
    valu2 = np.array([(4,16,25),(9,100,121)])
    print("the sum of array val 1&2 is: {}".format(valu1+valu2))
    
def subArrays():
    """
        subtracts elements of 2 arrays
    """
    valu1 = np.array([(1,2,3),(3,4,5)])
    valu2 = np.array([(4,16,25),(9,100,121)])
    print("the subtraction of array val 1&2 is: {}".format(valu1-valu2))

def multArrays():
    """
        multiply elements of 2 arrays
    """
    valu1 = np.array([(1,2,3),(3,4,5)])
    valu2 = np.array([(4,16,25),(9,100,121)])
    print("the multiplication of array val 1&2 is: {}".format(valu1*valu2))
def divArrays():
    """
        divide elements of 2 arrays
    """
    valu1 = np.array([(1,2,3),(3,4,5)])
    valu2 = np.array([(4,16,25),(9,100,121)])
    print("the divition of array val 1&2 is: {}".format(valu1/valu2))






