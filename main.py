import discord
from discord.ext import commands
import os
 
client = discord.Client()
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready():
 print('Bot is ready')

@client.event
async def on_message(message):
    if message.content == "hug":
        await message.channel.send('I will never hug anyone')

client.run(token)