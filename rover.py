direction_to_degrees = {"E": 0, "N": 90, "W": 180, "S": 270}
degrees_to_direction = {0: "E", 90: "N", 180: "W", 270: "S"}

class Rover:


    def __init__(self, name, x, y, d, maxX, maxY):
        self.name = name
        self.x = x
        self.y = y
        self.d = d
        self.maxX = maxX 
        self.maxY = maxY 
    
    def rotate(self, left_or_right):
        if left_or_right == 'L':
            self.d = (self.d + 90) % 360
        if left_or_right == 'R':
            self.d = (self.d - 90) % 360
    
    def advance(self):
        if self.d == 0: #move right/est
            x = self.x + 1
            y = self.y
        if self.d == 90: #move up/north
            x = self.x
            y = self.y + 1
        if self.d == 180: #move left/west
            x = self.x - 1
            y = self.y
        if self.d == 270: #move down/south
            x = self.x
            y = self.y -1
        if x > self.maxX or y > self.maxY:
            raise Exception(self.name + " requires attention! The instructions given will take it out of its designated area")
        self.x = x
        self.y = y
    def read_and_follow_instruction_tape(self, instruction_tape):
        for c in instruction_tape:
            if c == "M":
                self.advance()
            if c == "L" or c == "R":
                self.rotate(c)
            
    def __repr__(self):
        return "%d %d %s" % (self.x, self.y, degrees_to_direction[self.d])  
    def __str__(self):
        return "%d %d %s" % (self.x, self.y, degrees_to_direction[self.d])  