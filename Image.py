import math
from Color import color
class image:
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight
        self.pixels = [[None for _ in range(width)] for _ in range(hight)]
    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color
         
    def write_ppm(self, img_file):
        def to_byte(c):
            return round(max(min(c * 255, 255), 0) )
        img_file.write("P3 {} {}\n255\n".format(self.width, self.hight)
        )
        for row in self.pixels:
            for color in row:
                img_file.write(
                    "{} {} {} ".format(
                    to_byte(color.x), to_byte(color.y), to_byte(color.z)
                    )
                )
            img_file.write("\n")
