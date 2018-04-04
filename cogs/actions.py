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

class ActionsCog:
    def __init__(self, bot):
        self.bot = bot

        @bot.command()
        @commands.guild_only()
        async def pat(ctx, user:discord.Member):
            if ctx.message.author == bot.user:
                return

            elif user == ctx.message.author:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="As much as you want to, you cannot pat yourself! :sparkles:", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                member = ctx.message.author
                page = await bot.http._session.get('https://nekos.life/api/v2/img/pat')
                neko = await page.json()
                em = discord.Embed(title="{} has recieved a pat from {} ! :sparkling_heart:".format(user.name, member.name), color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def hug(ctx, user:discord.Member):
            if ctx.message.author == bot.user:
                return

            elif user == ctx.message.author:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="As much as you want to, you cannot hug yourself! :sparkles:", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                member = ctx.message.author
                page = await bot.http._session.get('https://nekos.life/api/v2/img/hug')
                neko = await page.json()
                em = discord.Embed(title="{} has hugged {} ! :sparkling_heart: :sparkles:".format(member.name, user.name), color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def kiss(ctx, user:discord.Member):
            if ctx.message.author == bot.user:
                return

            elif user == ctx.message.author:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="As much as you want to, you cannot kiss yourself! :sparkles:", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                member = ctx.message.author
                page = await bot.http._session.get('https://nekos.life/api/v2/img/kiss')
                neko = await page.json()
                em = discord.Embed(title="{} has kissed {} ! :sparkling_heart: :rose:".format(member.name, user.name), color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def cuddle(ctx, user:discord.Member):
            if ctx.message.author == bot.user:
                return

            elif user == ctx.message.author:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="As much as you want to, you cannot cuddle yourself! :sparkles:", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                member = ctx.message.author
                page = await bot.http._session.get('https://nekos.life/api/v2/img/cuddle')
                neko = await page.json()
                em = discord.Embed(title="{} is cuddling {} ! :rose:".format(member.name, user.name), color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def poke(ctx, user:discord.Member):
            if ctx.message.author == bot.user:
                return

            elif user == ctx.message.author:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="As much as you want to, you cannot poke yourself! :sparkles:", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                member = ctx.message.author
                page = await bot.http._session.get('https://nekos.life/api/v2/img/poke')
                neko = await page.json()
                em = discord.Embed(title="{} just poked {} ! :sparkles:".format(member.name, user.name), color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def slap(ctx, user:discord.Member):
            if ctx.message.author == bot.user:
                return

            elif user == ctx.message.author:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="As much as you want to, you cannot slap yourself! :sparkles:", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                member = ctx.message.author
                page = await bot.http._session.get('https://nekos.life/api/v2/img/slap')
                neko = await page.json()
                em = discord.Embed(title="{} just slapped {} ! :bomb:".format(member.name, user.name), color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def tickle(ctx, user:discord.Member):
            if ctx.message.author == bot.user:
                return

            elif user == ctx.message.author:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="As much as you want to, you cannot tickle yourself! :sparkles:", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                member = ctx.message.author
                page = await bot.http._session.get('https://nekos.life/api/v2/img/tickle')
                neko = await page.json()
                em = discord.Embed(title="{} is tickling {} ! :sparkles:".format(member.name, user.name), color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def feed(ctx, user:discord.Member):
            if ctx.message.author == bot.user:
                return

            elif user == ctx.message.author:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="As much as you want to, you cannot feed yourself! (At least with my commands, I'm not going to let you starve, silly.) :sparkles:", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                member = ctx.message.author
                page = await bot.http._session.get('https://nekos.life/api/v2/img/feed')
                neko = await page.json()
                em = discord.Embed(title="{} has fed {} ! :sparkles: :fork_knife_plate:".format(member.name, user.name), color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def bite(ctx, user:discord.Member):
            if ctx.message.author == bot.user:
                return

            elif user == ctx.message.author:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="As much as you want to, you cannot bite yourself! :sparkles:", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                img=["https://imgur.com/rGrnZO0.gif", "https://imgur.com/2S7IhKE.gif", "https://imgur.com/sjSHxGT.gif", "https://imgur.com/zaUdcF7.gif",
                "https://imgur.com/M4vsqF1.gif", "https://imgur.com/okTK5Rg.gif", "https://imgur.com/pkrW3Fv.gif", "https://imgur.com/8ndl01P.gif",
                "https://imgur.com/1Euo7tA.gif", "https://imgur.com/QjdiuRD.gif", "https://imgur.com/RbEiFiZ.gif", "https://imgur.com/3XOpTeF.gif",
                "https://imgur.com/O6gQC0D.gif", "https://imgur.com/afNZpYm.gif", "https://imgur.com/re2VR7Y.gif", "https://imgur.com/OUKkGV4.gif",
                "https://imgur.com/uXsFqcy.gif", "https://imgur.com/GXxBTZg.gif", "https://imgur.com/P9FQRHe.gif"]
                member = ctx.message.author
                embed=discord.Embed(title="{} has bitten {} ! :hibiscus: :sparkling_heart:".format(member.name, user.name), color=0x9b59b6)
                embed.set_image(url=random.choice(img))
                await ctx.send(embed=embed)
                asyncio.sleep(1)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def lick(ctx, user:discord.Member):
            if ctx.message.author == bot.user:
                return

            elif user == ctx.message.author:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="As much as you want to, you cannot lick yourself! :sparkles:", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                img=["https://imgur.com/cjYTEns.gif", "https://imgur.com/BmUcq3v.gif", "https://imgur.com/QSwbCfj.gif", "https://imgur.com/O34OEos.gif",
                "https://imgur.com/ZrUy8Y3.gif", "https://imgur.com/wz2BmRW.gif", "https://imgur.com/fuAkRPd.gif", "https://imgur.com/kZyKO5y.gif",
                "https://imgur.com/C7UU5MX.gif", "https://imgur.com/1QBiQHV.gif", "https://imgur.com/bav6CXS.gif", "https://imgur.com/MIi0l1r.gif",
                "https://imgur.com/V80YpDL.gif", "https://imgur.com/FISbHDG.gif", "https://imgur.com/ozMIgj9.gif"]
                member = ctx.message.author
                embed=discord.Embed(title="{} has licked {} ! :sparkling_heart:".format(member.name, user.name), color=0x9b59b6)
                embed.set_image(url=random.choice(img))
                await ctx.send(embed=embed)
                asyncio.sleep(1)

def setup(bot):
    bot.add_cog(ActionsCog(bot))
