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

class UtilityCog:
    def __init__(self, bot):
        self.bot = bot

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def uinfo(ctx, user: discord.Member):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed = discord.Embed(title="{}'s info.".format(user.name), description="Heres what I could find.", color=0x9b59b6)
                embed.add_field(name="Name", value=user.name, inline=True)
                embed.add_field(name="ID", value=user.id, inline=True)
                embed.add_field(name="Status", value=user.status, inline=True)
                embed.add_field(name="Highest Role", value=user.top_role)
                embed.add_field(name="Joined Discord", value=user.created_at.strftime("%m/%d/%y, %I:%M %p"))
                embed.add_field(name="Joined Server", value=user.joined_at.strftime("%m/%d/%y, %I:%M %p"))
                embed.set_thumbnail(url=user.avatar_url)
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def rinfo(ctx, *, str:discord.Role):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed = discord.Embed(color=0x9b59b6)
                embed.add_field(name="Role Name", value=str.mention)
                embed.add_field(name="Role ID", value=str.id)
                embed.add_field(name="Color Hex", value=str.colour)
                embed.add_field(name="Created At", value=str.created_at.strftime("%m/%d/%y, %I:%M %p"))
                embed.add_field(name="Mentionable", value=str.mentionable)
                embed.add_field(name="Default Role", value=str.is_default())
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def botinfo(ctx):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="Kayuna's Statistics :coffee:", color=0x9b59b6)
                embed.add_field(name="Server Count", value="{}".format(len(bot.guilds)), inline=True)
                embed.add_field(name="User Count", value="{}".format(len(bot.users)))
                embed.add_field(name="Version", value="v1.1")
                embed.add_field(name="Coded In", value="Python 3.6.5")
                embed.add_field(name="Library", value="discord.py")
                embed.add_field(name="Shard Count", value="{}/{}".format(bot.shard_id, bot.shard_count))
                embed.add_field(name="Support Server", value="[Click This Link](https://discord.gg/KnJ8EFm)")
                embed.add_field(name="Invite Me", value="[Click This Link](https://discordapp.com/oauth2/authorize?bot_id=429862295192207361&scope=bot&permissions=2146958591)")
                embed.set_thumbnail(url="https://imgur.com/hFLZtfX.jpg")
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def sinfo(ctx):
            textchannel = ctx.message.channel
            await textchannel.trigger_typing()
            time.sleep(2)
            guild = ctx.message.guild
            embed = discord.Embed(title="{}'s Information.".format(guild.name), color=0x9b59b6)
            embed.add_field(name="Server Name", value=guild.name, inline=True)
            embed.add_field(name="Region", value=guild.region, inline=True)
            embed.add_field(name="Owner", value=guild.owner, inline=True)
            embed.add_field(name="Created At", value=guild.created_at.strftime("%m/%d/%y, %I:%M %p"), inline=True)
            embed.add_field(name="Server ID", value=guild.id, inline=True)
            embed.add_field(name="Member Count", value=guild.member_count, inline=True)
            embed.set_thumbnail(url=guild.icon_url)
            await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 21600, BucketType.user)
        async def suggest(ctx, *, msg:str):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                target = ctx.message.author
                channel = bot.get_channel(426268143728721941)
                embed1 = discord.Embed(title="We have a new suggestion! :e_mail:", description=msg, color=0x9b59b6)
                embed1.add_field(name="User Name", value=target.name)
                embed1.add_field(name="User ID", value=target.id)
                embed1.add_field(name="Status", value=target.status)
                embed1.add_field(name="User Created At", value=target.created_at.strftime("%m/%d/%y, %I:%M %p"))
                embed1.set_thumbnail(url=target.avatar_url)
                embed2 = discord.Embed(title="Your suggestion has been sent to my developers! You can make a new suggestion again in 6 hours!", color=0x9b59b6)
                await channel.send(embed=embed1)
                await ctx.send(embed=embed2)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def avatar(ctx, user: discord.Member):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed = discord.Embed(title="{}'s avatar.".format(user.name), description="I fetched the users avatar for you.", color=0x9b59b6)
                embed.set_image(url=user.avatar_url)
                await ctx.send(embed=embed)
                asyncio.sleep(1)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.7, BucketType.user)
        async def ping(ctx):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                resp = await ctx.send(':ping_pong:')
                diff = resp.created_at - ctx.message.created_at
                embed = discord.Embed(title=f'Pong! That took {1000*diff.total_seconds():.1f}ms.', color=0x9b59b6)
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def membercount(ctx):
            textchannel = ctx.message.channel
            await textchannel.trigger_typing()
            time.sleep(2)
            guild = ctx.message.guild
            embed=discord.Embed(title="There are {} members in this server!".format(guild.member_count), color=0x9b59b6)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(UtilityCog(bot))
