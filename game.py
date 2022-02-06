"""
file name: game.py
description: movie wordle discord bot
language: python3
author: Samson Zhang | sz7651@rit.edu
"""
import os
import discord
from imdb_search import get_rand_movie
from imdb_search import check_movie
from discord.ext import commands
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!')
secret_name = get_rand_movie()
word_reveal = []


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
    init_word_reveal()


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
async def start(ctx):
    await ctx.send('Initial hint:\nReleased: ' + str(secret_name['year']))


@bot.command(help='use "!guess <movie name>" or "!guess hint" or "!guess give up"')
async def guess(ctx, *args):
    """
    command, takes the user input and checks whether it matches the secret name
    the secret name will be reset once the user gives up or gets the correct answer
    :param ctx: context
    :param args: user input
    """
    global secret_name

    await ctx.send('(debug msg) answer: ' + secret_name['title'] + '\n' +
                   '(debug msg) user input: ' + ' '.join(args))

    if len(args) == 0:
        await ctx.send("bruh you didn't even guess. Enter a movie name after the command")
        return

    if ' '.join(args) == 'give up':
        await ctx.send("Here's the correct answer: " + secret_name['title'] +
                       '\nYou dum')
        await ctx.send('use !start to start the next game')
        secret_name = get_rand_movie()
        init_word_reveal()

    elif ' '.join(args) == 'hint':
        if not check_reveals():
            reveal_word()
            await ctx.send("Here's a hint:" + display_word())
        else:
            await ctx.send("No more hints for you\n" +
                           "If I give you any more I might as well tell you the answer")

    elif check_movie(' '.join(args), secret_name):
        await ctx.send('Correct! WOW, you exist!')
        await ctx.send('use !start to start the next game')
        secret_name = get_rand_movie()
        init_word_reveal()
    else:
        await ctx.send('Incorrect, try asking again')


def check_reveals():
    length = len(word_reveal)
    count = 0

    for i in word_reveal:
        if i:
            count += 1
        if count >= length/2:
            return True

    return False


def init_word_reveal():
    global word_reveal

    for i in secret_name:
        if i == " ":
            word_reveal.append(True)
        word_reveal.append(False)

def display_word():
    word = ""
    count = 0

    for i in secret_name:
        if i == " ":
            word += i
        else:
            word += "_"
        count += 0
    return word 

def reveal_word():
    random_reveal = random.randrange(len(secret_name))

    while word_reveal[random_reveal]:
        random_reveal = random.randrange(len(secret_name))
    
    word_reveal[random_reveal] = True

    return word_reveal

bot.run(TOKEN)
