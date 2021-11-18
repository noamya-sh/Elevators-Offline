import numpy as np
import math
from floorStop import *
from CallOfElevator import *
import copy
class Elevator:
    def __init__(self, _id:int=None, _speed:float=None, _minFloor:int=None,
                 _maxFloor:int=None, _closeTime:float=None, _openTime:float=None,
                 _startTime:float=None, _stopTime:float=None, **kwargs):
        self._id = _id
        self._speed = _speed
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._closeTime = _closeTime
        self._openTime = _openTime
        self._startTime = _startTime
        self._stopTime = _stopTime
        self.fs= {}
        self.call2test=None

    # def __str__(self) -> str:
    #     return f"id:{self._id}, speed:{self._speed}, minFloor:{self._minFloor}, " \
    #            f"maxFloor:{self._maxFloor}, closeTime:{self._closeTime}, " \
    #            f"openTime:{self._openTime}, startTime:{self._startTime}, stopTime:{self._stopTime}"

    def __add__(self, call:CallOfElevator):
        self.addfloorsStop(self.fs,call)
        return self

    def __iter__(self):
        return self.fs.__iter__()

    def __lt__(self, other):
        return self.time(self.call2test) < other.time(self.call2test)

    def addfloorsStop(self,dict,call:CallOfElevator):
        time2src, time2dest = self.reachFloor(dict,call.src, call.dest, call.Time)
        self.insetKV(dict, call.src,time2src,call.dest,time2dest)

    def disInFloor(self,travelTime:float)->float: # speed * time = distance
        return self._speed * travelTime

    def disInTime(self,distance):
        return distance/self._speed

    def stop1(self):
        return self._stopTime+self._openTime+self._closeTime+self._startTime

    def getind(self,list,floor):
        l = np.array(list)
        diff = abs(l[1:] - l[:-1])
        ls = abs(l[1:] - floor) + abs(floor - l[:-1])
        for i in range(len(ls)):
            if ls[i] == diff[i]:
                return i+1;
        return len(l)

    # def pos(self,dict,time):
    #     dic1 = {k: v for k, v in dict.items() if k > time}
    #     dic2 = {k: v for k, v in dict.items() if k <= time}
    #     if len(dic1) == 0 and len(dic2) == 0:
    #         return 0
    #     if len(dic2) > 0:
    #         if len(dic1)>0:
    #             x = dic1[min(dic1)]-dic2[max(dic2)]
    #             if x > 0:
    #                 return dic2[max(dic2)] + self.disInFloor(math.ceil(time - max(dic2) - self._startTime))+self.stopInFloors()
    #             else:
    #                 return dic2[max(dic2)] - self.disInFloor(math.ceil(time - max(dic2) - self._startTime))-self.stopInFloors()
    #         else:
    #             return dic2[max(dic2)]
    #     else:
    #         if dic1[min(dic1)]>0:
    #             return self.disInFloor(math.ceil(time - self._startTime))+self.stopInFloors()
    #         else:
    #             return 0-self.disInFloor(math.ceil(time - self._startTime))-self.stopInFloors()

    def reachFloor(self,dict,src : int, dest : int, timeInit : float):#return the time that elevator reach the floors
        t1 = t2 = timeInit
        if not dict:
            t1 += self.disInTime(abs(src))
            if src != 0:
                t1 += self.stop1()
            t2 = math.ceil(t1) +self.disInTime(abs(src) + abs(dest - src)) + self.stop1()
            return math.ceil(t1), math.ceil(t2)
        dic1 = {k: v for k, v in dict.items() if k > timeInit}
        dic2 = {k: v for k, v in dict.items() if k < timeInit}
        if not dic1:
            pos = dic2[max(dic2)]
            t1 = max(dic2) + self.disInTime(abs(src-pos))+self.stop1()
            t2 = math.ceil(t1) + self.disInTime(abs(dest-src))+self.stop1()
        else:
            ind = self.getind(list(dic1.values()), src)
            dic1_keys = list(sorted(dic1.keys()))
            dic1_values = list(dic1.values())
            t1 = dic1_keys[ind-1] + self.disInTime(abs(dic1_values[ind-1]-src))+self.stop1()
            if len(list(dic1.values())) > ind:
                ind2 = self.getind(list(dic1.values())[ind:], dest)
                dic1_keys = list(sorted(dic1.keys()))[ind:]
                dic1_values = list(dic1.values())[ind:]
                t2 = dic1_keys[ind2-1] + self.disInTime(abs(dic1_values[ind2-1]-dest))+2*self.stop1()
            else:
                t2 = math.ceil(t1) + self.disInTime(abs(dest-src))+self.stop1()
        return math.ceil(t1),math.ceil(t2)

    def insetKV(self,dict,f1,t1,f2,t2):
        dic = {k: v for k, v in dict.items() if t1 <= k <= t2}
        if t1 and t2 in dic:
            return
        if t1 not in dic:
            for k,v in dic.items():
                if k<t2:
                    dict[math.ceil(k+self.stop1())] = dict.pop(k)
            dict[t1] = f1
        if t2 not in dic:
            dic2 = {k: v for k, v in dict.items() if t2 < k}
            for k,v in dic2.items():
                dict[k+2*math.ceil(self.stop1())] = dict.pop(k)
            dict[t2] = f2

    def stopInFloors(self):
        return self.disInFloor(self._stopTime)

    def cleanfs(self,time):
        dic = {k: v for k, v in self.fs.items() if k < time}
        if len(dic)>0:
            x = max(dic)
            for k, v in dic.items():
                if k!=x:
                    self.fs.pop(k)

    def time(self,call:CallOfElevator):
        if not self.fs:
            self.addfloorsStop(self.fs,call)
            x = max(self.fs) - call.Time
            self.fs= {}
            return x

        callInit = call.Time
        self.cleanfs(callInit)
        i=0
        dic = {k: v for k, v in self.fs.items() if k > callInit}
        d2 = copy.deepcopy(dic)
        t1, t2 = self.reachFloor(d2, call.src, call.dest, call.Time)
        timeTask = t2 - call.Time
        self.addfloorsStop(d2, call)
        d3 = {k: v for k, v in dic.items() if not (k == t1 and v== call.src) and not (k ==t2 and v==call.dest)}
        l=[]
        l.append(math.ceil(callInit))
        list1 = l + list(sorted(dic.keys()))
        # print(list1)
        list2 = l + list(sorted(d3.keys()))
        # print(list2)
        # s1=self.calDiff(list1)
        # s2=self.calDiff(list2)
        # if len(list2) != len(list1):
        #     print(callInit)
        #     print(list1)
        #     # print(np.cumsum(np.diff(list1)))
        #     print(list2)
            # print(np.cumsum(np.diff(list2)))
        #     print("*************************")
        # s = 0
        # for i in range(len(list2)):
        #     s+=list2[i]-list1[i]
        cost = np.diff(list2).sum() - np.diff(list1).sum()
        # cost = s2-s1
        return cost + timeTask
    #
    # def calDiff(self,list):
    #     return sum([list[i] - list[0] for i in range(1, len(list))])