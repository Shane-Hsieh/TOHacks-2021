# this is just boilerplate code from whnat we did last time, modify it

import discord
client = discord.Client()

#commands
@client.event
async def on_ready():
    general_channel = client.get_channel(ClientID) #put client ID here
    await general_channel.send('@EGG')

client.run('Token') #put discord bot token here

