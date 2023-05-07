import unittest
import car_speed_fun

class TestCarSpeed(unittest.TestCase):

    #@classmethod
    #def beforeAll(cls):
    #    print("Test suit 1 started!")
    
    #@classmethod
    #def afterAll(cls):
    #    print("Test suit 1 completed!")

    def setUp(self) -> None:
        print("Test case is started")
    def tearDown(self) -> None:
        print("Test case is ended")
    
    def test_low_speed(self):
        self.assertEqual(car_speed_fun.car_speed_level(20), "Low!!")

    def test_normal_speed(self):
        self.assertEqual(car_speed_fun.car_speed_level(75), "Normal!!")

    def test_high_speed(self):
        self.assertEqual(car_speed_fun.car_speed_level(160), "High!!")

    def test_vhigh_speed(self):
        self.assertEqual(car_speed_fun.car_speed_level(210), "V.High!!")

class TestInvalidCarSpeed(unittest.TestCase):

    def setUp(self) -> None:
        print("Invalid Test case is started")
    def tearDown(self) -> None:
        print("Invalid Test case is ended")

    def test_Invalid_speed1(self):
        self.assertEqual(car_speed_fun.car_speed_level(-1), "Invalid!!")

    def test_Invalid_speed2(self):
        self.assertEqual(car_speed_fun.car_speed_level(221), "Invalid!!")


if __name__ == '__main__':
    unittest.main()
