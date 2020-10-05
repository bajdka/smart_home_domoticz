import random
import os
from telegram_bot import TelegramBot

bot = TelegramBot()

def send_random_picture(message):
    onlyfiles = next(os.walk(os.getcwd() + '/assets'))[2]
    pic_count = len(onlyfiles)
    pic_number = random.randint(1, pic_count)
    photo = open(f"assets/{pic_number}.jpg", 'rb')
    bot.send_photo(message.chat.id, photo)