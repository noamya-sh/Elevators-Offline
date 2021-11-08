import json

from Elevator import Elevator


class Building:
    def __init__(self, minFloor:int=None, maxFloor:int=None, el:Elevator={}, **kwargs):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.el = el

    def __str__(self) -> str:
        c = ""
        for i in self.el:
            c += str(self.el[i])
        return f"minFloor=:{self.minFloor}, maxFloor=:{self.maxFloor}, el:{c}"

    def from_json(self, file_name: str):
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


import csv


def readcsv(file_name: str):
    with open(file_name) as file:
        rows = []
        a = []
        csvreader = csv.reader(file)
        header = csvreader
        for row in csvreader:
            rows.append(row)
        print(header)
        print(rows)
        #rows.index(1)


# if __name__ == '__main__':
#     b = Building()
#     b.from_json("B5.json")
#     E = b.el[3]._speed
#     s = b.minFloor
#     # print(b)
#     # print(E)
#     # print(s)
#     for i in b.el:
#          print(b.el[i])
#     # readcsv("Calls_a.csv")
