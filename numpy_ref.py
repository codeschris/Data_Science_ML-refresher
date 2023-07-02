"""
This is a file containing basic Numpy commands, functions and methods. Think of it as a 
way to remind myself what does what, when to use it and how to use it in future Statistics, 
Data Science and Machine Learning operations.

Numpy is very extensive. With this in mind, I will only be testing for commands and methods so I can
apply them in a model or test where necessary.
"""
#Import module/dependency
import numpy as np

#Arrays
a = np.array([1, 2, 4]) #1D array
b = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype=int)

print("1D array:\n{}\n".format(a))
print("2D array:\n{}\n".format(b))
print("3D array:\n{}\n".format(c))

#Generating arrays
d = np.full((3, 3), 2)
e = np.ones((3, 3)) #generate array of ones
f = np.zeros((3, 3))    #generate array of zeros

print(d)
print(e)
print(f)