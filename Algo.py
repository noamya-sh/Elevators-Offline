import csv
import sys

from Building import Building
from CallOfElevator import CallOfElevator


class Algo:
    def __init__(self,string:str=None):
        list = string.split(" ")
        b=Building()
        self.building=b.from_json(list[0])
        self.csv = list[1]
        self.out = list[2]

    def readcsv(file_name: str):
        with open(file_name) as file:
            rows = []
            a = []
            csvreader = csv.reader(file)
            for row in csvreader:
                c = CallOfElevator(name=row[0], Time=row[1], src=row[2],
                                   dest=row[3], sta=row[4], ele=int(row[5]))
                Algo.allocte(c)

    def allocte(self, call:CallOfElevator=None):
        min=sys.maxint
        j=0
        count=0
        for i in self.building.el:
            t = allTime(i,call)
            if t<min:
                min=t
                j=count
            count+=1
        writeCsv(call,j)
        addCall(j,call)

if __name__ == '__main__':
    Algo.readcsv("Calls_d.csv")
#     a=Algo("<Building.json> <Calls.csv> <output.csv>")
