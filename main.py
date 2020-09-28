#!usr/bin/env python
from Color import color
from Image import image
from vector import vector
from point import point
from sphere import sphere
from scene import scene
from engine import RenderEngine
from light import Light
from material import Material

def main():
    WIDTH = 1000
    HEIGHT = 1000
    camera = point(0, 0, -1 )
    objects = [sphere(point(0, 0, 0), 0.5, Material(color.from_hex("#FFFFFF"), 0.05, 0.1)) ]
    lights = [Light(point(10.0 * -1.14, 10 * 1.14, 0), color.from_hex("#FF0000")),
              Light(point(0, -10, 0), color.from_hex("#00FF00")),
              Light(point(10.0 * 1.14, 10.0 * 1.14, 0), color.from_hex("#0000FF")),
              ]
    scene_1 = scene(camera, objects,lights, WIDTH, HEIGHT)
    engine = RenderEngine()
    im = engine.render(scene_1)
    with open("render.ppm", "w") as img_file:
        im.write_ppm(img_file)



if __name__ == "__main__":
    main()

