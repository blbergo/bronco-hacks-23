import os
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Event handler for responding to messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('Bryan'):
        response = "Bryan smells."
        await message.channel.send(response)

# Run the bot with your token
bot.run("")
