import math
import numpy as np


def calculate_2norm(vector):

    return math.sqrt(sum([value**2 for value in vector]))



def calculate_cosine(vector1, vector2):
    
    return (np.dot(vector1, vector2)/(calculate_2norm(vector1) * calculate_2norm(vector2)))