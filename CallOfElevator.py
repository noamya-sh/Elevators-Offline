class CallOfElevator:
    def __init__(self, name: str = "", Time = 0.0, src: int = 0, dest: int = 0, sta=0, ele: int = 0, **kwargs):
        self.name = name
        self.Time = Time
        self.src = src
        self.dest = dest
        self.sta = sta
        self.ele = ele

    def __str__(self) -> str:
        return f"{self.name}, {self.Time}, src:{self.src}, dest:{self.dest}, {self.sta}, {self.ele}"

