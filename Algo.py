import csv
import Building
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
            header = csvreader
            for row in csvreader:
                rows.append(row)
            print(header)
            print(rows)

    def readcsv1(file_name: str = ""):
        with open(file_name) as file:
            rows = []
            a = []
            csvreader = csv.reader(file)
            for row in csvreader:
                c = CallOfElevator(name=row[0], Time=row[1], src=row[2],
                                   dest=row[3], sta=row[4],ele=int(row[5]))
                a.append(c)
                rows.append(row)
            for i in a:
                print(i)

    # if __name__ == '__main__':
    #     readcsv1("Calls_d.csv")
#     a=Algo("<Building.json> <Calls.csv> <output.csv>")
