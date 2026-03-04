from instabot import Bot

bot = Bot()
bot.login(username = "python, password = "1234")
bot.follow('wscubetechindia')
bot.upload_photo("path", caption = " i love pthon")
bot.unfollow("any one you don't want to follow")
bot.send_message(" i love my self",["to any everyone"])
followers = bot.get_user_followers("any one add name of there account")
for follower in followers:
          print(bot.get_user_info(follower))
following = bot.get_user_following("jone_pthon08")
for Following in following:
          print(bot.get_user_info("jone_pthon08"))
