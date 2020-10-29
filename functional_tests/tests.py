from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10
    
    
class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
        
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
        
    def test_can_start_a_list_for_one_user(self):
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
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        
        # There is still a text box inviting its to add another item. It
        # enters "Use peacock feathers to make a fly" (Peba is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on its list
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # Peba wonders whether the site will remember its list. Then it sees
        # that the site has generated a unique URL for its -- there is some
        # explanatory text to that effect.
        
    def test_multiple_users_can_start_lists_at_different_urls(self):
    # Peba starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
           
        # It notices that its list has a unique URL
        peba_list_url = self.browser.current_url
        self.assertRegex(peba_list_url, '/lists/.+')
           
        # Now a new user, Aspone, comes along to the site.
          
        ## We use a new browser to make sure that no information
        ## of Peba's is coming through from cookies ect
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        # Aspone visits the home page. There is no sign of Peba's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        
        # Aspone starts a new list by entering a new item.
        # It is less interesting than Peba...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        
        # Aspone gets its own unique URL
        aspone_list_url = self.browser.current_url
        self.assertRegex(aspone_list_url, '/lists/.+')
        self.assertNotEqual(aspone_list_url, peba_list_url)
        
        # Again, there is no trace of Peba's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)


        # Satisfied, they both go back to sleep