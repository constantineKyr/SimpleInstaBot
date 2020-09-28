from InstaLike import InstaLike

def main():
    
    username = ''
    password = ''
    chrome_driver_path = '/usr/local/bin/chromedriver'
    
    like = InstaLike(username, password, chrome_driver_path)
    like.hashtags(['traveler'])

if __name__ == "__main__":
    main()