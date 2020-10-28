from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
    
    
class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
        
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Peba hears about a cool todo list site, it visits it
        self.browser.get(self.live_server_url)
        
        #It sees the title and header mention Todo lists
        self.assertIn('To-Do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)

        # It is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        
        # It types "Buy peacock featitss" into a text box (Peba's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')
        
        # When it hits enter, the page updates, and now the page lists
        # "1: Buy peacock featitss" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        # There is still a text box inviting its to add another item. It
        # enters "Use peacock feathers to make a fly" (Peba is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on its list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Peba wonders whether the site will remember its list. Then it sees
        # that the site has generated a unique URL for its -- there is some
        # explanatory text to that effect.
        self.fail('finish this test')

        # It visits that URL - its to-do list is still there.

        # Satisfied, it goes back to sleep
                