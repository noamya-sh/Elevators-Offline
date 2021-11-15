from floorStop import *
from Elevator import *
from CallOfElevator import *
import numpy as np
class lll:
    def __init__(self,x):
        self._dd=x;

class kkk:
    def __init__(self,y):
        self.gg=y


if __name__ == '__main__':
    # d = {"_id": 10,
    #      "_speed": 9.0,
    #      "_minFloor": -10,
    #      "_maxFloor": 100,
    #      "_closeTime": 1,
    #      "_openTime": 1,
    #      "_startTime": 2,
    #      "_stopTime": 2}
    # e = Elevator(**d)
    # x, y = e.reachFloor(0, 5, 62)
    # print(x,y)
    list = [1,5,8,10]
    print(list)
    n = np.diff(list)[1:]
    for i in n:
        print(i)
    print(np.diff(list).sum())
    # def vv(x):
    #     return (x,2*x)
    # i,j = vv(5)
    # print(i)
    # print(j)

