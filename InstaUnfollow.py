from InstaLogin import InstaLogin
import helpers
import sys
import time

class InstaFollow(InstaLogin):
    
    def __init__(self, username, password, chrome_driver_path, unfollowing_speed):
        super().__init__(username, password, chrome_driver_path)
        self.unfollowing_speed = unfollowing_speed
        
    def unfollowNonFollowers(self, readCsv = False, followingsPath = None, followersPath = None):
        if readCsv and followingsPath != '' and followersPath != '':
            following_accounts = helpers.readCsvFile(followingsPath)
            followers_accounts = helpers.readCsvFile(followersPath)
        else:
            following_accounts = self.getFollowings()
            followers_accounts = self.getFollowers()
        not_following_back = [user for user in following_accounts if user not in followers_accounts]
        self.unfollow(not_following_back)

    def getFollowings(self):    
        following_accounts = []
        following_number = self.driver.find_element_by_xpath( '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text.replace(',','').replace(' following','').strip()
        print("total following:" +following_number)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        time.sleep(self.unfollowing_speed)
        while len(following_accounts) != int(following_number):
            following_accounts = self.get_accounts()
        
        return following_accounts

    def getFollowers(self):
        followers_accounts = []
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(self.unfollowing_speed)
        followers_accounts = self.get_accounts()

        return followers_accounts

    def unfollow(self, not_following_back):
        count = 0
        for name in not_following_back:
            if count < 250:
                try:
                    count = count+1
                    self.driver.get('https://www.instagram.com/'+name+'/')
                    time.sleep(self.unfollowing_speed)
                    self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
                    time.sleep(self.unfollowing_speed)
                    self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
                    time.sleep(self.unfollowing_speed)
                    print("Unfollowed "+str(count)+" : " +name)
                except:
                    print("error")
                    count = count-1
                    continue
        print("Total Unfollows: "+str(count))

    def get_accounts(self):
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        prev_height, height = 0, 1
        while prev_height != height:
            prev_height = height
            time.sleep(5)
            height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
        
        return names