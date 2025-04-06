import os
import discord
#from discord.app_commands import describe
from discord.ext import commands
#from discord import app_commands

from sv import server_on

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot is online')

#แจ้งเตือนคนเข้า
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1356879499362439345)
    text = f"Welcome!!, {member.mention}!"
    embed = discord.Embed(title= 'Welcome!!',
                          description = text,
                           color = 0x5dade2)
    await channel.send(text)
    await channel.send(embed=embed)
#ส่งข้อความ
@bot.event
async def on_message(message):
    mes = message.content
    if mes == 'G say hi!':
        await message.channel.send(f'Hi, {message.author.mention}!')
    elif mes == 'hello G!':
        await message.channel.send('Hello,' + str(message.author.mention))

        await bot.process_commands(message)

#commands
@bot.command()
async def pv(cnx):
    await cnx.send("https://www.roblox.com/share?code=00bdce6324590b4f83aa0e326ad8aeca&type=Server")



server_on()

bot.run(os.getenv('TOKEN'))
