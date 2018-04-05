import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
import datetime
import json
import os
import time
import sys, traceback
from asyncurban import UrbanDictionary
from discord.ext.commands.cooldowns import BucketType

initial_extensions = ['cogs.admincommands', 'cogs.actions', 'cogs.images', 'cogs.miscellaneous', 'cogs.utility', 'cogs.fun', 'cogs.nsfw', 'cogs.owner']

bot = commands.AutoShardedBot(description="Kayuna", command_prefix="=", pm_help = False, case_insensitive=True, owner_id = 419346812890251265)
bot.remove_command("help")
# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    print('You are running Kayuna v1.1')
    print('Created by Mika#0777')
    return await bot.change_presence(activity=discord.Game(name="Alpha Testing | =help"))

@bot.command()
@commands.guild_only()
@commands.cooldown(1, 1, BucketType.guild)
async def help(ctx):
    if ctx.message.author == bot.user:
        return

    else:
        textchannel = ctx.message.channel
        await textchannel.trigger_typing()
        time.sleep(2)
        embed = discord.Embed(title="Modules :closed_lock_with_key: ", description="**\n• Actions**\n\n**• Administration**\n\n**• Images**\n\n**• Miscellaneous**\n\n**• Utility**\n\n**• Fun**\n\n**• Nsfw**", color=0x9b59b6)
        embed.set_footer(text="Use =(module name) to see the given modules commands.")
        await ctx.send(embed=embed)

@bot.command()
@commands.guild_only()
@commands.cooldown(1, 1, BucketType.guild)
async def actions(ctx):
    if ctx.message.author == bot.user:
        return

    else:
        textchannel = ctx.message.channel
        await textchannel.trigger_typing()
        time.sleep(2)
        embed = discord.Embed(title="Action Commands :coffee:", description="**Pat** - Pats another user. | **Usage:** =pat @user\n\n**Hug** - Hugs another user. | **Usage:** =hug @user\n\n**Kiss** - Kisses another user. | **Usage:** =kiss @user\n\n**Cuddle** - Cuddles another user. | **Usage:** =cuddle @user\n\n**Poke** - Pokes another user. | **Usage:** =poke @user\n\n**Slap** - Slaps another user. | **Usage:** =slap @user\n\n**Tickle** - Tickles another user. | **Usage:** =tickle @user\n\n**Bite** - Bites another user. | **Usage:** =bite @user\n\n**Lick** - Licks another user. | **Usage:** =lick @user\n\n**Feed** - Feeds a user. | **Usage:** =feed @user", color=0x9b59b6)
        await ctx.send(embed=embed)

@bot.command()
@commands.guild_only()
@commands.cooldown(1, 1, BucketType.guild)
async def images(ctx):
    if ctx.message.author == bot.user:
        return

    else:
        textchannel = ctx.message.channel
        await textchannel.trigger_typing()
        time.sleep(2)
        embed = discord.Embed(title="Image Commands :frame_photo:", description="**Neko** - Fetches a neko girl photo. | **Usage:** =neko\n\n**Kitsune** - Fetches a foxgirl photo. | **Usage:** =kitsune", color=0x9b59b6)
        await ctx.send(embed=embed)

@bot.command()
@commands.guild_only()
@commands.cooldown(1, 1, BucketType.guild)
async def administration(ctx):
    if ctx.message.author == bot.user:
        return

    else:
        textchannel = ctx.message.channel
        await textchannel.trigger_typing()
        time.sleep(2)
        embed1 = discord.Embed(title="Administration Commands :rotating_light:", description="**Kick** - Kicks the user from the server. | **Usage:** =kick @user\n\n**Ban** - Bans the user from the server. | **Usage:** =ban @user\n\n**Hackban** - Bans a user whos not in the server. | **Usage:** =hackban (user ID)\n\n**Softban** - Auto bans/unbans a user & deletes messages. | **Usage:** =softban @user\n\n**Nickname** - Changes the users nickname. | **Usage**: =nickname @user (new name)\n\n**Purge** - Deletes a number of messages from the channel. | **Usage:** =purge (number)\n\n**Give Role** - Gives a role to a user. | **Usage:** =giverole @user (target role)\n\n**Take Role** - Takes a role from a user. | **Usage:** =takerole @user (target role)\n\n**Create Role** - Creates a new role in the server. | **Usage:** =createrole (new role name)\n\n**Delete Role** - Deletes a role in the server. | **Usage:** =deleterole (target role)", color=0x9b59b6)
        embed2 = discord.Embed(description="**Create Channel** - Creates a new text channel. | **Usage:** =createchannel (name)\n\n**Delete Channel** - Deletes the current text channel. | **Usage:** =delchannel\n\n**Rolehoist** - Hoists a given role in the server. | **Usage:** =rhoist (target role)\n\n**Unhoist** - Unhoists a given role in the server. | **Usage:** =unhoist (target role)", color=0x9b59b6)
        await ctx.send(embed=embed1)
        await ctx.send(embed=embed2)

@bot.command()
@commands.guild_only()
@commands.cooldown(1, 1, BucketType.guild)
async def miscellaneous(ctx):
    if ctx.message.author == bot.user:
        return

    else:
        textchannel = ctx.message.channel
        await textchannel.trigger_typing()
        time.sleep(2)
        embed = discord.Embed(title="Miscellaneous Commands :question:", description="**About Me** - Posts a few random facts about me. | **Usage:** =aboutme", color=0x9b59b6)
        await ctx.send(embed=embed)

@bot.command()
@commands.guild_only()
@commands.cooldown(1, 1, BucketType.guild)
async def utility(ctx):
    if ctx.message.author == bot.user:
        return

    else:
        textchannel = ctx.message.channel
        await textchannel.trigger_typing()
        time.sleep(2)
        embed = discord.Embed(title="Utility Commands :hammer:", description="**Help** - Displays the bots help page. | **Usage:** =help\n\n**User Info** - Posts information about a user. | **Usage:** =uinfo @user\n\n**Role Info** - Posts information about a role. | **Usage:** =rinfo (role)\n\n**Bot Info** - Posts an info page about me. | **Usage:** =botinfo\n\n**Server Info** - Gets information about the current server. | **Usage:** =sinfo\n\n**Suggest** - Send a suggestion to my developers. | **Usage:** =suggest (message)\n\n**Avatar** - Fetches a users avatar & posts it in the chat. | **Usage:** =avatar @user\n\n**Ping** - Shows your latency to the bots server. | **Usage:** =ping\n\n**Member Count** - Shows current server user count. | **Usage:** =membercount", color=0x9b59b6)
        await ctx.send(embed=embed)

@bot.command()
@commands.guild_only()
@commands.cooldown(1, 1, BucketType.guild)
async def fun(ctx):
    if ctx.message.author == bot.user:
        return

    else:
        textchannel = ctx.message.channel
        await textchannel.trigger_typing()
        time.sleep(2)
        embed = discord.Embed(title="Fun Commands :tophat:", description="**Coin Flip** - Flips a coin, which lands on either heads or tails. | **Usage:** =coinflip\n\n**Lenny Shrug** - Posts a ¯\_(ツ)_/¯ face in chat. | **Usage:** =lennyshrug\n\n**Say** - Makes the bot repeat what you say. | **Usage:** =say (message)\n\n**Ship** - Shows relationship stats for you & a target user. | **Usage:** =ship @user\n\n**Urban** - Searches a word on Urban Dictionary. | **Usage:** =urban (word)\n\n**Urban Random** - Reponds with a random Urban Dictionary term. | **Usage:** =urbanr\n\n**Weather** - Checks the weather in a given location. | **Usage:** =weather (city)", color=0x9b59b6)
        await ctx.send(embed=embed)

@bot.command()
@commands.guild_only()
@commands.cooldown(1, 1, BucketType.guild)
async def nsfw(ctx):
    if ctx.message.author == bot.user:
        return

    else:
        textchannel = ctx.message.channel
        await textchannel.trigger_typing()
        time.sleep(2)
        embed = discord.Embed(title="NSFW Commands :sparkling_heart:", description="**Note that all NSFW commands can only be used in NSFW channels by default & contain NO real porn!\n\nLewdneko** - Posts a NSFW neko to the chat. | **Usage:** =lewdneko\n\n**Lewdnekogif** - Posts a NSFW neko gif to the chat. | **Usage:** =lewdnekogif\n\n**Hentai** - Posts a random hentai gif to the chat. | **Usage:** =hentai\n\n**Vanilla** - Vanilla hentai at its finest. | **Usage:** =vanilla\n\n**Oral** - Girls getting eaten out. Enough said. ~ | **Usage:** =oral\n\n**Blowjob** - The command title says it all. | **Usage:** =blowjob\n\n**Lesbian** - Posts a lesbian hentai gif. | **Usage:** =lesbian\n\n**Cum** - Posts a cum related hentai gif. | **Usage:** =cum\n\n**Boobs** - Boobs. Boobs everywhere. Also, mostly gifs. | **Usage:** =boobs\n\n**Anal** - Pretty sure you can figure this one out yourself. | **Usage:** =anal\n\n**Pussy** - Lewd cats that don't meow, if you catch my drift. | **Usage:** =pussy", color=0x9b59b6)
        await ctx.send(embed=embed)

@bot.command()
async def embed(ctx):
    embed = discord.Embed(title="Name", description = "NA", color=0x9b59b6)
    embed.set_footer(text="This is a footer.")
    embed.set_author(text="Me, of course.")
    embed.add_field(name="This is a field.", value = "No it isn't.", inline= True)
    await ctx.send(embed=embed)
    #This line ^ defines the embed function, so replies from the bot that use embeds can function, don't touch this or it will disrupt all the embeds in all bot responses.

bot.run('NDI5ODYyMjk1MTkyMjA3MzYx.DaZLhQ.yU1DkysI667m1COjnVDvOaVVqr0')
