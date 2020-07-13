
import discord
from discord.ext import commands, tasks
import random
from itertools import cycle

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Type .rules for options'))
    print("Bot is ready.")

@client.command(aliases=['r'])
async def rock(ctx):
    number = random.randint(1,3)
    if number == 1:
        await ctx.send("Bot picked rock, IT'S A TIE!")
    elif number == 2:
        await ctx.send('Bot picked paper, YOU LOST!')
    elif number == 3:
        await ctx.send('Bot picked scissors, YOU WIN!')

@client.command(aliases=['p'])
async def paper(ctx):
    number = random.randint(1,3)
    if number == 1:
        await ctx.send('Bot picked rock, YOU WIN!')
    elif number == 2:
        await ctx.send("Bot picked paper, IT'S A TIE!")
    elif number == 3:
        await ctx.send('Bot picked scissors, YOU LOST!')

@client.command(aliases=['s'])
async def scissors(ctx):
    number = random.randint(1,3)
    if number == 1:
        await ctx.send('Bot picked rock, YOU LOST!')
    elif number == 2:
        await ctx.send("Bot picked paper, YOU WIN!")
    elif number == 3:
        await ctx.send("Bot picked scissors, IT'S A TIE!")

@client.command()
async def rules(ctx):
    await ctx.send("To play Rock Paper Scissors type in the following commands: \n Rock = .rock or .r \n Paper = .paper or .p \n Scissors = .scissors or .s \n Adam is a weeb lul")



client.run('NzEyNzk3NzgyMDc5MDQ1Njcy.XurdAA.LpW2lPUsI6dBUGYrDClCmYiZXls
')