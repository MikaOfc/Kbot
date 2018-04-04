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

class OwnerCog:
    def __init__(self, bot):
        self.bot = bot

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 1800, BucketType.guild)
        @commands.is_owner()
        async def game(ctx, *, str):
            textchannel = ctx.message.channel
            await textchannel.trigger_typing()
            time.sleep(2)
            game = discord.Game(str)
            await bot.change_presence(status=discord.Status.online, activity=game)
            embed=discord.Embed(title="Game successfully changed!", color=0x9b59b6)
            await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 5, BucketType.guild)
        @commands.is_owner()
        async def restart(ctx):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="Restarting! :sparkling_heart:", color=0x9b59b6)
                await ctx.send(embed=embed)
                await bot.logout()

def setup(bot):
    bot.add_cog(OwnerCog(bot))
