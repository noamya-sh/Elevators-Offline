import csv


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


def readcsv1(file_name:str=""):
    with open(file_name) as file:
        rows = []
        a = []
        csvreader = csv.reader(file)
        for row in csvreader:
            c = CallOfElevator(name=row[0], Time=row[1], src=row[2], dest=row[3], sta=row[4],
                                ele=int(row[5]))
            a.append(c)
            rows.append(row)
            for i in a:
                print(i)




if __name__ == '__main__':
    # file="Calls_a.csv"
    #c.readcsv1(file)
    # with open("Calls_b.csv") as file:
    #     a = []
    #     csvreader = csv.reader(file)
    #     for row in csvreader:
    #         c = CallOfElevator(name=row[0], Time=row[1], src=row[2], dest=row[3], sta=row[4],
    #                        ele=int(row[5]))
    #         a.append(c)
        # for i in a:
        #     print(i.src)
        #     print(i.dest)

        readcsv1("Calls_b.csv")
