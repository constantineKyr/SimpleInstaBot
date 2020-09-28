from InstaFollow import InstaFollow
from InstaLike import InstaLike

def main():
    
    username = ''
    password = ''
    chrome_driver_path = '/usr/local/bin/chromedriver'

    #follow = InstaFollow(username, password, chrome_driver_path)
    #follow.hashtags(['hills']) # will do 20 follows in total

    #like = InstaLike(username, password, chrome_driver_path)
    #like.hashtags(['travel']) # will do 20 likes in total

if __name__ == "__main__":
    main()