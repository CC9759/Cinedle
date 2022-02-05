"""
file name: game.py
description: movie wordle discord bot
language: python3
author: Samson Zhang | sz7651@rit.edu
"""
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!')
secret_name = 'Never Gonna Give You Up'
hints = ['released: 1987', 'artist: Rick Astley', 'album: Whenever You Need Somebody']


@bot.event
async def on_ready():
    """
    prints a message on bot startup
    """
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                        name='my roommate sleep'))

    print(
        f'{bot.user} has descended upon:\n'
        f'{guild.name}(id: {guild.id})\n'
        'Leggo, bot started\n'
        '.-.-.-..-.-.-.-.-.'
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


@bot.command(help='use "!guess <song name>" or "!guess hint" or "!guess give up"')
async def guess(ctx, *args):
    """
    command, takes the user input and checks whether it matches the song name
    :param ctx: context
    :param args: user input
    """
    # initialize the name and hints
    # song_name = something string
    # hint = something list

    # await ctx.send('(debug msg) answer: ' + song_name + '\n' +
    #               '(debug msg) user input: ' + ' '.join(args))

    if len(args) == 0:
        await ctx.send("bruh you didn't even guess. Enter a song name after the command")
        return
    if ' '.join(args) == 'give up':
        await ctx.send("Here's the correct answer: " + secret_name +
                       '\nYou dum')
    elif ' '.join(args) == 'hint':
        if len(hints) != 0:
            await ctx.send("Here's a hint:\n" + hints.pop(0))
        else:
            await ctx.send("No more hints for you\n" +
                           "If I give you any more I might as well tell you the answer")
    elif ' '.join(args) == secret_name:
        await ctx.send('Correct! WOW, you exist!')
    else:
        await ctx.send('Incorrect, try asking again')

@bot.command()
async def play(ctx):
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)
    
    player = await vc.create_ytdl_player(url)
    player.start()

bot.run(TOKEN)
