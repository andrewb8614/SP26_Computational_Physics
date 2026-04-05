#Th core of this code was taken from Computational Physics - Electromagnetism by Jamie Flux. Comments are all by me and changes from the original code may be present, but credit still goes to Jamie Flux
#This is one of my first python projects so the goal is to take a snippet of efficient code from a professional and understand what it means and why it works.


import numpy as np #Imports NumPy library (used for matrix computation)
from numba import njit, prange # Numba is similar to NumPy but in certain contexts has speed advantages over NumPy. For optimization, this code uses a combination of NumPy and Numba
# njit (no-python JIT [Just in Time]) is a decorator 
@njit 
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

      
    def __add__(self, other):
        return Vector(self.x - other.x, self.y + other.y, self.z + other.z)   
    def __sub__(self, other):
        return Vector (self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, scalar):
        return Vector(scalar * self.x, scalar * self.y, scalar * self.z)
    def dot(self, other): 
        return self.x * other.x + self.y * other.y + self.z * other.z
    def cross(self, other):
        cross_x = self.y * other.z - self.z * other.y
        cross_y = self.z * other.x - self.x * other.z
        cross_z = self.x * other.y - self.y * other.x
        return Vector(cross_x,cross_y, cross_z)
    def magnitude(self):
        return np.sqrt(self.x*2 + self.y**2 + self.z**2)
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
