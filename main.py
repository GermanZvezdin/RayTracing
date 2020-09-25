#!usr/bin/env python
from Color import color
from Image import image
from vector import vector
from point import point
from sphere import sphere
from scene import scene
from engine import RenderEngine
def main():
    WIDTH = 320
    HEIGHT = 200
    camera = point(0, 0, -1 )
    objects = [sphere(point(0, 0, 0), 0.5, color.from_hex("FF0000"))]
    scene_1 = scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()
    im = engine.render(scene_1)
    
    with open("render.ppm", "w") as img_file:
        im.write_ppm(img_file)



if __name__ == "__main__":
    main()

