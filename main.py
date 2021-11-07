import json
class Elevator:
    def __init__(self,_id:int =None,_speed:float =None, _minFloor:int =None, _maxFloor:int =None,
                 _closeTime:float =None,_openTime:float =None,_startTime:float =None,_stopTime:float =None,**kwargs):

        self._id=_id;
        self._speed=_speed
        self._minFloor=_minFloor
        self._maxFloor=_maxFloor
        self._closeTime=_closeTime
        self._openTime=_openTime
        self._startTime=_startTime
        self._stopTime=_stopTime

    def __str__(self) -> str:
        return f"Elevator id:{self._id}, speed:{self._speed}, minFloor:{self._minFloor}, " \
               f"maxFloor:{self._maxFloor}, closeTime:{self._closeTime}, openTime:{self._openTime}," \
               f" startTime:{self._startTime}, stopTime:{self._stopTime}"


class Building:
    def __init__(self,minFloor:int =None,maxFloor:int =None,**kwargs):
        self.minFloor=minFloor
        self.maxFloor=maxFloor
        self.elevators={}

    def getElevator(self,index):
        return self.elevators[index]

    def init_from_file(self, file_name: str) -> None:
        with open(file_name, "r") as f:
            dict_building = json.load(f)
            self.minFloor=dict_building.get("_minFloor")
            self.maxFloor = dict_building.get("_maxFloor")
            list_ele = dict_building.get("_elevators")
            i=0
            el={}
            for d in list_ele:
                elvator=Elevator()
                elvator.__dict__.update(d)
                # elvator = Elevator(**d)
                el[i] = elvator
                i+=1
            self.elevators=el
    def __str__(self):
        s="**************************************************" \
          "The Building*************************************************"
        s+=f"\nminFloor:{self.minFloor}  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" \
           f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  maxFloor:{self.maxFloor}\n"
        for i in self.elevators:
            s+=str(self.elevators[i])
            s+="\n"
        return s


if __name__ == '__main__':
    b=Building()
    b.init_from_file("B5.json")
    # d={'_id': 0, '_speed': 0.5, '_minFloor': -2, '_maxFloor': 10, '_closeTime': 2.0, '_openTime': 2.0,
    # '_startTime': 3.0, '_stopTime': 3.0}
    # for i in b.elevators:
    #     print(b.elevators[i])
    print(b)