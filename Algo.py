import csv
import sys
import random
from Building import *
from CallOfElevator import *
from Elevator import *


class Algo:
    def __init__(self, json,input,output):
        b = Building()
        b.from_json(json)
        self.building = b
        self.csv = self.readcsv(input)
        self.writeCsv(output, self.csv)

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
        k = self.building.el[0]
        k.call2test=call
        i = 0
        p=[]
        # if len(self.building.el) == 2:
        #     if len(k.fs) < len(self.building.el[1].fs):
        #         k += call
        #         return k._id
        #     else:
        #         self.building.el[1] += call
        #         return self.building.el[1]._id
        for v in self.building:
            if not v.fs or (len(v.fs) == 1 and all(k < call.Time for k in v.fs.keys())):
                p.append(v)
        min =10000
        x=0
        if len(p)>0:
            for i in range(len(p)):
                if p[i].time(call) < min:
                    min = p[i].time(call)
                    x = p[i]
            x+=call
            return x._id

        for e in self.building:
            e.call2test = call
            if k>e:
               k=e
        k+=call
        return k._id

    def writeCsv(self, file, list):
        new_list = []
        for obj in list:
            new_list.append(obj.__dict__.values())
        with open(file, 'w', newline="") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerows(new_list)


if __name__ == '__main__':

    import time

    st_time = time.time()
    Algo(json="B3.json", input="Calls_d.csv",output="try.csv")
    sp_time = time.time()
    print(sp_time-st_time)
