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

class ImagesCog:
    def __init__(self, bot):
        self.bot = bot

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def kitsune(ctx):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                page = await bot.http._session.get('https://nekos.life/api/v2/img/fox_girl')
                neko = await page.json()
                em = discord.Embed(title="Have a cute fox girl. ♡ ~", color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def neko(ctx):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                page = await bot.http._session.get('https://nekos.life/api/v2/img/neko')
                neko = await page.json()
                em = discord.Embed(title="Nyyaaa. ♡ ~",color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(ImagesCog(bot))
