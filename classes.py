#general moving class
class moving_object():
    def __init__(self):
        self.hspeed = 10 #horizontal speed
        self.vspeed = 10 #vertical speed
        self.xcord = 0 #x coördinate
        self.ycord = 0 #y coördinate

    def left(self):
        self.xcord -= self.hspeed

    def right(self):
        self.xcord += self.hspeed

    def up(self):
        self.ycord -= self.vspeed

    def down(self):
        self.ycord == self.vspeed
    
