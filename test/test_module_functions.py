import unittest
import time
import tkinter
from digital_clock import main


class TestModuleFunctions(unittest.TestCase):
    TIME_LABEL = None
    DATE_LABEL = None
    WINDOW = None

    @classmethod
    def setUpClass(cls):
        cls.WINDOW = tkinter.Tk()
        cls.TIME_LABEL = tkinter.Label(master=cls.WINDOW)
        cls.DATE_LABEL = tkinter.Label(master=cls.WINDOW)

    def test_update_function_1(self):
        main.update(self.TIME_LABEL, self.DATE_LABEL, self.WINDOW)
        self.assertEqual(self.TIME_LABEL.cget('text'), time.strftime("%H:%M:%S"))
        self.assertEqual(self.DATE_LABEL.cget('text'), time.strftime("%a, %d %b %Y"))

    def test_update_function_2(self):
        time_compare = time.strftime("%H:%M:%S")
        time.sleep(1)
        main.update(self.TIME_LABEL, self.DATE_LABEL, self.WINDOW)
        self.assertNotEqual(self.TIME_LABEL.cget('text'), time_compare)
