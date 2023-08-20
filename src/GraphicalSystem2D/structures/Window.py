import consts


class Window:
    def __init__(self):
        self.xw_min = consts.VIEWPORT_X_MIN
        self.yw_min = consts.VIEWPORT_Y_MIN
        self.xw_max = consts.VIEWPORT_X_MAX
        self.yw_max = consts.VIEWPORT_Y_MAX

        self.x_displacement = 0
        self.y_displacement = 0
        
        self.step = 10  # amount of pixels

    def reescale(self, amount):
        ...

    def navigate(self, direction):
        if direction == "UP":
            self.yw_min += self.step
            self.yw_max += self.step
            self.y_displacement += self.step
        elif direction == "DOWN":
            self.yw_min -= self.step
            self.yw_max -= self.step
            self.y_displacement -= self.step
        elif direction == "RIGHT":
            self.xw_min += self.step
            self.xw_max += self.step
            self.x_displacement += self.step
        elif direction == "LEFT":
            self.xw_min -= self.step
            self.xw_max -= self.step
            self.x_displacement -= self.step

    def getDisplacement(self) -> tuple:
        return self.x_displacement, self.y_displacement
