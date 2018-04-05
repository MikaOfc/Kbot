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
from apixu.client import ApixuClient, ApixuException
from asyncurban import UrbanDictionary
from discord.ext.commands.cooldowns import BucketType

api_key = '6103b63add044f4385031538180504'
client = ApixuClient(api_key)

class FunCog:
    def __init__(self, bot):
        self.bot = bot

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 1, BucketType.user)
        async def weather(ctx, *, str):
            current = client.getCurrentWeather(q=str)
            embed=discord.Embed(title="Current weather for :white_sun_small_cloud:", color=0x9b59b6)
            embed.add_field(name="Country", value="{}".format(current['location']['country']), inline=True)
            embed.add_field(name="State/Region", value="{}".format(current['location']['region']), inline=True)
            embed.add_field(name="City", value="{}".format(current['location']['name']), inline=True)
            embed.add_field(name="Lat/Long", value="{}/{}".format(current['location']['lat'], current['location']['lon']))
            embed.add_field(name="Local Time", value="{}".format(current['location']['localtime']))
            embed.add_field(name="Temperature", value="{}°C/{}°F".format(current['current']['temp_c'], current['current']['temp_f']))
            embed.add_field(name="Wind Speed", value="{}kph/{}mph".format(current['current']['wind_kph'], current['current']['wind_mph']))
            embed.add_field(name="Current Rainfall", value="{}mm/{}in".format(current['current']['precip_mm'], current['current']['precip_in']))
            embed.add_field(name="Humidity", value="{} RH".format(current['current']['humidity']))
            embed.add_field(name="Last Updated", value="{}".format(current['current']['last_updated']))
            embed.set_thumbnail(url="https://imgur.com/oheopRH.jpg")
            await ctx.send(embed=embed)

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

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 1, BucketType.user)
        async def urban(ctx, *, str):
            if ctx.message.author == bot.user:
                return

            else:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    ud = UrbanDictionary()
                    word = await ud.get_word(str)
                    embed=discord.Embed(title="Word: {0.word}".format(word), color=0x9b59b6)
                    embed.add_field(name="Urban Dictionary Definition", value="{0.definition}".format(word), inline=True)
                    embed.add_field(name="Urban Link", value="{0.permalink}".format(word), inline=False)
                    embed.set_thumbnail(url="https://imgur.com/HBPlcKQ.jpg")
                    await ctx.send(embed=embed)
                    await ud.close()

                except asyncurban.errors.WordNotFoundError():
                    embed=discord.Embed(title="There were no matches for that word!", color=0x9b59b6)
                    await ctx.send(embed=embed)
                    await ud.close()

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 1, BucketType.user)
        async def urbanr(ctx):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                ud = UrbanDictionary()
                random_word = await ud.get_random()
                embed = discord.Embed(title="Word: {0.word}".format(random_word), color=0x9b59b6)
                embed.add_field(name="Urban Dictionary Definition", value="{0.definition}".format(random_word), inline=True)
                embed.add_field(name="Urban Link", value="{0.permalink}".format(random_word), inline=True)
                embed.set_thumbnail(url="https://imgur.com/HBPlcKQ.jpg")
                await ctx.send(embed=embed)
                await ud.close()

def setup(bot):
    bot.add_cog(FunCog(bot))
