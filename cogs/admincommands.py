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

class AdminCommandsCog:
    def __init__(self, bot):
        self.bot = bot

        @bot.command()
        @commands.guild_only()
        async def testing(ctx):
            embed=discord.Embed(title="Thank fucking God, this test obviously works!")
            await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.guild)
        @commands.has_permissions(ban_members=True)
        @commands.bot_has_permissions(ban_members=True)
        async def ban(ctx, user: discord.Member):
            if ctx.message.author == bot.user:
                return

            elif user == ctx.message.author:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="You cannot ban yourself!", color=0x9b59b6)
                await ctx.send(embed=embed)

            elif ctx.message.author == ctx.guild.owner:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    victim = user
                    await ctx.guild.ban(victim)
                    embed = discord.Embed(title="User successfully banned! :hammer: ", color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="I can not ban members with a equal or higher top role than me! Please consider moving my role to the top of the role list.")
                    await ctx.send(embed=embed)

            elif user.top_role >= ctx.message.author.top_role:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed = discord.Embed(title="You cannot ban a user equal to or higher than you in the role hierarchy!", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                victim = user
                await ctx.guild.ban(victim)
                embed = discord.Embed(title="User successfully banned! :hammer: ", color=0x9b59b6)
                await ctx.send(embed=embed)
                #Bans the tagged user from the server.
                #Please fix it where it doesn't give the succesful prompt when tagging the server owner for a ban.

        @bot.command()
        @commands.guild_only()
        @commands.has_permissions(ban_members=True)
        @commands.cooldown(1, 5, BucketType.user)
        async def hackban(ctx, user_id:int):
            author = ctx.message.author
            guild = author.guild
            user = guild.get_member(user_id)
            await bot.http.ban(user_id, guild.id, 0)
            textchannel = ctx.message.channel
            await textchannel.trigger_typing()
            time.sleep(2)
            embed=discord.Embed(title="{} has been succesfully banned!".format(user_id), color=0x9b59b6)
            await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.has_permissions(ban_members=True)
        @commands.cooldown(1, 5, BucketType.user)
        async def softban(ctx, target:discord.Member):
            if ctx.message.author == bot.user:
                return

            elif ctx.message.author == ctx.guild.owner:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    await ctx.guild.ban(target, delete_message_days=3)
                    await ctx.guild.unban(target)
                    embed = discord.Embed(title="Succesfully softbanned that user! :hammer:", color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="That users top role is higher than or equal to my own bot role! My role must be higher than the target users, in order to ban them!", color=0x9b59b6)
                    await ctx.send(embed=embed)

            elif target == ctx.message.author:
                embed=discord.Embed(title="You cannot softban yourself!", color=0x9b59b6)
                await ctx.send(embed=embed)

            elif target.top_role >= ctx.message.author.top_role:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="You cannot softban a member whos highest role is equal to or higher than your own highest role!", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                await ctx.guild.ban(target, delete_message_days=3)
                await ctx.guild.unban(target)
                embed = discord.Embed(title="Succesfully softbanned that user! :hammer:", color=0x9b59b6)
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.has_permissions(manage_roles=True)
        @commands.cooldown(1, 0.5, BucketType.user)
        async def rhoist(ctx, *, str:discord.Role):
            if ctx.message.author == bot.user:
                return

            elif ctx.message.author == ctx.guild.owner:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    await str.edit(hoist=True)
                    embed=discord.Embed(title="Successfully hoisted that role!", color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="That role is higher than or equal to my own bot role! My role must be higher than the target role, in order to hoist them!", color=0x9b59b6)
                    await ctx.send(embed=embed)

            elif str >= ctx.message.author.top_role:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="You cannot hoist a role that is equal to or higher than your own highest role!", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    await str.edit(hoist=True)
                    embed=discord.Embed(title="Successfully hoisted that role!", color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="That role is higher than or equal to my own bot role! My role must be higher than the target role, in order to hoist them!", color=0x9b59b6)
                    await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.has_permissions(manage_roles=True)
        @commands.cooldown(1, 0.5, BucketType.user)
        async def unhoist(ctx, *, str:discord.Role):
            if ctx.message.author == bot.user:
                return

            elif ctx.message.author == ctx.guild.owner:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    await str.edit(hoist=False)
                    embed=discord.Embed(title="Successfully unhoisted that role!", color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="That role is higher than or equal to my own bot role! My role must be higher than the target role, in order to hoist them!", color=0x9b59b6)
                    await ctx.send(embed=embed)

            elif str >= ctx.message.author.top_role:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="You cannot unhoist a role that is equal to or higher than your own highest role!", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                await str.edit(hoist=False)
                embed=discord.Embed(title="Successfully unhoisted that role!", color=0x9b59b6)
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.has_permissions(manage_channels=True)
        @commands.cooldown(1, 0.5, BucketType.user)
        async def delchannel(ctx):
            textchannel = ctx.message.channel
            await textchannel.delete()

        @bot.command()
        @commands.guild_only()
        @commands.has_permissions(manage_channels=True)
        @commands.cooldown(1, 0.5, BucketType.user)
        async def createchannel(ctx, *, str):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                guild = ctx.message.guild
                await guild.create_text_channel(str)
                embed=discord.Embed(title="Channel successfully created!", color=0x9b59b6)
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.has_permissions(manage_roles=True)
        @commands.bot_has_permissions(manage_roles=True)
        @commands.cooldown(1, 0.5, BucketType.user)
        async def createrole(ctx, *, name):
            if ctx.message.author == bot.user:
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                await ctx.guild.create_role(name=name)
                embed=discord.Embed(title="Role successfully created!", color=0x9b59b6)
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.has_permissions(manage_roles=True)
        @commands.bot_has_permissions(manage_roles=True)
        @commands.cooldown(1, 0.5, BucketType.user)
        async def deleterole(ctx, *, str:discord.Role):
            if ctx.message.author == bot.user:
                return

            elif ctx.message.author == ctx.guild.owner:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    await str.delete()
                    embed=discord.Embed(title="Role successfully deleted!", color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="That role is higher than or equal to my own bot role! My role must be higher than the target role, in order to delete it!", color=0x9b59b6)
                    await ctx.send(embed=embed)

            elif str >= ctx.message.author.top_role:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="You cannot delete a role equal to or higher than your own top role!", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    await str.delete()
                    embed=discord.Embed(title="Role successfully deleted!", color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="That role is higher than or equal to my own bot role! My role must be higher than the target role, in order to delete it!", color=0x9b59b6)
                    await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.has_permissions(manage_roles=True)
        @commands.bot_has_permissions(manage_roles=True)
        @commands.cooldown(1, 0.5, BucketType.user)
        async def giverole(ctx, user:discord.Member, *, str:discord.Role):
            if ctx.message.author == ctx.guild.owner:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    await user.add_roles(str)
                    embed=discord.Embed(title="Successfully added {} to {}!".format(str, user), color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="That role is higher than or equal to my own bot role! My role must be higher than the target role, in order to assign them!", color=0x9b59b6)
                    await ctx.send(embed=embed)

            elif ctx.message.author == bot.user:
                return

            elif user.top_role >= ctx.message.author.top_role and str < ctx.message.author.top_role:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    await user.add_roles(str)
                    embed=discord.Embed(title="Successfully added {} to {}!".format(str, user), color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="That role is higher than or equal to my own bot role! My role must be higher than the target role, in order to assign them!", color=0x9b59b6)
                    await ctx.send(embed=embed)

            elif str >= ctx.message.author.top_role:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed = discord.Embed(title="You cannot assign a role equal to or higher than your own highest role, to others!", color=0x9b59b6)
                await ctx.send(embed=embed)

            elif user.top_role >= ctx.message.author.top_role:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed = discord.Embed(title="You cannot assign a role via my commands to a user equal to or higher than you in the role hierarchy!", color=0x9b59b6)
                await ctx.send(embed=embed)

            elif str in user.roles:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="That user already has that role!", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    await user.add_roles(str)
                    embed=discord.Embed(title="Successfully added {} to {}!".format(str, user), color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="That role is higher than or equal to my own bot role! My role must be higher than the target role, in order to assign them!", color=0x9b59b6)
                    await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.has_permissions(manage_roles=True)
        @commands.bot_has_permissions(manage_roles=True)
        @commands.cooldown(1, 0.5, BucketType.user)
        async def takerole(ctx, user:discord.Member, *, str:discord.Role):
            if ctx.message.author == bot.user:
                return

            elif ctx.message.author == ctx.guild.owner:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    await user.remove_roles(str)
                    embed=discord.Embed(title="Successfully removed {} from {}!".format(str, user), color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="That role is higher than or equal to my own bot role! My role must be higher than the target role, in order to assign them!", color=0x9b59b6)
                    await ctx.send(embed=embed)

            elif user.top_role >= ctx.message.author.top_role and str < ctx.message.author.top_role:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(0.5)
                    await user.remove_roles(str)
                    embed=discord.Embed(title="Successfully removed {} from {}!".format(str, user), color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="That role is higher than or equal to my own bot role! My role must be higher than the target role, in order to remove them!", color=0x9b59b6)
                    await ctx.send(embed=embed)

            elif str >= ctx.message.author.top_role:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed = discord.Embed(title="You cannot remove a role higher than or equal to your own highest role, from other members or yourself!", color=0x9b59b6)
                await ctx.send(embed=embed)

            elif user.top_role >= ctx.message.author.top_role:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed = discord.Embed(title="You cannot remove a role via my commands from a user equal to or higher than you in the role hierarchy!", color=0x9b59b6)
                await ctx.send(embed=embed)

            elif str not in user.roles:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="That user does not that role!", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    await user.remove_roles(str)
                    embed=discord.Embed(title="Successfully removed {} from {}!".format(str, user), color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="That role is higher than or equal to my own bot role! My role must be higher than the target role, in order to remove them!", color=0x9b59b6)
                    await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.has_permissions(manage_nicknames=True)
        @commands.bot_has_permissions(manage_nicknames=True)
        @commands.cooldown(1, 0.5, BucketType.user)
        async def nickname(ctx, user:discord.Member, *, str):
            if ctx.message.author == ctx.guild.owner:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    member = user
                    await member.edit(nick=str)
                    embed=discord.Embed(title="Nickname successfully changed!", color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="I can not edit the nicknames of users with a equal or higher top role than me! Please consider moving my role to the top of the role list.", color=0x9b59b6)
                    await ctx.send(embed=embed)

            elif ctx.message.author == bot.user:
                return

            elif user.top_role >= ctx.message.author.top_role:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed = discord.Embed(title="You cannot change the nickname of someone equal to or higher than you in the role hierarchy!", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    member = user
                    await member.edit(nick=str)
                    embed=discord.Embed(title="Nickname successfully changed!", color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="I can not edit the nicknames of users with a equal or higher top role than me! Please consider moving my role to the top of the role list.", color=0x9b59b6)
                    await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.has_permissions(manage_messages=True)
        @commands.bot_has_permissions(manage_messages=True)
        @commands.cooldown(1, 0.5, BucketType.guild)
        async def purge(ctx, number: int):
            if ctx.message.author == bot.user:
                return

            if number > 1000:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(description="I cannot delete more than 1,000 messages at a time, or messages older than 2 weeks old. Thats how Discord works, don't blame me please.~ ♡", color=0x9b59b6)
                await ctx.send(embed=embed)
                return

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                deleted = number
                textchannel = ctx.message.channel
                await textchannel.purge(limit=deleted+1)
                embed = discord.Embed(title="Cleared {} message(s).".format(deleted), color=0x9b59b6)
                await ctx.send(embed=embed)

        @bot.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.guild)
        @commands.has_permissions(kick_members=True)
        @commands.bot_has_permissions(kick_members=True)
        async def kick(ctx, user: discord.Member):
            if ctx.message.author == bot.user:
                return

            elif user == ctx.message.author:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed=discord.Embed(title="You cannot kick yourself!", color=0x9b59b6)
                await ctx.send(embed=embed)

            elif ctx.message.author == ctx.guild.owner:
                try:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    victim = user
                    await ctx.guild.kick(victim)
                    embed = discord.Embed(title="User successfully kicked! :boot: ", color=0x9b59b6)
                    await ctx.send(embed=embed)

                except discord.Forbidden:
                    textchannel = ctx.message.channel
                    await textchannel.trigger_typing()
                    time.sleep(2)
                    embed=discord.Embed(title="I can not kick members with a equal or higher top role than me! Please consider moving my role to the top of the role list.")
                    await ctx.send(embed=embed)

            elif user.top_role >= ctx.message.author.top_role:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                embed = discord.Embed(title="You cannot kick a user equal to or higher than you in the role hierarchy!", color=0x9b59b6)
                await ctx.send(embed=embed)

            else:
                textchannel = ctx.message.channel
                await textchannel.trigger_typing()
                time.sleep(2)
                victim = user
                await ctx.guild.kick(victim)
                embed = discord.Embed(title="User successfully kicked! :boot: ", color=0x9b59b6)
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AdminCommandsCog(bot))
