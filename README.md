# WeebBot
simple python script to check if a group of friends are online and notify through the bot

# Setup

1. Download latest release : https://github.com/subzerodev/WeebBot/releases
2. Create 2 files with no extension : wifikey apikey

WARNING: Files must be made with an editor like notepad++ or vscode. Not windows notepad
NOTE: if your wifi name or password has special characters they need to be escaped i.e SuperS3cure!"£$ would have to be SuperS3cure\!\"\£\$

# wifikey
```
Description='Wifi Profile'
Interface=wlan0
Connection=wireless
Security=wpa
ESSID=YOURSSID
IP=dhcp
Key=YOURPASS
```
# apikey
```
DISCORD_BOT_KEY='YOURKEY'
```
3. Burn image to sd card using a tool like balena etcher: https://www.balena.io/etcher/
4. Once the image has burnt, unplug the sd card from pc and plug back in. Copy wifikey and apikey on to the root directory of sd card. 
5. Plug into pi and boot
6. First startup can take a while
