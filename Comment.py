from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
import time
import random
from selenium.common import exceptions

URL = "https://www.instagram.com/accounts/login/"


class Comment:
    def __init__(self):
        #set up selenium
        self.options = ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)

    def login(self, username, pw):
        self.driver.get(URL)
        time.sleep(3)
        #INPUT USERNAME
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
        #INPUT PASSWORD
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(pw, Keys.ENTER)
        time.sleep(8)

    def comment_like(self, username, lst_of_comments, keyword):
        #go to # by given keyword
        self.driver.get(f"https://www.instagram.com/explore/tags/{keyword}/")
        time.sleep(10)
        #get all posts on site
        self.find_posts = self.driver.find_elements(By.XPATH, '//div[@class="_aabd _aa8k  _al3l"]//ancestor::a')
        time.sleep(1)
        # go through each post, look if already commented if not comment and like
        for element in self.find_posts:
            self.can_comment = True
            #OPEN POST
            element.click()
            time.sleep(3)
            self.comments_of_posts= self.driver.find_elements(By.XPATH, '//span[@class="xt0psk2"]//ancestor::a')
            #BREAK IF ALLREADY COMMENTED
            for comments in self.comments_of_posts:
                self.commented_account = comments.text
                if self.commented_account == username:
                    self.can_comment = False
                    break
            if self.can_comment: #and random.randint(0,1) ==1:
                #ADD COMMENT AND POST İT
                for i in range(0, 22):
                    try:
                        self.driver.find_element(By.XPATH, '//div[@class="_akhn"]//textarea' ).send_keys(random.choice(lst_of_comments))
                        self.driver.find_element(By.XPATH, '//div[@class=" _am-5"]').click()
                        break
                    except exceptions.StaleElementReferenceException or NoSuchElementException:
                        pass


                #CLİCK LİKE BUTTON
                try:
                    self.driver.find_element(By.XPATH, '//span//ancestor::div[@class="x6s0dn4 x78zum5 xdt5ytf xl56j7k"]').click()
                except NoSuchElementException:
                    pass

            time.sleep(3)
            #CLOSE POST
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
