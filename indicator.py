import time
import discord
from eink import eink
import logging
import RPi.GPIO as gpio

#set gpio
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(3,gpio.OUT)
gpio.setup(15,gpio.OUT)
gpio.setup(27,gpio.OUT)
gpio.setup(7,gpio.OUT)
gpio.setup(5,gpio.OUT)
gpio.setup(13,gpio.OUT)
#set all lights off
gpio.output(3,False)
gpio.output(15,False)
gpio.output(27,False)
gpio.output(7,False)
gpio.output(5,False)
gpio.output(13,False)

#setup logging
logger = logging.getLogger('mainlog')
logger.setLevel(logging.DEBUG)
stream = logging.StreamHandler()
stream.setLevel(logging.DEBUG)
logger.addHandler(stream)

#############
#set objects#
#############

#set discord client and intents
intents = discord.Intents.default() # set intents here but you need to set priv intents in bot interface on discord app page
intents.members = True
client = discord.Client(intents=intents)

#set display stuff
eink = eink()
whoConnect=['','','','','','']

#Ready the bot
@client.event
async def on_ready():
    print('chat id is 670001728')
    print('We have logged in as {0.user}'.format(client))
   
    for guild in client.guilds:
        if int(guild.id) == 134755712181075968:
            for member in guild.members:
                print('hi ', member.name)  #debug print name of all connected
                checkConnected(member) # check for members already connected before bot connection

#If discord members voice state changes
@client.event
async def on_voice_state_update(member, before, after):
    if member.name =='Rythm':
        print('Rythm')
    else:
        if not before.channel and after.channel:#entered server voice channels - diff from move channel
            checkConnected(member)#check monitored members to see if connected and turn on light

            whoConnectStr = ''.join(whoConnect) #list of who on converted to string
            print('who on ' + whoConnectStr)
            updateScreen(whoConnectStr)#update screen on who on

        elif before.channel and not after.channel:#left all voice channels
            checkDisconnected(member)

            whoConnectStr = ''.join(whoConnect)
            print('who o ' + whoConnectStr)
            updateScreen(whoConnectStr)

def checkConnected(member):#check who connected

    if member.id==134755248525934592 and member.voice != None:
        whoConnect[0] = member.name + ' '
        gpio.output(15,True)
    if member.id==615528881671241728 and member.voice != None:
        whoConnect[1] = member.name + ' '
        gpio.output(27,True)
    if member.id==161098456730042369 and member.voice != None:
        whoConnect[2] = member.name + ' '
        gpio.output(3,True)
    if member.id==333679716248846353 and member.voice != None:
        whoConnect[3] = member.name + ' '
        gpio.output(7,True)
    if member.id==185088377266110464 and member.voice != None:
        whoConnect[4] = member.name + ' '
        gpio.output(5,True)
    if member.id==294115977707388929 and member.voice != None:
        whoConnect[5] = member.name + ' '
        gpio.output(13,True)

def checkDisconnected(member):#check who disconnected
    if member.id==134755248525934592:
        whoConnect[0] = ''
        gpio.output(15,False)
    if member.id==615528881671241728:
        whoConnect[1] = ''
        gpio.output(27,False)
    if member.id==161098456730042369:
        whoConnect[2] = ''
        gpio.output(3,False)
    if member.id==333679716248846353:
        whoConnect[3] = ''
        gpio.output(7, False)
    if member.id==185088377266110464:
        whoConnect[4] = ''
        gpio.output(5,False)
    if member.id==294115977707388929:
        whoConnect[5] = ''
        gpio.output(13,False)

def updateScreen(string):#update screen
    eink.stringToPages(string,22)
    eink.pagesToDisplay()

client.run('Nzg0MzgwMzczMzc1MjU0NTQ5.X8odJg.otA8m8GYoyPv-2XY4gMHQrLN2rU')
