import numpy as np
import matplotlib.pyplot as plt
import math

#number of points to generate (for bigger points usually there won't be a line that divides space correctly)
NUMBEROFPOINTS = 4


#creating numpy array NUMBEROFPOINTS x [[x-cordinate, y-cordinate], label]
RenderedPoints = np.array([ np.array([np.random.rand(2), [-1,1][np.random.choice(2, 1,)[0]] ], dtype = object)  for i in range(NUMBEROFPOINTS)])


def Percepton(array: np.array, epochs: int):

    theta  = np.zeros(2) #creating theta [0,0] 
    offset = np.zeros(1) #creating offset [0]

    for i in range(epochs): #iterating number of requested epochs

        for vector, label in array: # iterating through array where vector := [x-cordinate, y-cordinate] and label := [label] 
            
            if label*(vector@theta + offset) <= 0: 
                theta  += label*vector
                offset += label

    return theta, offset 

theta, offset = Percepton(RenderedPoints, 50) # calling Percepton

def Draw(points : np.array):

    #drawing all points
    plt.scatter( [points[:,0][i][0] for i in range(NUMBEROFPOINTS)], [points[:,0][i][1] for i in range(NUMBEROFPOINTS)])

    #drawing 1 labeled points once again with diffrent color
    plt.scatter( [points[:,0][i][0] if points[:,1][i] == 1 else None for i in range(NUMBEROFPOINTS)], [points[:,0][i][1] if points[:,1][i] == 1 else None for i in range(NUMBEROFPOINTS)])

    #drawing line 
    plt.plot([i for i in range(10)], [-(offset + theta[0]*i)/theta[1] for i in range(10)], label="percepton")

    plt.show()



if __name__ == '__main__':
    Draw(RenderedPoints)