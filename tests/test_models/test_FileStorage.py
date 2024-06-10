#!/usr/bin/python3
from models.engine.file_storage import FileStorage
import unittest


class Test_File_Storage(unittest.TestCase):

    def setUP(self):
        self.FS = FileStorage()
