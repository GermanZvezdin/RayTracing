from Image import image
from ray import ray
from point import point
from Color import color
from material import Material
from vector import vector
import math
class RenderEngine:
    def render(self, scene):
        width = scene.width
        height = scene.height
        ascept_ratio = float(width) / height
        x0 = -1.0
        x1 = +1.0
        xstep = (x1 - x0) / (width - 1)
        y0 = -1.0 / ascept_ratio
        y1 = +1.0 / ascept_ratio
        ystep = (y1 - y0) / (height - 1)
        
        camera = scene.camera
        pixels = image(width, height)
        for j in range(height):
            y = y0 + j * ystep
            for i in range(width):
                x = x0 + i * xstep
                new_point = point(x,y) - camera
                #print(new_point)
                rey = ray(camera, new_point)
                pixels.set_pixel(i, j, self.ray_trace(rey, scene))
            #progress bar
            print("{:3.0f}%".format(float(j)/float(height) * 100), end="\r")
        return pixels
    def ray_trace(self, rey, scene):
        colar = color(0, 0, 0)
        (dist_hit, obj_hit) = self.find_nearest(rey, scene)
        
        if obj_hit is None:
            return colar
        
        hit_pos = rey.origin + rey.direction * dist_hit
        hit_normal = obj_hit.normal(hit_pos)
        colar = colar + self.color_at(obj_hit, hit_pos, hit_normal, scene)
        return colar
    def find_nearest(self, rey, scene):
        dist_min = None
        obj_hit = None
        for obj in scene.objects:
            dist = obj.intersects(rey)
            if (dist is not None) and ((obj_hit is None) or (dist < dist_min)):
                dist_min = dist
                obj_hit = obj
        return (dist_min, obj_hit)
    def color_at(self, obj_hit, hit_pos,normal, scene):
        mat = obj_hit.material
        obj_color = mat.color_at(hit_pos)
        specular_k = 1.5
        to_cam = scene.camera - hit_pos
        c = mat.ambient * color.from_hex("#000000")
        for light in scene.lights:
            to_light = ray(hit_pos, light.position - hit_pos)
            #Освещение по Ламберту
            c = c + obj_color * mat.diffuse * max(normal.dot_product(to_light.direction), 0)
            #Blin-Phong lightinig
            half_vector = (to_light.direction + to_cam).normolize()
            c = c + light.color * mat.specular * max(normal.dot_product(half_vector), 0) ** specular_k
        return c
                
