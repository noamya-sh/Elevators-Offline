# import numpy as np
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
        self.calls=[]
        self.fs=[]

    # def __str__(self) -> str:
    #     return f"id:{self._id}, speed:{self._speed}, minFloor:{self._minFloor}, " \
    #            f"maxFloor:{self._maxFloor}, closeTime:{self._closeTime}, " \
    #            f"openTime:{self._openTime}, startTime:{self._startTime}, stopTime:{self._stopTime}"

    def __add__(self, call:CallOfElevator):
        self.calls.append(CallOfElevator)
        time2src,time2dest= self.reachFloor(call.src, call.dest, call.Time)
        if time2src!=-1:
            self.fs.append(floorStop(call.src,time2src))
        if time2dest!=-1:
            self.fs.append(floorStop(call.dest, time2dest))
        # self.fs.sort
        return self

    def __iter__(self):
        return self.fs.__iter__()

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

    def reachFloor(self,src : int, dest : int, timeInit : float):#return the time that elevator reach the floor
        t1 = t2 = timeInit
        if not self.fs:
            t1 += self.disInTime(abs(src))
            if src!=0:
                t1+=self._startTime+self._stopTime+self._openTime
            t2 += self.disInTime(abs(src) + abs(dest - src)) + self.stop1() + self._stopTime + self._openTime
            return t1,t2
        i=0
        while self.fs[i].time < timeInit: #search the next task of elevator
            i+=1

        now = self.pos(timeInit)

        while i < len(self.fs) and abs(self.fs[i].floor - now.floor) < abs(src - now.floor):# not trust
            now = self.fs[i]
            i+=1
        if self.fs[i].floor != src:
            t1 += now.time + self.disInTime(abs(src - self.fs[i].floor)) + self._stopTime+self._openTime
            now = src
        else:
            t1=-1
        while i < len(self.fs) and abs(self.fs[i].floor - now) < abs(dest - now):# not trust
            if t1!=-1:
                self.fs[i].time =now.time +self.disInTime(abs(now.floor - self.fs[i].floor))+self.stop1()
            now = self.fs[i]
            i+=1
        if self.fs[i].floor != dest:
            t2 += self.fs[i].time + self.disInTime(abs(dest - self.fs[i].floor)) + self._stopTime+self._openTime
        else:
            t2=-1

        while i < len(self.fs):
            if t1!=-1:
                self.fs[i] += self.stop1()
            if t2!=-1:
                self.fs[i] += self.stop1()
            i += 1

        return (t1,t2)

    def time(self,call:CallOfElevator):
        callInit = call.Time
        i=0
        while self.fs[i]<callInit:
            i+=1
        list =[callInit]
        while i < len(self.fs):
            list.append(self.fs[i].time)
        all = np.diff(list).sum()