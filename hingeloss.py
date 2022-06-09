import numpy as np

def single_hinge_loss(point, label, theta, theta_0):
    #hinge loss of a single point 
    return max([0,1-label*(theta@point + theta_0)])

def hingeloss(Points, labels, theta, theta_0):
    #Average hinge loss in 'Points' set of points
    sum = 0
    for i in len(Points):
        sum+=single_hinge_loss(Points[i], labels[i], theta, theta_0)

    return sum/ len(Points)



