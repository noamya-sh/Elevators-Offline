import numpy as np

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

    def __str__(self) -> str:
        return f"id:{self._id}, speed:{self._speed}, minFloor:{self._minFloor}, " \
               f"maxFloor:{self._maxFloor}, closeTime:{self._closeTime}, " \
               f"openTime:{self._openTime}, startTime:{self._startTime}, stopTime:{self._stopTime}"

    def __add__(self, call:CallOfElevator):
        self.calls.append(CallOfElevator)
        time2src,time2dest=self.reachFloor(call.src,call.dest,call.Time)
        if time2src!=-1:
            self.fs.append(floorStop(call.src,time2src))
        if time2dest!=-1:
            self.fs.append(floorStop(call.dest, time2dest))
        # self.fs.sort
        return self

    def __iter__(self):
        return self.calls.__iter__()

    def pos(self,time):
        if not self.fs:
            return 0
        t = self.fs[0].time
        i=0

        #Extreme cases:
        if t>time:
            return self.disInFloor(time - self._startTime)
        if self.fs[len(self.fs)-1].time<time:
            return self.fs[len(self.fs)-1].floor

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

    def reachFloor(self,floor1 : int, floor2 : int, timeInit : float):#return the time that elevator reach the floor
        if not self.fs:
            return disinTime(abs(floor1)+abs(floor2-floor1))+self.stop1()+self._stopTime+self._openTime
        i=0
        while self.fs[i].time < timeInit: #search the next task of elevator
            i+=1
        now = self.pos(timeInit)

        while i < len(self.fs) and abs(self.fs[i].floor - now) < abs(floor1 - now):# not trust
            now = self.fs[i].floor
            i+=1
        if self.fs[i].floor != floor1:
            t1=self.fs[i].time+self.disInTime(abs(floor1-self.fs[i].floor))+self.stop1()
        else:
            t1=-1
        while i < len(self.fs) and abs(self.fs[i].floor - now) < abs(floor2 - now):# not trust
            if t1!=-1:
                self.fs[i]+self.stop1()
            i+=1
        if self.fs[i].floor != floor2:
            t2 = self.fs[i].time+self.disInTime(abs(floor2-self.fs[i].floor))+self.stop1()
        else:
            t2=-1
        while i < len(self.fs):
            if t1!=-1:
                self.fs[i] += self.stop1()
            if t2!=-1:
                self.fs[i] += self.stop1()
            i += 1

        return (t1,t2)
