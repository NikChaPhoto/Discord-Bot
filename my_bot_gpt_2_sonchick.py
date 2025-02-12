import discord
import myToken

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'hallo' in message.content:
        await message.channel.send('Hello there!')

client.run(myToken.token)
