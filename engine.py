from Image import image
from ray import ray
from point import point
from Color import color
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
        return pixels
    def ray_trace(self, rey, scene):
        colar = color(0, 0, 0)
        (dist_hit, obj_hit) = self.find_nearest(rey, scene)
        
        if obj_hit is None:
            return colar
        
        hit_pos = rey.origin + rey.direction * dist_hit
        colar = colar + self.color_at(obj_hit, hit_pos, scene, rey)
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
    def color_at(self, obj_hit, hit_pos, scene, rey):
        normal = obj_hit.get_normal(hit_pos)
        vec = vector(rey.origin.x - rey.direction.x, rey.origin.y - rey.direction.y, rey.origin.z - rey.direction.z)
        angle = normal.get_cos(vec)
        #print(math.acos(angle) * 57.7)
        #print((1 - math.fabs(math.acos(angle) * 57.7 * 100 / 90)))
        return obj_hit.material * angle
                
