import numpy as np
from ray import ray
class sphere():
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material
    def intersects(self, rey):
        sphere_to_ray = rey.origin - self.center
        a = 1
        b = 2 * rey.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius
        diskriminant = b * b - 4  * a * c
        
        if diskriminant >= 0:
            dist = (- b  - np.sqrt(diskriminant)) / 2 * a
            if dist > 0:
                return dist
        return None
         
    
