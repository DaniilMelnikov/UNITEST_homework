import unittest

from py_diplom_basic import YandexDisk

class TestSomething(unittest.TestCase):
    
    def test_create_folder(self):
        YaPeople = YandexDisk('AQAAAABR1iriAADLWx8VKbkKPUEZmL-gvjaCrcU')
        self.assertEqual(YaPeople.create_folder("234"), 201)

