# Automate Instagram
# pip install instapy
from instapy import *
# Make a login
s = InstaPy(username='Enter User', password='Enter Pass')
s.login()
# Like a Post by tags
s.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
s.like_by_tags(['Car', 'bmw'], amount=5)
# Like a Post by Feed
s.like_by_feed(amount=5)
# Don't like the post
s.set_dont_like(['boring'])
# Comment on Post
s.set_do_comment(True, percentage=100)
s.set_comments(['Nice!', 'Cool', 'Awesome'])
# Follow the user
s.set_do_follow(True, percentage=100)
# Follow by Tags
s.follow_by_tags(['Car', 'bmw'], amount=5)
# Follow by usernames
s.follow_by_list(['username1', 'username2'], times=1, sleep_delay=300, interact=False)
# Follow Someone Friends
s.follow_user_followers(['username1', 'username2'], amount=5, randomize=False, interact=False)
# Follow Likers of Post
s.follow_likers(['username1' , 'username2'], photos_grab_amount = 3, follow_likers_per_photo = 2, randomize=True, sleep_delay=300, interact=False)
# Follow Commenters of Post
s.follow_commenters(['username1' , 'username2'], photos_grab_amount = 3, follow_commenters_per_photo = 2, randomize=True, sleep_delay=300, interact=False)
# Unfollow user
s.unfollow_users(amount=10, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=12*60*60, sleep_delay=300)
# Like, Comment Follow
s.interact_by_URL(urls = ["url1", "url2"], randomize=True, interact=False, media='Photo')
# End Session 
s.end()