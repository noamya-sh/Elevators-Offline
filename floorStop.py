class floorStop:
    def __init__(self, floor: int, time: float):
        self.floor = floor
        self.time = time

    def __add__(self, t):
        self.time += t
        return self

    def __