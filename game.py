"""
file name: game.py
description: music wordle discord bot
language: python3
author: Samson Zhang | sz7651@rit.edu
"""
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!')
song_name = 'Never Gonna Give You Up'

@bot.event
async def on_ready():
    """
    prints a message on bot startup
    """
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} has descended upon:\n'
        f'{guild.name}(id: {guild.id})\n'
        'Leggo'
    )


@bot.event
async def on_message(message):
    """
    sends a message on discord when someone sends a specific message
    :param message: message sent by user
    """
    if message.author == bot.user:
        return

    if message.content == 'commies' or message.content == 'commie':
        await message.channel.send('https://www.youtube.com/watch?v=4quwGch9jLg')
    await bot.process_commands(message)


@bot.command()
async def hi(ctx):
    """
    command, prints a message when ran
    :param ctx: context
    """
    user = ctx.message.author
    await ctx.send("shuddup " + user.display_name)


@bot.command()
async def guess(ctx, *args):
    """
    command, takes the user input and checks whether it matches the song name
    :param ctx: context
    :param args: user input
    """
    await ctx.send('(debug msg) answer: ' + song_name + '\n' +
                   '(debug msg) user input: ' + ' '.join(args))

    if len(args) == 0:
        await ctx.send("bruh you didn't even guess. Enter a song name after the command")
    elif ' '.join(args) == song_name:
        await ctx.send('wow, you exist!')
    else:
        await ctx.send('try asking again')


bot.run(TOKEN)
