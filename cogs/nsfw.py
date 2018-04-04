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

class NsfwCog:
    def __init__(self, bot):
        self.bot = bot

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def pussy(ctx):
            textchannel = ctx.message.channel
            await textchannel.trigger_typing()
            time.sleep(0.5)
            ch = ctx.message.channel
            if ch.is_nsfw():
                page = await bot.http._session.get('https://nekos.life/api/v2/img/pussy')
                neko = await page.json()
                em = discord.Embed(title="How lewd. ♡ ~", color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

            else:
                embed = discord.Embed(title="I can only post NSFW content in a NSFW channel!", color=0x9b59b6)
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def anal(ctx):
            textchannel = ctx.message.channel
            await textchannel.trigger_typing()
            time.sleep(0.5)
            ch = ctx.message.channel
            if ch.is_nsfw():
                page = await bot.http._session.get('https://nekos.life/api/v2/img/anal')
                neko = await page.json()
                em = discord.Embed(title="How lewd. ♡ ~", color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

            else:
                embed = discord.Embed(title="I can only post NSFW content in a NSFW channel!", color=0x9b59b6)
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def boobs(ctx):
            textchannel = ctx.message.channel
            await textchannel.trigger_typing()
            time.sleep(0.5)
            ch = ctx.message.channel
            if ch.is_nsfw():
                page = await bot.http._session.get('https://nekos.life/api/v2/img/boobs')
                neko = await page.json()
                em = discord.Embed(title="How lewd. ♡ ~", color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

            else:
                embed = discord.Embed(title="I can only post NSFW content in a NSFW channel!", color=0x9b59b6)
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def lesbian(ctx):
            textchannel = ctx.message.channel
            await textchannel.trigger_typing()
            time.sleep(0.5)
            ch = ctx.message.channel
            if ch.is_nsfw():
                page = await bot.http._session.get('https://nekos.life/api/v2/img/les')
                neko = await page.json()
                em = discord.Embed(title="How lewd. ♡ ~", color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

            else:
                embed = discord.Embed(title="I can only post NSFW content in a NSFW channel!", color=0x9b59b6)
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def cum(ctx):
            textchannel = ctx.message.channel
            await textchannel.trigger_typing()
            time.sleep(0.5)
            ch = ctx.message.channel
            if ch.is_nsfw():
                page = await bot.http._session.get('https://nekos.life/api/v2/img/cum')
                neko = await page.json()
                em = discord.Embed(title="How lewd. ♡ ~", color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

            else:
                embed = discord.Embed(title="I can only post NSFW content in a NSFW channel!", color=0x9b59b6)
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def oral(ctx):
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                ch = ctx.message.channel
                if ch.is_nsfw():
                    page = await bot.http._session.get('https://nekos.life/api/v2/img/kuni')
                    neko = await page.json()
                    em = discord.Embed(title="How lewd. ♡ ~", color=0x9b59b6)
                    em.set_image(url=neko['url'])
                    await ctx.send(embed=em)

                else:
                    embed = discord.Embed(title="I can only post NSFW content in a NSFW channel!", color=0x9b59b6)
                    await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def blowjob(ctx):
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                ch = ctx.message.channel
                if ch.is_nsfw():
                    page = await bot.http._session.get('https://nekos.life/api/v2/img/bj')
                    neko = await page.json()
                    em = discord.Embed(title="How lewd. ♡ ~", color=0x9b59b6)
                    em.set_image(url=neko['url'])
                    await ctx.send(embed=em)

                else:
                    embed = discord.Embed(title="I can only post NSFW content in a NSFW channel!", color=0x9b59b6)
                    await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def vanilla(ctx):
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(0.5)
                ch = ctx.message.channel
                if ch.is_nsfw():
                    page = await bot.http._session.get('https://nekos.life/api/v2/img/classic')
                    neko = await page.json()
                    em = discord.Embed(title="How lewd. ♡ ~", color=0x9b59b6)
                    em.set_image(url=neko['url'])
                    await ctx.send(embed=em)

                else:
                    embed = discord.Embed(title="I can only post NSFW content in a NSFW channel!", color=0x9b59b6)
                    await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def lewdneko(ctx):
            textchannel = ctx.message.channel
            await textchannel.trigger_typing()
            time.sleep(0.5)
            ch = ctx.message.channel
            if ch.is_nsfw():
                page = await bot.http._session.get('https://nekos.life/api/v2/img/lewd')
                neko = await page.json()
                em = discord.Embed(title="Oh, how lewd. ♡ ~", color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

            else:
                embed = discord.Embed(title="I can only post NSFW content in a NSFW channel!", color=0x9b59b6)
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def lewdnekogif(ctx):
            textchannel = ctx.message.channel
            await textchannel.trigger_typing()
            time.sleep(0.5)
            ch = ctx.message.channel
            if ch.is_nsfw():
                page = await bot.http._session.get('https://nekos.life/api/v2/img/nsfw_neko_gif')
                neko = await page.json()
                em = discord.Embed(title="How lewd. ♡ ~", color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

            else:
                embed = discord.Embed(title="I can only post NSFW content in a NSFW channel!", color=0x9b59b6)
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def hentai(ctx):
            textchannel = ctx.message.channel
            await textchannel.trigger_typing()
            time.sleep(0.5)
            ch = ctx.message.channel
            if ch.is_nsfw():
                page = await bot.http._session.get('https://nekos.life/api/v2/img/Random_hentai_gif')
                neko = await page.json()
                em = discord.Embed(title="How lewd. ♡ ~", color=0x9b59b6)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

            else:
                embed = discord.Embed(title="I can only post NSFW content in a NSFW channel!", color=0x9b59b6)
                await ctx.send(embed=embed)
                
def setup(bot):
    bot.add_cog(NsfwCog(bot))
