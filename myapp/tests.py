# myapp/tests.py
from django.test import TestCase
from .models import MyModel

class MyModelTest(TestCase):
    def test_model_creation(self):
        obj = MyModel.objects.create(name="Test")
        self.assertEqual(obj.name, "Test")