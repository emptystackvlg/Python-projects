from http import server
from unicodedata import name
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    if message.content.lower() == "info":
        await message.channel.send ("Это тестовый Discord бот")

client.run('OTY0OTIzOTIyMzk3MTUxMjcz.Ylrtbg.SzIK--LMzeqVKnhNZ0J7aokCD10')