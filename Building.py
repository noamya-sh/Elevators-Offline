import json
from Elevator import *

class Building:
    def __init__(self, minFloor: int = None, maxFloor: int = None, el: Elevator = {}, **kwargs):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.el = el

    def __iter__(self):
        return self.el.values().__iter__()

    def from_json(self, file_name: str)->None:
        with open(file_name, "r") as f:
            dict_ele = json.load(f)
            self.minFloor = dict_ele.get("_minFloor")
            self.maxFloor = dict_ele.get("_maxFloor")
            new_ele_arr = dict_ele.get("_elevators")
            e = {}
            i = 0
            for v in new_ele_arr:
                Elev = Elevator(**v)
                e[i] = Elev
                i += 1
            self.el = e
