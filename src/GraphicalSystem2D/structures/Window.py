class Window:
    def __init__(self, xw_min: int, yw_min: int, xw_max: int, yw_max: int):
        self.xw_min = xw_min
        self.yw_min = yw_min
        self.xw_max = xw_max
        self.yw_max = yw_max
        
        self.step = 10 # amount of pixels
        
    def reescale(self, amount):
        ...
        
    