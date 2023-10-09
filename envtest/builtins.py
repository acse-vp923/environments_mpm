import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc
import random
import pandas as pd

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve','sum_column_values']

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def rand_array(shape):
    return np.random.rand(*shape)

def my_mat_solve(A, b):
    return A.inv()*b

def sum_column_values(data, column_name):
    df = pd.DataFrame(data)
    column_sum = df[column_name].sum()
    return column_sum