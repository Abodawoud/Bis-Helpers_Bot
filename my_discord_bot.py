#!/usr/bin/python3

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='you', help='Get information about you.')
async def get_your_info(ctx):
    response = '''
    Information about you:
    '''
    await ctx.send(response)

bot_token = 'Your token'
bot.run(bot_token)
