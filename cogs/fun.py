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

class FunCog:
    def __init__(self, bot):
        self.bot = bot

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def coinflip(ctx):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                img=["https://imgur.com/deO6E7E.jpg", "https://imgur.com/HdmlGay.jpg"]
                embed=discord.Embed(title="Heres the result!", color=0x9b59b6)
                embed.set_image(url=random.choice(img))
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def lennyshrug(ctx):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed = discord.Embed(description="¯\_(ツ)_/¯", color=0x9b59b6)
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def say(ctx, *, message):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                await ctx.send(message)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def ship(ctx, user:discord.Member):
            if user == ctx.message.author:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                page = await bot.http._session.get('https://nekos.life/api/v2/img/hug')
                neko = await page.json()
                em=discord.Embed(title="Awwee, you must be lonely, heres a hug from me instead! :sparkling_heart:", color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                member = ctx.message.author
                number1 = [random.randint(2,99)]
                number2 = [random.randint(2,99)]
                number3 = [random.randint(2,99)]
                number4 = [random.randint(2,99)]
                await ctx.send("**{} and {}'s love index.**".format(member.name, user.name))
                embed=discord.Embed(title="Statistics :closed_lock_with_key:", color=0x9b59b6)
                embed.add_field(name="Chance Of It All Working Out", value="{}%".format(random.choice(number1)))
                embed.add_field(name="Chance Of Being Cheated On", value="{}%".format(random.choice(number2)))
                embed.add_field(name="Chance Of Children", value="{}%".format(random.choice(number3)))
                embed.add_field(name="Chance Of Mariage", value="{}%".format(random.choice(number4)))
                embed.set_thumbnail(url="https://imgur.com/XZucXvF.jpg")
                await ctx.send(embed=embed)
                asyncio.sleep(1)

def setup(bot):
    bot.add_cog(FunCog(bot))
