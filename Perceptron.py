import numpy as np
import math


def perceptron(points, labels, epochs):

    theta  = np.zeros(2) #creating theta [0,0] 
    theta_0 = np.zeros(1) #creating theta_0 [0]

    for i in range(epochs): #iterating number of requested epochs

        for i in range(len(labels)): 

            if labels[i]*(points[i]@theta + theta_0) <= 0: 
                theta  += labels[i]*points[i]
                theta_0 += labels[i]

    return theta, theta_0 

