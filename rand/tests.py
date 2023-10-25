from django.test import TestCase

from rand.models import Bandname, Album
from rand.views import getrandname, getrandalbum

class BandnameTestCase(TestCase):
    def setUp(self):
        Bandname.objects.create(
            bandname_text="Darth Brooks",
            openai_prompt="Darth Vader wearing a cowboy hat playing an acoustic guitar",
        )

    def test_random(self):
        print(getrandname())

class AlbumTestCase(TestCase):
    def setUp(self):
        Album.objects.create(
            name="Baby Cheeses In The Manger",
            openai_prompt="A block of cheese in the biblical setting of the manger with the three wise men",
        )

    def test_random(self):
        print(getrandalbum())
