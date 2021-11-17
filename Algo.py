import csv
import sys
import random
from Building import Building
from CallOfElevator import *
from Elevator import * #Elevator


class Algo:
    def __init__(self, string: str = None):
        # self.building=Building()
        list = string.split(" ")
        b = Building()
        b.from_json(list[0])
        self.building = b
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
        # return random.randint(0, 9)
        k = self.building.el[0]
        k.call2test=call
        i = 0
        p=[]
        for v in self.building:
            if not v.fs:
                p.append(v)
        # p = [e for i, e in enumerate(list(self.building.el.values())) if not e.fs]
        min =10000
        x=0
        if len(p)>0:
            for i in range(len(p)):
                if p[i].time(call) < min:
                    min = p[i].time(call)
                    x = p[i]
            p[i]+=call
            return p[i]._id
        for e in self.building:
            e.call2test = call
            if k>e:
               k=e
        k+=call
        return k._id
        # if call.src <= -1 and call.Time<90.155555555:
        #     return 0
        # else:
        #     return 1


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
    # # d.building=b
    # d=Algo()
    # print(d.readcsv("C:\\Users\\נעמיה\\PycharmProjects\\Elevators-Offline\\Calls_a.csv"))
    # d.writeCsv("try.csv",a)
    Algo("B5.json C:\\Users\\נעמיה\\PycharmProjects\\Elevators-Offline\\Calls_d.csv try.csv")
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
