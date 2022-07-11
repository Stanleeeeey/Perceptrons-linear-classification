import matplotlib.pyplot as plt
from LinearPerceptron import * #perceptron
from AverageLinearPerceptron import * # avarage_perceptron
import numpy as np

#number of points to generate (for bigger number of points there is bigger probability that there won't be a hyperlane dividing space correctly)
NUMBEROFPOINTS = 6
DIMENSION      = 3 # number of dimensions of point 


#creating numpy array NUMBEROFPOINTS x [[x-cordinate, y-cordinate], label]
Points = np.array([np.random.rand(DIMENSION)  for i in range(NUMBEROFPOINTS)])
Labels = np.array([np.random.choice([1,-1], 1)  for i in range(NUMBEROFPOINTS)])


def draw_points(points, labels):
    #drawing all points
    plt.scatter( [points[i][0] for i in range(NUMBEROFPOINTS)], [points[i][1] for i in range(NUMBEROFPOINTS)])

    #drawing 1 labeled points once again with diffrent color
    plt.scatter( [points[i][0] if labels[i] == 1 else None for i in range(NUMBEROFPOINTS)], [points[i][1] if labels[i] == 1 else None for i in range(NUMBEROFPOINTS)])

def Draw( theta, theta_0, label):

   
    #drawing line 
    plt.plot([i for i in range(10)], [-(theta_0 + theta[0]*i)/theta[1] for i in range(10)], label=label)









if __name__ == '__main__':
    draw_points(Points, Labels)
    theta, theta_0 = perceptron(Points, Labels, 50) # calling Percepton
    Draw( theta, theta_0, "percepton")

    theta, theta_0 = avarage_perceptron(Points, Labels, 50) # calling Percepton
    Draw( theta, theta_0,  "average percepton")

    plt.show()