#Basic UserBot used to respond when im offline
#Feel free to use, make sure you give credit. :)
#Created by Sanjay
#Discord.py Library

import discord
from discord.ext import commands
import random
import logging
logging.basicConfig(level=logging.INFO) #Logs command prompt


#Basic Bot Info
description = '''NAME OF BOT'''
prefix = '''PREFIX'''
bot = False
bot = commands.Bot(command_prefix='PREFIX', description=description)


@bot.event
async def on_ready():
    print('------ Logged in as -----')
    print('Username: ' + bot.user.name)
    print('UserID: ' + bot.user.id)
    print('Prefix: ' + prefix)
    print('----- Output -----')



@bot.command(description='ping')
async def ping():
    """Ping"""
    await bot.say('Pong')

@bot.group(pass_context=True)
async def about(ctx):
    """General Info"""
    if ctx.invoked_subcommand is None:
        await bot.say("Invoked Sub-Command")



bot.run("YOUR TOKEN HERE")