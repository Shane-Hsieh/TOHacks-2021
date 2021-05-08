# this is just boilerplate code from whnat we did last time, modify it

import discord
from discord.ext import commands
client = discord.Client()

client = commands.Bot(command_prefix = "!")

#commands
@client.event
async def on_ready():
    general_channel = client.get_channel(805633741166477365) #put client ID here

@client.command()
async def opgg(ctx):
	await ctx.send('https://op.gg')

@client.command()
async def warn(ctx):
    await ctx.send('Bruh')

@client.command()
async def cringe (ctx):
    await ctx.send('https://tenor.com/view/dies-of-cringe-cringe-gif-20747133')

@client.command()
async def args(ctx, arg1, arg2):
    await bot.say('You sent {} and {}'.format(arg1, arg2))

client.run('') #put discord bot token here
