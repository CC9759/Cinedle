"""
file name: game.py
description: movie wordle discord bot
language: python3
author: Samson Zhang | sz7651@rit.edu, Celina Chen
"""
from curses.ascii import isalpha
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
word_blanks = []


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
    init_hint = 'Initial hints: '
    await ctx.send(init_hint)


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
    """
    checks if the number of characters revealed has reached the limit of half the word

    :return: true if the number of revealed chars is more than or equal to half of the movie name
    """
    length = len(word_blanks)
    count = 0

    for i in word_blanks:
        if isalpha(i) or i == " ":
            count += 1
        if count >= length/2:
            return True

    return False


def init_word_reveal():
    """
    initializes the word blanks based on the secret movie
    """
    global word_blanks

    for i in secret_name:
        if isalpha(i):
            word_blanks.append("_")
        else:
            word_blanks.append(i)

def display_word():
    """
    takes the list of chars from word blanks and creates a complete string

    :return: the complete string of the word blank list
    """
    word = ""
    for i in word_blanks:
        word += i

    return word 

def reveal_word():
    """
    reveals a random character in the secret movie name
    """
    random_reveal = random.randrange(len(secret_name))

    while not isalpha(word_blanks[random_reveal]):
        random_reveal = random.randrange(len(secret_name))
    
    word_blanks[random_reveal] = secret_name[random_reveal]

if __name__ == "__main__":
    bot.run(TOKEN)
