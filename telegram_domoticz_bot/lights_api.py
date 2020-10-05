from domoticz_api import get_domoticz_response
from telegram_bot import TelegramBot
from enum import Enum


class LightCommand(Enum):
    ON = 'On'
    OFF = 'Off'
    TOGGLE = 'Toggle'


class HueLight(Enum):
    GO = {'name': 'Hue Go', 'idx': 7}
    BEDROOM_TOP = {'name': 'Sypialnia - lampa sufitowa', 'idx': 9}
    BEDROOM_BED = {'name': 'Sypialnia - lampka nocna', 'idx': 8}
    LIVING_ROOM_TOP = {'name': 'Salon - lampa sufitowa', 'idx': 10}
    PLAY_1 = {'name': 'Hue Play 1', 'idx': 11}
    PLAY_2 = {'name': 'Hue Play 2', 'idx': 12}
    KITCHEN_TOP = {'name': 'Kuchnia', 'idx': 46}


bot = TelegramBot()


def switch_light(message, light, command):
    response = get_domoticz_response(message, {
        'type': 'command',
        'param': 'switchlight',
        'idx': light.value['idx'],
        'switchcmd': command.value
    })

    success_message = f"{light.value['name']} turned {light_on(message, light).lower()}! \U00002728"
    bot.send_message(message.chat.id, success_message)


def set_light_brightness(message, light, brighness_level):
    response = get_domoticz_response(message, {
        'type': 'command',
        'param': 'setcolbrightnessvalue',
        'idx': light.value['idx'],
        'hue': 274,
        'brightness': brighness_level,
        'iswhite': 'false'
    })
    success_message = f"{light.value['name']} changed brightness! \U0001F48E"
    bot.send_message(message.chat.id, success_message)


def set_light_color(message, light, color):
    rgb = {
        'blue': '{"m":3,"t":0,"r":0,"g":0,"b":50,"cw":0,"ww":0}',
        'red': '{"m":3,"t":0,"r":50,"g":0,"b":0,"cw":0,"ww":0}',
        'green': '{"m":3,"t":0,"r":0,"g":50,"b":0,"cw":0,"ww":0}',
    }

    if color in rgb.keys():
        response = get_domoticz_response(message, {
            'type': 'command',
            'param': 'setcolbrightnessvalue',
            'idx': light.value['idx'],
            'color': rgb[color],
            'brightness': 360
        })
        success_message = f"{light.value['name']} changed colour! \U0001F308"
        bot.send_message(message.chat.id, success_message)
    else:
        bot.send_message(
            message.chat.id, f"Dostępne kolory to:\n{', '.join(map(str, rgb.keys()))}")


def light_on(message, light):
    # Returns On/Off
    response = get_domoticz_response(
        message, {'type': 'devices', 'filter': 'light', 'used': 'true', 'order': 'Name'})
    lights = response['result']
    test = [device['Status']
            for device in lights if int(device['idx']) == light.value['idx']]
    return test[0]
