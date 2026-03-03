import numpy as np

def rotate_around_z(points, theta):
    points = np.array(points)
    arr = []
    if len(points) != 3:
        for i in range(len(points)):
            t = [points[i][0]*np.cos(theta) - points[i][1]*np.sin(theta), points[i][0]*np.sin(theta) + points[i][1]*np.cos(theta), points[i][2]]
            arr.append(t)
    else:
        arr = [points[0]*np.cos(theta) - points[1]*np.sin(theta), points[0]*np.sin(theta) + points[1]*np.cos(theta), points[2]]
        
    return np.array(arr)