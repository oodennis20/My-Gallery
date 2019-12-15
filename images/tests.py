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
    
    def test_search_by_category(self):
        self.drinks.save()
        images = Image.search_by_category('fun')
        self.assertTrue(len(images) > 0)

    def test_view_location(self):
        self.drinks.save()
        location = Image.view_location(self.kenya)
        self.assertTrue(len(location) > 0)

    def test_view_category(self):
        self.drinks.save()
        categories = Image.view_category(self.fun)
        self.assertTrue(len(categories) > 0)

class categoriesTest(TestCase):
    def setUp(self):
        self.music = categories(name='music')

    def test_instance(self):
        self.music.save()
        self.assertTrue(isinstance(self.music, categories))

class LocationTest(TestCase):
    def setUp(self):
        self.kenya = Location(name='Kenya')

    def test_instance(self):
        self.kenya.save()
        self.assertTrue(isinstance(self.kenya, Location))