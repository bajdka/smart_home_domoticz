import os
import telebot
import logging

class TelegramBot(object):
    def __new__(self, profile = None):
        token = os.getenv('TELEGRAM_TOKEN')
        if (token == None):
            exit('TELEGRAM_TOKEN variable is missing!')

        telebot.logger.setLevel(logging.INFO)
        return telebot.TeleBot(token)
