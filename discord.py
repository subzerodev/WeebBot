import time

import discord
from telegram import Bot

client = discord.Client()

@client.event
async def on_ready():
    print('chat id is 670001728')
    print('We have logged in as {0.user}'.format(client))

    #bot.send_message(chat_id=-1001268968056, text='hi')


@client.event
async def on_message(message):
    

@client.event
async def on_voice_state_update(member, before, after):
    if member.name =='Rythm':
        print('Rythm')
    else:
        if not before.channel and after.channel:
            print(member.name + ' has entered ' + after.channel.name)
            
        elif before.channel and not after.channel:
            print(member.name + ' has left ' + before.channel.name)
            
        elif before.channel != after.channel:
            print(member.name + ' has moved to ' + after.channel.name)
            
        elif after.self_deaf or after.self_deaf:
            if client.get_channel != 809917287393787924:
                print(member.name + ' has deafened')
                
        elif before.self_deaf or before.self_deaf:
            print(member.name + ' has undeafened')
            
        elif after.self_mute or after.mute:
            print(member.name + ' has muted')
            
        elif before.self_mute or before.mute:
            print(member.name + ' has unmuted')
            

client.run('BOTAPIKEY')
