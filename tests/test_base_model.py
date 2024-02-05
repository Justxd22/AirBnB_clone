import unittest, time
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_str(self):
        model = BaseModel()
        self.assertTrue(str(model).startswith("[BaseModel]"))

    def test_save(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        time.sleep(.1)
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)