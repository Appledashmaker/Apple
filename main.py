import discord
import os
from keep_alive import keep_alive
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$twi'):
        await message.channel.send('Follow my master @MLPDJGAMERAPPLEDASHFIM!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$nudes'):
        await message.channel.send('WHO POSTED MY NUDES ON TWITTER DOT COM!')
  


keep_alive()
client.run(os.getenv('TOKEN'))