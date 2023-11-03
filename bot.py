import discord
from discord.ext import commands

# Define your intents
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True  # Add this line to allow reading message content

# Create an instance of the bot with the specified intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Event handler for responding to messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if the message starts with 'l'
    if message.content.startswith('Bryan'):
        response = "Bryan smells."
        await message.channel.send(response)

# Run the bot with your token
bot.run("")
