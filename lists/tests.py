from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertIn(
            '<title>To-Do lists</title>',
            response.content.decode()
        )
        print(response.content)
        self.assertTrue(response.content.decode().startswith('<html>'))
        self.assertTrue(response.content.decode().endswith('</html>'))
    