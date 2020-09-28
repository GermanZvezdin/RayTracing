from Color import color
class Light:
    def __init__(self, position, c = color.from_hex("#FFFFFF")):
        self.position = position
        self.color = c
