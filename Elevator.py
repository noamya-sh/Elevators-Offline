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
        self.fs.append(floorStop(call.src,reachFloor(call.src)))
        self.fs.append(floorStop(call.dest, reachFloor(call.dest)))
        #self.fs.sort
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
        if disT <0:#yet in previous floor
            return previous.floor

        if previous.floor < next.floor:
            return previous.floor + self.disInFloor(disT)
        else:
            return previous.floor - self.disInFloor(disT)


    def disInFloor(self,travelTime:float)->float:
        return self._speed * travelTime

    def disInTime(self,distance):
        return distance/self._speed

    def reachFloor(self,floor:int,timeInit): #return the time that elevator reach the floor
        if not self.fs:
            return self._startTime+disinTime(abs(floor))+self._stopTime+self._openTime

        pos =