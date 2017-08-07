#general moving class
class moving_object():
    def __init__(self):
        self.xspeed = 0 #horizontal speed
        self.yspeed = 0 #vertical speed
        self.xcord = 0 #x coördinate
        self.ycord = 0 #y coördinate

    '''def left(self):
        self.xcord -= self.hspeed

    def right(self):
        self.xcord += self.hspeed

    def up(self):
        self.ycord -= self.vspeed

    def down(self):
        self.ycord == self.vspeed'''
    
#ball variable
class ball():
    def __init__(self, dia):
        self.xcord = 100 #x coord
        self.ycord = 70 #y coord
        self.xspeed = 3 #horizontal speed
        self.yspeed = 0 #vertical speed
        self.weight = 0.1 #size of the parabole bigger number smaller parabole
        self.dia = dia
