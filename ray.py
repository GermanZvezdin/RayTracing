class ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normolize() 
