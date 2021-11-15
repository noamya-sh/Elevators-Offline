import csv
import sys

from Building import *
from CallOfElevator import *
from Elevator import * #Elevator


class Algo:
    def __init__(self, string: str = None):
        list = string.split(" ")
        b = Building()
        self.building = b.from_json(list[0])
        self.csv = self.readcsv(list[1])
        self.out = list[2]
        self.writeCsv(self.out, self.csv)

    def readcsv(file_name: str):
        with open(file_name) as file:
            CallsList = []
            csvreader = csv.reader(file)
            for row in csvreader:
                c = CallOfElevator(name=row[0], Time=float(row[1]), src=int(row[2]),
                                   dest=int(row[3]), sta=row[4],
                                   ele=int(row[5]))
                c.ele = Algo.allocate(c)
                CallsList.append(c)
            return CallsList

    def allocate(call: CallOfElevator=None):
        # b = Building()
        # b.from_json("B2.json")
        # i=0
        # for j in b.el:
        #     return min(b.el[i],b.el[i+1],)
        # i=0
        # for elev in self.building.el:
        #     if elev.calls[i].dest<call.dest:
        #         return 0
        #     elif elev.calls[i].dest==call.dest:
        #         return 1
        #     else:
        #         return 2
        if call.src != -4 and call.Time<90.155555555:
            return 0
        else:
            return 1

    #     min=sys.maxint
    #     j=0
    #     count=0
    #     for i in self.building.el:
    #         t = allTime(i,call)
    #         if t<min:
    #             min=t
    #             j=count
    #         count+=1
    #     writeCsv(call,j)
    #     addCall(j,call)

    def writeCsv(file, list):
        new_list = []
        for obj in list:
            new_list.append(obj.__dict__.values())
        with open(file, 'w', newline="") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerows(new_list)
            print(new_list)


if __name__ == '__main__':
    d = Algo("B5.json Calls_b.csv try.csv")


    # Algo("B5.json Calls_b.csv try.csv")
    # a = Algo.readcsv("Calls_b.csv")
    # Algo.writeCsv("try.csv", a)

    # a = Algo("<Building.json> <Calls.csv> <output.csv>")
    #     with open("Calls_a.csv") as file:
    #         a = []
    #         csvreader = csv.reader(file)
    #         for row in csvreader:
    #             c = CallOfElevator(name=row[0], Time=row[1], src=row[2], dest=row[3], sta=row[4],
    #                            ele=0)
    #             a.append(c)
    #         for i in a:
    #             print(i.ele)
    #             print(i.dest)
