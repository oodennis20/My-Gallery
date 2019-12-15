from django.test import TestCase
from .models import *
# Create your tests here.

class ImageTest(TestCase):

    # def class instance setup for the project
    def setUp(self):
        self.kenya = Location.objects.create(name='Kenya')
        self.fun = categories.objects.create(name='fun')
        self.music = categories.objects.create(name='Music')

        self.drinks = Image.objects.create(name='drinks', location=self.kenya,  description='picture of drinks')

        self.drinks.categories.add(self.fun)
        

    # def a testcase for instance of the drinks class
    def test_instance(self):
        self.drinks.save()
        self.assertTrue(isinstance(self.drinks, Image))

    def test_delete_image(self):
        self.drinks.save()
        self.drinks.delete()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_update(self):
        self.drinks.save()
        self.drinks.name = 'MoreDrinks'
        self.assertTrue(self.drinks.name == 'MoreDrinks')

    def test_all_images(self):
        self.drinks.save()
        images = Image.all_images()
        self.assertTrue(len(images) > 0)