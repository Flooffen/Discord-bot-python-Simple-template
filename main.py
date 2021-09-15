import discord
from discord.ext import commands

client = commands.Bot(command_prefix=("-"))


@client.event
async def on_ready():
    print("bot started")


@client.command()
async def hi(ctx):
    await ctx.send("hello")


@client.command()
async def slap(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} slap {member.mention}")


token_file = open('token.txt')
token = token_file.readlines()[0].strip("\n")
token_file.close()
client.run(token)
