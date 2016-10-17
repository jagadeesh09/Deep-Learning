


import theano.tensor as T



def ReLu(x):

    """ ReLu(x) = max(0,x) """
    
    return T.nnet.relu(x)

def sigmoid(x):

    """sigmoid function is 1/1+exp(-x)"""
    
    return 1/(1+T.exp(-x)

def tanh(x):
    
    return T.tanh(x)
    

def softmax(x):
    """ X is a two dimensional tensor and it calculates row wise"""
              
    return T.nnet.softmax(x)
              

