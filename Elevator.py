import numpy as np
import math
from floorStop import *
from CallOfElevator import *
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
        self.fs=[]
        self.call2test=None

    # def __str__(self) -> str:
    #     return f"id:{self._id}, speed:{self._speed}, minFloor:{self._minFloor}, " \
    #            f"maxFloor:{self._maxFloor}, closeTime:{self._closeTime}, " \
    #            f"openTime:{self._openTime}, startTime:{self._startTime}, stopTime:{self._stopTime}"

    def __add__(self, call:CallOfElevator):
        self.addfloorsStop(call)
        return self

    def __iter__(self):
        return self.fs.__iter__()

    def __lt__(self, other):
        return self.time(self.call2test) > other.time(self.call2test)

    def addfloorsStop(self,call:CallOfElevator):
        time2src, time2dest = self.reachFloor(call.src, call.dest, call.Time)
        if time2src != -1:
            self.fs.append(floorStop(call.src, math.ceil(time2src)))
        if time2dest != -1:
            self.fs.append(floorStop(call.dest, math.ceil(time2dest)))
        self.fs.sort()

    def pos(self,time):
        if not self.fs:
            return 0
        t = self.fs[0].time

        #Extreme cases:
        if t>time:
            return self.disInFloor(time - self._startTime)
        if self.fs[len(self.fs)-1].time<time:
            return self.fs[len(self.fs)-1].floor

        i = 0
        while t<time and i < len(self.fs):
            t=self.fs[i].time
            i+=1

        previous=self.fs[i - 1]
        if i==len(self.fs):
            return previous.floor
        next = self.fs[i]
        disT = time - previous.time - self._startTime
        if disT <0:  #yet in previous floor
            return previous.floor

        if previous.floor < next.floor:
            return previous.floor + self.disInFloor(disT)
        else:
            return previous.floor - self.disInFloor(disT)


    def disInFloor(self,travelTime:float)->float: # speed * time = distance
        return self._speed * travelTime

    def disInTime(self,distance):
        return distance/self._speed

    def stop1(self):
        return self._stopTime+self._openTime+self._closeTime+self._startTime
    def cleanPast(self,time):
        i=0
        while i < len(self.fs):
            if self.fs[i].time<time:
                self.fs.remove(self.fs[i])
            i+=1
        return
    def reachFloor(self,src : int, dest : int, timeInit : float):#return the time that elevator reach the floor
        t1 = t2 = timeInit
        if not self.fs:
            t1 += self.disInTime(abs(src))
            if src!=0:
                t1+=self._startTime+self._stopTime+self._openTime
            t2 += self.disInTime(abs(src) + abs(dest - src)) + self.stop1() + self._stopTime + self._openTime
            return t1,t2
        i=0
        # self.cleanPast(timeInit)
        prev=floorStop(self.pos(timeInit),timeInit)
        while  i < len(self.fs) and self.fs[i].time < timeInit: #search the next task of elevator
            prev = self.fs[i]  # self.pos(timeInit)
            i+=1

        while i < len(self.fs) and abs(self.fs[i].floor - prev.floor) < abs(src - prev.floor)+self.stopInFloors():# not trust
            prev = self.fs[i]
            i+=1
        if i==len(self.fs) or self.fs[i].floor != src:
            t1 += prev.time + self.disInTime(abs(src - prev.floor)) + self._stopTime + self._openTime
            prev=floorStop(src,t1)
            # prev = src
        else:
            t1=-1
        while i < len(self.fs) and abs(self.fs[i].floor - prev.floor) < abs(dest - prev.floor)+self.stopInFloors():# not trust
            if t1!=-1:
                self.fs[i].time = prev.time + self.disInTime(abs(prev.floor - self.fs[i].floor)) + self.stop1()
            prev = self.fs[i]
            i+=1
        if i==len(self.fs) or self.fs[i].floor != dest:
            t2 += prev.time + self.disInTime(abs(dest - prev.floor)) + self._stopTime+self._openTime
            prev = floorStop(src, t1)
        else:
            t2=-1

        while i < len(self.fs):
            # if t1!=-1:
            #     self.fs[i] = self.stop1()
            # if t2!=-1:
            #     self.fs[i] += self.stop1()
            self.fs[i].time = prev.time + self.disInTime(abs(prev.floor - self.fs[i].floor)) + self.stop1()
            prev = self.fs[i]
            i += 1

        return t1,t2
    def stopInFloors(self):
        return self.disInFloor(self._stopTime)

    def time(self,call:CallOfElevator):
        if not self.fs:
            self.addfloorsStop(call)
            return self.fs[1].time - call.Time
        callInit = call.Time
        i=0
        while i<len(self.fs) and self.fs[i].time<callInit:
            i+=1
        pre = self.fs[:i]
        fs2 = self.fs[i:].copy()
        self.addfloorsStop(call)
        list1 =[]
        while i < len(self.fs):
            list1.append(self.fs[i].time)
            i+=1
        list2 = []
        j=0
        while j < len(fs2):
            list2.append(fs2[j].time)
            j+=1
        cost = np.cumsum(np.diff(list1)).sum() - np.cumsum(np.diff(list2).sum())
        self.fs=pre+fs2
        return cost
