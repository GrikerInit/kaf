import discord
from discord.ext import commands
import os
 
client = discord.Client()
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready():
 print('Bot is ready')

hug1 = "hug me"

@client.event
async def on_message(message):
    if message.content == hug1:
        await message.channel.send('No Never')

client.run(token)