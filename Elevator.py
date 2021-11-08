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

    def __str__(self) -> str:
        return f"id:{self._id}, speed:{self._speed}, minFloor:{self._minFloor}, " \
               f"maxFloor:{self._maxFloor}, closeTime:{self._closeTime}, " \
               f"openTime:{self._openTime}, startTime:{self._startTime}, stopTime:{self._stopTime}"


