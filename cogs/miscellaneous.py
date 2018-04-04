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

class MiscellaneousCog:
    def __init__(self, bot):
        self.bot = bot

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.guild)
        async def aboutme(ctx):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed = discord.Embed(description="I'm a simple moderation & image searching bot that requires absolutely zero setup. Just a plug & play application at its finest. All credit goes to my sole devolper.", color=0x9b59b6)
                await ctx.send(embed=embed)
                asyncio.sleep(1)

def setup(bot):
    bot.add_cog(MiscellaneousCog(bot))
