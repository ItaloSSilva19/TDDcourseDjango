from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase):

    def test_maths_works(self):
        self.assertEqual(1 + 1, 3)