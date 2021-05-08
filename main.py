import discord
from discord.ext import commands
#client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    general_channel = client.get_channel(805633741166477365) #put client ID here


#help page
client.remove_command('help')
help_page = {
    '1': "```Page 1 of 2\n-------------\nwarn\ncringe\nvalorant\nping```",
    '2': "```Page 2 of 2\n-------------\nopgg <champ name> <position>\ncounters <champ name> <position>\n"
         "build <champ name> <position>\nrunes <champ name> <position>\n"
         "skills <champ name> <position>\nwr <champ name> <position>\nprofile <summoner name>```"
}
@client.command()
async def help(ctx, pgnum):
    await ctx.send(help_page[pgnum])


# other commands
@client.command()
async def warn(ctx):
    await ctx.send('https://tenor.com/view/discord-meme-spooked-scared-mod-gif-18361254')

@client.command()
async def cringe (ctx):
    await ctx.send('https://tenor.com/view/dies-of-cringe-cringe-gif-20747133')

@client.command()
async def valorant (ctx):
    await ctx.send('https://tenor.com/view/tf2-virus-computer-team-fortress2-gif-17012348')

@client.command()
async def ping(ctx):
	await ctx.send(f'{round(client.latency * 1000)} ms')


# op.gg commands
@client.command()
async def opgg(ctx, arg1, arg2):
    await ctx.send('https://www.op.gg/champion/{}/statistics/{}'.format(arg1, arg2))
    await ctx.send(file=discord.File('./images/'+ arg1 + '.png'))

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
