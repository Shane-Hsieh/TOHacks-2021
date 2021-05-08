import discord

from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.command()
async def ping(ctx):
	await ctx.send(f'{round(client.latency * 1000)} ms')

@client.command()
async def jerome(ctx):
	await ctx.send('but whyyyyy 😩')

client.run('ODQwNjIxMTQ2MDgzOTUwNjIy.YJa3cw.ZO_LkLsaKwoJrl8XcrSqHiXG80s')
