from InstaLogin import InstaLogin
import random
import time

class InstaFollow(InstaLogin):
    
    def __init__(self, username, password, chrome_driver_path):
        super().__init__(username, password, chrome_driver_path)

    def hashtags(self, hashtag_list):
        tag = -1
        for hashtag in hashtag_list:
            self.driver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
            time.sleep(random.randint(1,2))
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div').click()
            for x in range(0,20):
                time.sleep(random.randint(5,10))
                self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                time.sleep(random.randint(5,10))
                if x == 0:
                    self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()
                else:
                    self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()