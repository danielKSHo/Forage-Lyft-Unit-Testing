import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class TestCapuletEngine(unittest.TestCase):
    
    def test_needs_service_true(self):
        self.assertTrue(CapuletEngine(30002, 1).needs_service())
        self.assertTrue(CapuletEngine(-1, -30002).needs_service())
        self.assertTrue(CapuletEngine(50234, 14123).needs_service())        
    
    def test_needs_service_false(self):
        self.assertFalse(CapuletEngine(30001, 1).needs_service())
        self.assertFalse(CapuletEngine(-1, 30001).needs_service())
        self.assertFalse(CapuletEngine(53453, 61532).needs_service())
        
class TestWilloughbyEngine(unittest.TestCase):    
    
    def test_needs_service_true(self):
        self.assertTrue(WilloughbyEngine(60002, 1).needs_service())
        self.assertTrue(WilloughbyEngine(-1, -60002).needs_service())
        self.assertTrue(WilloughbyEngine(80234, 14123).needs_service())        
    
    def test_needs_service_false(self):
        self.assertFalse(WilloughbyEngine(60001, 1).needs_service())
        self.assertFalse(WilloughbyEngine(-1, -60001).needs_service())
        self.assertFalse(WilloughbyEngine(7354, 56456).needs_service())

class TestSternmanEngine(unittest.TestCase):

    def test_needs_service_true(self):
        self.assertTrue(SternmanEngine(True).needs_service())   
    
    def test_needs_service_false(self):
        self.assertFalse(SternmanEngine(False).needs_service())

class TestSpindlerBattery(unittest.TestCase):

    def test_needs_service_true(self):
        current_date = datetime.today().date()
        
        last_service_date = current_date.replace(year=current_date.year - 3)
        self.assertTrue(SpindlerBattery(current_date, last_service_date).needs_service())
        
        last_service_date = current_date.replace(year=current_date.year - 7)
        self.assertTrue(SpindlerBattery(current_date, last_service_date).needs_service())
        
        last_service_date = current_date.replace(year=current_date.year - 4)
        self.assertTrue(SpindlerBattery(current_date, last_service_date).needs_service())        
    
    def test_needs_service_false(self):
        current_date = datetime.today().date()
        
        last_service_date = current_date.replace(year=current_date.year)
        self.assertFalse(SpindlerBattery(current_date, last_service_date).needs_service())

        last_service_date = current_date.replace(year=current_date.year + 2)
        self.assertFalse(SpindlerBattery(current_date, last_service_date).needs_service())

        last_service_date = current_date.replace(year=current_date.year - 2)
        self.assertFalse(SpindlerBattery(current_date, last_service_date).needs_service())

class TestNubbinBattery(unittest.TestCase):

    def test_needs_service_true(self):
        current_date = datetime.today().date()
        
        last_service_date = current_date.replace(year=current_date.year - 5)
        self.assertTrue(NubbinBattery(current_date, last_service_date).needs_service())
        
        last_service_date = current_date.replace(year=current_date.year - 7)
        self.assertTrue(NubbinBattery(current_date, last_service_date).needs_service())
        
        last_service_date = current_date.replace(year=current_date.year - 6)
        self.assertTrue(NubbinBattery(current_date, last_service_date).needs_service())        
    
    def test_needs_service_false(self):
        current_date = datetime.today().date()
        
        last_service_date = current_date.replace(year=current_date.year)
        self.assertFalse(NubbinBattery(current_date, last_service_date).needs_service())

        last_service_date = current_date.replace(year=current_date.year + 2)
        self.assertFalse(NubbinBattery(current_date, last_service_date).needs_service())

        last_service_date = current_date.replace(year=current_date.year - 2)
        self.assertFalse(NubbinBattery(current_date, last_service_date).needs_service())

if __name__ == '__main__':
    unittest.main()