from InstaUnfollow import InstaUnfollow
from InstaFollow import InstaFollow
from InstaLike import InstaLike

def main():
    
    username = ''
    password = ''
    chrome_driver_path = '/usr/local/bin/chromedriver'

    '''unfollows users that don't follow back by given csv's from IGExport'''
    #followersFile = ''
    #unfollowersFile = ''
    #unfollow = InstaFollow(username, password, chrome_driver_path,5)
    #unfollow.unfollowNonFollowers(True, 'data/followings/'+followersFile+'.csv','data/followers/'+unfollowersFile+'.csv')

    '''follows users by given hashtags'''
    #follow = InstaFollow(username, password, chrome_driver_path)
    #follow.hashtags(['hills']) # will do 20 follows in total

    '''likes user images by given hastags'''
    #like = InstaLike(username, password, chrome_driver_path)
    #like.hashtags(['travel']) # will do 20 likes in total

if __name__ == "__main__":
    main()