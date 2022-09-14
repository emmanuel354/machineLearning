import numpy as np
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
    
