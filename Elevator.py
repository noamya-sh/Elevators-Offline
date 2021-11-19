import numpy as np
import math
import copy
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
        self.fs= {}
        self.call2test=None

    def __add__(self, call:CallOfElevator):
        self.addfloorsStop(self.fs,call)
        return self

    def __iter__(self):
        return self.fs.__iter__()

    def __lt__(self, other):
        return self.time(self.call2test) < other.time(self.call2test)

    def addfloorsStop(self,dict:{},call:CallOfElevator)->None:
        """
        :param dict: dict put new stops in it.
        :param call: call to insert in dict.
        """
        time2src, time2dest = self.reachFloor(dict,call.src, call.dest, call.Time)
        self.insetKV(dict, call.src,time2src,call.dest,time2dest)

    def disInFloor(self,travelTime:float)->float: # speed * time = distance
        """
        :param travelTime: time.
        :return distance that the elevator performs at a certain time.
        """
        return self._speed * travelTime

    def disInTime(self,distance:int)->float:
        """
        :param distance: distance of floors.
        :return time required to travel a certain distance.
        """
        return distance/self._speed

    def stop1(self)->float:
        """
        :return time of stop in floor.
        """
        return self._stopTime+self._openTime+self._closeTime+self._startTime

    def getind(self,list:list[int],floor:int)->int:
        """
        This function returns the index in which the input floor will be inserted.
        If is possible to insert the floor in a way that does not extend
        the way to other floors - insert there, otherwise insert at the end.
        :param list: list of floors.
        :param floor: floor to insert.
        :return index.
        """
        l = np.array(list)
        diff = abs(l[1:] - l[:-1])
        ls = abs(l[1:] - floor) + abs(floor - l[:-1])
        for i in range(len(ls)):
            if ls[i] == diff[i]:
                return i+1;
        return len(l)


    def reachFloor(self,dict,src : int, dest : int, timeInit : float)->tuple:#return the time that elevator reach the floors
        """
        This function will look for the time when the elevator will reach the src floor and the dest floor.
        :param dict: dict that from its data the times will be calculated.
        :param src: src floor of the callForElevator.
        :param dest: dest floor of the callForElevator.
        :param timeInit: time init of the callForElevator.
        :return :t1: time reach src floor. t2:time reach dest floor.
        """
        t1 = t2 = math.ceil(timeInit)
        if not dict:
            t1 += self.disInTime(abs(src))
            if src != 0:
                t1 += self.stop1()
            t2 = math.ceil(t1) +self.disInTime(abs(src) + abs(dest - src)) + self.stop1()
            return math.ceil(t1), math.ceil(t2)
        dic1 = {k: v for k, v in dict.items() if k > timeInit}
        dic2 = {k: v for k, v in dict.items() if k < timeInit}
        if not dic1: #the elevator in LEVEL state
            pos = dic2[max(dic2)]
            t1 = max(dic2) + self.disInTime(abs(src-pos))+self.stop1()
            t2 = math.ceil(t1) + self.disInTime(abs(dest-src))+self.stop1()
        else:
            if src not in dic1.values():
                ind = self.getind(list(dic1.values()), src)
                dic1_keys = list(sorted(dic1.keys()))
                dic1_values = list(dic1.values())
                t1 = dic1_keys[ind-1] + self.disInTime(abs(dic1_values[ind-1]-src))+self.stop1()
            else:
                ind =list(dic1.values()).index(src)
                t1= list(sorted(dic1.keys()))[ind]

            # find time for dest floor:
            if len(list(dic1.values())) > ind:
                if dest not in dic1.values():
                    ind2 = self.getind(list(dic1.values())[ind:], dest)
                    dic1_keys = list(sorted(dic1.keys()))[ind:]
                    dic1_values = list(dic1.values())[ind:]
                    t2 = dic1_keys[ind2-1] + self.disInTime(abs(dic1_values[ind2-1]-dest))+2*self.stop1()
                else:
                    ind2 =list(dic1.values()).index(dest)
                    t2 = list(sorted(dic1.keys()))[ind2]

            else:
                t2 = math.ceil(t1) + self.disInTime(abs(dest-src))+self.stop1()
        return math.ceil(t1),math.ceil(t2)

    def insetKV(self,dict:{},f1:int,t1:int,f2:int,t2:int)->None:
        """
        This function insert new stops to dict and updates the times of subsequent stops.
        :param dict: dict put new stops in it.
        :param f1: src floor.
        :param t1: time reach src floor.
        :param f2: dest floor.
        :param t2: time reach dest floor.
        """
        dic = {k: v for k, v in dict.items() if t1 <= k <= t2}
        if t1 in dic and t2 in dic:
            return
        if t1 not in dic:
            for k,v in dic.items():
                if k<t2:
                    dict[k+math.ceil(self.stop1())] = dict.pop(k)
            dict[t1] = f1
        if t2 not in dic:
            dic2 = {k: v for k, v in dict.items() if t2 < k}
            for k,v in dic2.items():
                dict[k+2*math.ceil(self.stop1())] = dict.pop(k)
            dict[t2] = f2

    def cleanfs(self,time)->None:
        """
        This function deletes all stops that are reached before 'time', except for the last stop
        :param time: the decisive time.
        """
        dic = {k: v for k, v in self.fs.items() if k < time}
        if len(dic)>0:
            x = max(dic)
            for k, v in dic.items():
                if k!=x:
                    self.fs.pop(k)

    def time(self,call:CallOfElevator)->int:
        """
        This function calculate the cost of insert new call to this elevator.
        :param call: callForElevator to check.
        """
        if not self.fs: #in case of start simulator
            self.addfloorsStop(self.fs,call)
            x = max(self.fs) - call.Time
            self.fs= {}
            return x
        callInit = call.Time
        self.cleanfs(callInit)
        dic = {k: v for k, v in self.fs.items() if k > callInit}
        d2 = copy.deepcopy(dic)
        t1, t2 = self.reachFloor(d2, call.src, call.dest, call.Time)
        timeTask = t2 - call.Time

        self.addfloorsStop(d2, call)
        d3 = {k: v for k, v in dic.items() if not (k == t1 and v == call.src) and not (k == t2 and v == call.dest)}
        l = []
        l.append(math.ceil(callInit))
        list1 = l + list(sorted(dic.keys()))
        list2 = l + list(sorted(d3.keys()))
        # print(list2)
        s1 = self.calDiff(list1)
        s2 = self.calDiff(list2)
        cost = s2-s1
        return cost + timeTask
    #
    def calDiff(self,list:list[int])->int:
        """
        This function calculate differnce of each element [1-end] with first element.
        :param list: list of int.
        :return: list of differences.
        """
        return sum([list[i] - list[0] for i in range(1, len(list))])