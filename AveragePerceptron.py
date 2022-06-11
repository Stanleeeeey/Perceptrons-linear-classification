import numpy as np


def avarage_perceptron(points, labels, T):

    #sums of theta and theta_0 to calculate the average
    sum_theta   = np.zeros(points.shape[1],)
    sum_theta_0 = 0

    #initliazing theta and theta_0
    theta   = np.zeros(points.shape[1],)
    theta_0 = 0

    #counter of all thetas and thetas_0
    count = 0

    for t in range(T):

        for i in range(points.shape[0]):

            #single percepton step
            if labels[i]*(points[i]@theta + theta_0) <= 0.0000001:
                theta, theta_0 = theta+labels[i]*points[i], theta_0+labels[i]

            #increasing sum of theta, theta_0 and count 
            sum_theta   +=theta
            sum_theta_0 +=theta_0
            
            count+=1

    #calculating the average based on sum_theta, sum_theta_0, count
    return (sum_theta/count, sum_theta_0/count)