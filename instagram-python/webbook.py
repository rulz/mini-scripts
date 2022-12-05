from instabot import Bot
import os

os.system("rm -rf config")
bot  = Bot()
bot.login(username='elrulz', password='Elrulz1212!')

# image = 'img/img-bot.jpeg'
# bot.upload_photo(image, caption="Test 1")
dir_image = 'img/'

count = 1
for image in os.listdir(dir_image):
    bot.upload_photo(dir_image + image, caption="Prueba {}".format(count))
    count += 1
