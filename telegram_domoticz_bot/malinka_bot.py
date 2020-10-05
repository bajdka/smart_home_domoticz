
from telegram_bot import TelegramBot
from pic_api import send_random_picture
from lights_api import switch_light, set_light_color, set_light_brightness, LightCommand, HueLight, light_on

bot = TelegramBot()

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
    """
/malinkanadzis - losowa Malinka na poprawę humoru
/salon - sterowanie lampą sufitową w salonie
/go - sterowanie Hue Go [on/off/color]
/kuchnia - sterowanie lampami w kuchni
/sleepy - tylko lampka nocna
/goodbye - wyłączenie wszystkich świateł
/help - przypominajka komend
    """)


@bot.message_handler(commands=['malinkanadzis'])
def send_random_dog_picture(message):
    send_random_picture(message)


@bot.message_handler(commands=['go'])
def handle_hue_go(message):
    command_param=message.text[message.entities[0].length + 1:]

    if (command_param == 'off'):
        switch_light(message, HueLight.GO, LightCommand.OFF)
    elif (command_param == 'on'):
        switch_light(message, HueLight.GO, LightCommand.ON)
    elif (command_param == ''):
        switch_light(message, HueLight.GO, LightCommand.TOGGLE)
    else:
        set_light_color(message, HueLight.GO, command_param)


@bot.message_handler(commands=['salon'])
def handle_living_room_light(message):
    switch_light(message, HueLight.LIVING_ROOM_TOP, LightCommand.TOGGLE)

@bot.message_handler(commands=['kuchnia'])
def handle_living_room_light(message):
    switch_light(message, HueLight.KITCHEN_TOP, LightCommand.TOGGLE)


@bot.message_handler(commands=['sleepy'])
def handle_sleepy_time(message):
    switch_light(message, HueLight.BEDROOM_TOP, LightCommand.OFF)
    switch_light(message, HueLight.BEDROOM_BED, LightCommand.ON)
    set_light_brightness(message, HueLight.BEDROOM_BED, 20)


@bot.message_handler(commands=['goodbye'])
def handle_living_room_light(message):
    for light in HueLight:
        switch_light(message, light, LightCommand.OFF)
    bot.send_message(message.chat.id, 'Dobrej nocy! \U0001F319')


bot.polling()
