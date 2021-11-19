from unittest import TestCase
from Elevator import *
from Building import *
from CallOfElevator import *


class TestElevator(TestCase):

    def test_addfloors_stop(self):
        elev = Elevator(0,1,0,100, 1, 1, 1, 1)
        calls = [CallOfElevator("gg",1, 0, 25,0,-1),
                 CallOfElevator("gg",11, 25,28,0,-1)]
        elev.addfloorsStop(elev.fs, calls[0])
        self.assertEqual(list(elev.fs.keys())[0], 1)
        self.assertEqual(list(elev.fs.keys())[1], 30)
    def test_dis_in_floor(self):
        elev = Elevator(0, 1, 0, 100, 1, 1, 1, 1)
        x = elev.disInFloor(5)
        self.assertEqual(x, 5)
    def test_dis_in_time(self):
        elev = Elevator(0,2,0,100, 1, 1, 1, 1)
        x = elev.disInTime(10)
        self.assertEqual(x,5)
    def test_stop1(self):
        elev = Elevator(0, 1, 0, 100, 1, 2, 2, 1)
        x = elev.stop1()
        self.assertEqual(x, 6)


