#!/usr/bin/python3


"""testing the file storage call"""\

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import unittest
import os


class Test_File_Storage(unittest.TestCase):

    def setUp(self):
        self.base = BaseModel()

    def test_istance(self):
        self.assertIsInstance(storage, FileStorage)

    def test_file_path(self):
        file_base = "file.json"
        self.assertIsInstance(file_base, str)
        self.assertEqual(storage._FileStorage__file_path, file_base)
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    def test_objects(self):
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_all(self):
        new = storage.all()
        self.assertIsInstance(new, dict)

    def test_save(self):
        storage.save()
        self.assertTrue(os.path.exists(storage._FileStorage__file_path))
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_relaod(self):
        self.base.save()
        myobjs = storage.all()
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(myobjs[key].to_dict(), value.to_dict())


if __name__ == "__main__":
    unittest.main()
