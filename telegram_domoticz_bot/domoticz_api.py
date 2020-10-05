import requests
import urllib
import telebot
from telegram_bot import TelegramBot

DOMOTICZ_API_URL = "http://192.168.1.29:8080/json.htm?"

bot = TelegramBot()
logger = telebot.logger

def get_domoticz_response(message, payload):
    response = requests.get(DOMOTICZ_API_URL, payload)
    logger.info(urllib.parse.urlencode(payload))

    if (response.json()['status'] == 'OK'):
        return response.json()
    else:
        logger.error(response.json())
        bot.send_message(message.chat.id, f"Coś poszło nie tak \U0001F605")
