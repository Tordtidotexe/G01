import os
import discord
from discord.ext import commands
from discord import app_cammands

from sv import server_on

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


server_on()

bot.run(os.getenv('TOKEN'))
