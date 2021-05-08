# this is just boilerplate code from whnat we did last time, modify it

import discord
client = discord.Client()

#commands
@client.event
async def on_ready():
    general_channel = client.get_channel(812470218106470453) #put client ID here
    await general_channel.send(hackernews_module.tophn_wrapper(0))

client.run('token') #put discord bot token here