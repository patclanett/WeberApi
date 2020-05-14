from django.test import TestCase
from .models import Villager

# Create your tests here.

class VillagerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Villager.objects.create(name = 'Weber')
        Villager.objects.create(personality = 'Lazy')
        Villager.objects.create(birthday = '06/30')

    def test_name(self):
        test = Villager.objects.get(id=1)
        expected_obj = f'{test.name}'
        self.assertEquals(expected_obj, 'Weber')

    def test_personality(self):
        test = Villager.objects.get(id=2)
        expected_obj = f'{test.personality}'
        self.assertEquals(expected_obj, 'Lazy')

    def test_birthday(self):
        test = Villager.objects.get(id=3)
        expected_obj = f'{test.birthday}'
        self.assertEquals(expected_obj, '06/30')

