# this is just boilerplate code from whnat we did last time, modify it

import discord
from discord.ext import commands
#client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    general_channel = client.get_channel(805633741166477365) #put client ID here

# warn
@client.command()
async def warn(ctx):
    await ctx.send('https://tenor.com/view/discord-meme-spooked-scared-mod-gif-18361254')

@client.command()
async def cringe (ctx):
    await ctx.send('https://tenor.com/view/dies-of-cringe-cringe-gif-20747133')

@client.command()
async def valorant (ctx):
    await ctx.send('https://tenor.com/view/tf2-virus-computer-team-fortress2-gif-17012348')

# op.gg commands
@client.command()
async def opgg(ctx, arg1, arg2):
	await ctx.send('https://www.op.gg/champion/{}/statistics/{}'.format(arg1, arg2))

@client.command()
async def counters(ctx, arg1, arg2):
    await ctx.send('https://na.op.gg/champion/{}/statistics/{}/matchup'.format(arg1, arg2))

@client.command()
async def build(ctx, arg1, arg2):
    await ctx.send('https://na.op.gg/champion/{}/statistics/{}/item'.format(arg1, arg2))

@client.command()
async def runes(ctx, arg1, arg2):
    await ctx.send('https://www.op.gg/champion/{}/statistics/{}/rune'.format(arg1, arg2))

@client.command()
async def skills(ctx, arg1, arg2):
    await ctx.send('https://www.op.gg/champion/{}/statistics/{}/skill'.format(arg1, arg2))

@client.command()
async def wr(ctx, arg1, arg2):
    await ctx.send('https://www.op.gg/champion/{}/statistics/{}/trend'.format(arg1, arg2))

@client.command()
async def profile(ctx, arg1):
    await ctx.send('https://na.op.gg/summoner/userName={}'.format(arg1))

client.run('') #put discord bot token here
