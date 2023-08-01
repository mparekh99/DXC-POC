"""
Tests.py
"""
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from items.forms import NameForm, addForm, updateForm
from items.views import *
from items.models import Item, GildedRose, kata_item, Normal, AgedBrie, Sulfuras, Concert, Conjured


class GildedKataTest(LiveServerTestCase):
    """Selenium Testing Class"""
    def setUp(self):
        self.options = Options()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=self.options)

    def tearDown(self):
        self.driver.close()

    def test_projectedDays_button(self):
        """Testing projected days button"""

        self.driver.get('http://127.0.0.1:8000/')

        prev_table_row = self.driver.find_elements(By.TAG_NAME, "tr")

        row_list = []
        prev_rows = len(prev_table_row)

        for row in range(2, prev_rows + 1):
            string = ""
            for column in range(2, 5):
                string = string + self.driver.find_element(
                    By.XPATH, "/html/body/div/table/tbody/tr["+
                    str(row) +"]/td["+ str(column) +"]").text
            row_list.append(string)


        # time.sleep(5)
        days = self.driver.find_element(By.NAME, "numDays")
        days.send_keys('5')


        self.driver.find_element(By.NAME, "numberDays").submit()
        #time.sleep(5)

        current_table_row = self.driver.find_elements(By.TAG_NAME, "tr")
        current_table_column = self.driver.find_elements(
            By.XPATH, "/html/body/div/table/tbody/tr[1]/th")
        print(len(current_table_row))
        print(len(current_table_column))

        num_rows = len(current_table_row)
        num_column = len(current_table_column)

        assert num_column == 4

        count = 0
        print("Testing Vals")
        for row in range(2, num_rows + 1):
            string = ""

            for column in range(2, 5):
                # print("Row is: ", row)
                # print("Column is: ", column)
                string = string + self.driver.find_element(
                    By.XPATH, "/html/body/div/table/tbody/tr["+
                    str(row) +"]/td["+ str(column) +"]").text
            print(string)
            print(row_list[count])

            if "Sulfuras" not in string:
                assert string != row_list[count]
            count = count + 1
            # print("Next Row")


    def test_addItem(self):
        """Testing addItem"""
        self.driver.get('http://127.0.0.1:8000/')

        table_old_rows = self.driver.find_elements(By.XPATH, "/html/body/div/table/tbody/tr")
        #print(table.size)
        button = self.driver.find_element(By.NAME, "adding")
        button.click()

        name = self.driver.find_element(By.NAME, "name")
        expiration = self.driver.find_element(By.NAME, "expiration")
        quality = self.driver.find_element(By.NAME, "quality")
        name.send_keys("Aged Brie")
        expiration.send_keys(6)
        quality.send_keys(3)
        #time.sleep(2)
        self.driver.find_element(By.NAME, "addingItem").submit()

        #time.sleep(1)
        table_rows = self.driver.find_elements(By.XPATH, "/html/body/div/table/tbody/tr")
        #Row is always 1 up num
        # print(len(table_rows))
        assert len(table_rows) == len(table_old_rows) + 1


    def test_upload(self):
        """Testing upload"""
        self.driver.get('http://127.0.0.1:8000/')
        table_old_rows = self.driver.find_elements(By.XPATH, "/html/body/div/table/tbody/tr")
        print(len(table_old_rows))

        self.driver.get('http://127.0.0.1:8000/upload')

        upload = self.driver.find_element(By.NAME, "Inventory")
        upload.send_keys("C:/Users/mparekh9/Downloads/test_inventory.json")

        self.driver.find_element(By.NAME, "uploading_file").submit()


        self.driver.get('http://127.0.0.1:8000/')
        table_rows = self.driver.find_elements(By.XPATH, "/html/body/div/table/tbody/tr")

        print(len(table_rows))

        assert len(table_rows) == len(table_old_rows) + 8






    def test_sellAll(self):
        """Testing sellAll button"""
        self.driver.get('http://127.0.0.1:8000/')

        # table_old_row = self.driver.find_elements(By.XPATH, "/html/body/div/table/tbody/tr")


        self.driver.find_element(By.NAME, "sellAll").submit()

        table_row = self.driver.find_elements(By.XPATH, "/html/body/div/table/tbody/tr")

        print(len(table_row))

        assert len(table_row) == 1





#https://ordinarycoders.com/blog/article/testing-django-selenium
