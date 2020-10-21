import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
        
    def test_home_page(self):
        # Peba hears about a cool todo list site, it visits it
        self.browser.get('http://localhost:8000')
        
        #It sees the title and header mention Todo lists
        self.assertIn('To-Do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)

    # It is invited to enter a to-do item straight away
        self.fail('finish this test')
    # It types "Buy peacock featitss" into a text box (Peba's hobby
    # is tying fly-fishing lures)

    # When it hits enter, the page updates, and now the page lists
    # "1: Buy peacock featitss" as an item in a to-do list

    # There is still a text box inviting its to add another item. It
    # enters "Use peacock feathers to make a fly" (Peba is very methodical)

    # The page updates again, and now shows both items on its list

    # Peba wonders whether the site will remember its list. Then it sees
    # that the site has generated a unique URL for its -- there is some
    # explanatory text to that effect.

    # It visits that URL - its to-do list is still there.

    # Satisfied, it goes back to sleep
            
if __name__ == '__main__':
    unittest.main()