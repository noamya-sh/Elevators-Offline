import csv
import sys

from Building import Building
from CallOfElevator import CallOfElevator
from Elevator import * #Elevator


class Algo:
    def __init__(self, string: str = None):
        # self.building=Building()
        list = string.split(" ")
        b = Building()
        self.building = b.from_json(list[0])
        self.csv = self.readcsv(list[1])
        self.out = list[2]
        self.writeCsv(self.out, self.csv)

    def readcsv(self, file_name):
        with open(file_name) as file:
            CallsList = []
            csvreader = csv.reader(file)
            for row in csvreader:
                c = CallOfElevator(name=row[0], Time=float(row[1]), src=int(row[2]),
                                   dest=int(row[3]), sta=row[4],
                                   ele=int(row[5]))
                c.ele = self.allocate(c)
                CallsList.append(c)
            return CallsList

    def allocate(self, call: CallOfElevator=None):

        for e in self.building:
            return min()
        if call.src <= -1 and call.Time<90.155555555:
            return 0
        else:
            return 1


    def writeCsv(self, file, list):
        new_list = []
        for obj in list:
            new_list.append(obj.__dict__.values())
        with open(file, 'w', newline="") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerows(new_list)
            print(new_list)


if __name__ == '__main__':
    # d=Algo("B2.json")
    # b=Building()
    # b.from_json("B2.json")
    # d.building=b
    # a=d.readcsv("Calls_b.csv")
    # d.writeCsv("try.csv",a)
    Algo("B2.json Calls_b.csv try.csv")
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
