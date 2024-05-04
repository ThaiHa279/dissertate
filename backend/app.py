# bot.py
import os
import sys

import discord
from dotenv import load_dotenv
from services.chatService import ChatService
sys.path.append('/home/thaiha/workspace/dissertate/backend') 


chat = ChatService()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents(guilds=True, messages=True, reactions=True, message_content=True))

@client.event
async def on_ready():
    print('Hello {0.user} !'.format(client))
    await client.change_presence(activity=discord.Game('👀'))

chat = ChatService()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    chat.storageMessage(message.author, message.content)
    response = chat.createRespone(message.content)
    await message.channel.send(response)

client.run(TOKEN)