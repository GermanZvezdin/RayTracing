#!usr/bin/env python
from Color import color
from Image import image
from vector import vector
from point import point
from sphere import sphere
from scene import scene
from engine import RenderEngine
def main():
    WIDTH = 1000
    HEIGHT = 1000
    camera = point(0, 0, -1 )
    objects = [sphere(point(0, 0.5, 0.5), 0.2, color.from_hex("FFFF00")), sphere(point(0, 0, 0), 0.2, color.from_hex("FF0000")), sphere(point(0, 0.5, 0.5), 0.2, color.from_hex("FFFF00")) ]
    scene_1 = scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()
    im = engine.render(scene_1)
    
    with open("render.ppm", "w") as img_file:
        im.write_ppm(img_file)



if __name__ == "__main__":
    main()

