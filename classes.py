#general moving class
class Moving_object():
    def __init__(self):
        self.xspeed = 0 #horizontal speed
        self.yspeed = 0 #vertical speed
        self.xcord = 0 #x coördinate
        self.ycord = 0 #y coördinate
    
#ball variable
class Ball(Moving_object):
    def __init__(self):
        super().__init__()
        self.xcord = 500
        self.xspeed = 3
        self.ycord = 70
        self.weight = 0.1 #size of the parabole bigger number smaller parabole
        self.dia = 50 #diameter of the ball
