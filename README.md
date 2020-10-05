### Homepage
https://www.domoticz.com/

### Adding motherboard sensors
https://gadget-freakz.com/adding-motherboard-sensors-into-domoticz/

### Adding Roborock vacuum
https://github.com/rytilahti/python-miio
https://python-miio.readthedocs.io/en/latest/discovery.html#logged-tokens
https://go-home.io/devices/vacuum/xiaomi/
https://ehoco.nl/roborock-vacuum-cleaner-bedienen-domoticz/
https://github.com/mrin/domoticz-mirobot-plugin

### Adding Philips Hue
https://www.domoticz.com/wiki/Philips_Hue_Lights
Brigde IP can be found in Hue app.
Used port: 80

### Wake up TV on LAN
https://www.domoticz.com/wiki/Wake-up_On_Lan
How to check IP & MAC address: https://support.boingo.com/military/s/article/How-do-I-find-the-MAC-address-on-my-Samsung-Smart-TV
Used port: 80

### Connect with Telegram
https://www.domoticz.com/wiki/Telegram_Bot#Creating_Your_Bot_and_Getting_Your_Token
https://github.com/eternnoir/pyTelegramBotAPI

### TODO: Add Raspberry Pi camera
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/3
https://www.domoticz.com/wiki/Camera_Setup#Adding_Cameras_to_Domoticz
https://www.domoticz.com/wiki/Camera_Setup#Raspberry_PI_Camera

### Adding Zigbee2MQTT
https://grylewicz.pl/domoticz-4-budujemy-wlasna-bramke-zigbee/
https://www.zigbee2mqtt.io/getting_started/running_zigbee2mqtt.html
Worked after modifying npm path & `sudo ln -s "$(which node)" /usr/bin/node`
Checking Zigbee2MQTT service logs
```
sudo journalctl -u zigbee2mqtt.service -f
```

### Tuya devices
https://github.com/guino/tuyaha
Debugging: https://github.com/guino/tuyaha/blob/master/tools/debug_discovery.py

### Domoticz API
https://www.domoticz.com/wiki/Domoticz_API
