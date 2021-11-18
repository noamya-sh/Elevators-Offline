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
def getkey(dic,floor):
    l = np.array(list(dic.values()))
    diff = list(abs(l[1:] - l[:-1]))
    ls = list(abs(l[1:] - floor) + abs(floor - l[:-1]))
    for i in range(len(ls)):
        if ls[i]==diff[i]:
            return i+1;
    return len(l)

if __name__ == '__main__':
    a = {7:1,2:-5,3:-9, 1:-10,9:-12,10:-13,4:-20}
    dic = {k: v for k, v in a.items() if k < -1}
    x = len(dic)
    print(x)
    # print(list(sorted(a.keys()))[2:])
    # b ={210:-3,130:4,140:1,150:-2}
    # print(list(sorted(b.keys())))
    # print(list(b.values()))
    # print(list(sorted(b.values())))
    # # print(getkey(dic=a,floor=7))
    # # # for e in map(lambda x,y:[x,y], a[::2], a[1::2])
    # # # [(1, 2), :-5(3, 4), (5, 6), (7, 8), (9, 10), (11, None)]
    # # print(np.searchsorted([1, 5, 8, 12, 15], 2))
    # # l = np.array([1,-5,-9,-10,-12,-13,-20])
    # # # print((l[1:] - l[:-1]) / 2)
    # # x =7
    # # print(l)
    # # print(list(abs(l[1:] - l[:-1])))
    # # print(abs(l[1:] - 7) +abs(7-l[:-1]))
    # # print(np.diff(l))
    # # diff = np.abs(np.diff(l))
    # # print(diff)
    # # k=[]
    # # for i in l:
    # #     k.append(abs(x-i))
    # # print(k)
    # # # print(np.argmax(np.array(a)==1))
    # list = [1,5,8,10,15]
    # list2 = [1,3,5,8,10,15]
    # # print(list)
    # # n = np.diff(list)
    # # print(n)
    # # print(np.cumsum(n))
    # # def vv(x):
    #     return (x,2*x)
    # i,j = vv(5)
    # print(i)
    # print(j)

