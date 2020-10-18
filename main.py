import discord
from discord.ext import commands

import asyncio

import cogs

import json_manager
import music

import os 

token=json_manager.get(json_manager.config_file_uri, "token")
prefix=json_manager.get(json_manager.config_file_uri, "prefix")

if token == "":
    print("error token is not defined !")
elif prefix == "":
    print("error prefix is not defined !")
else:
    bot=commands.Bot(command_prefix=prefix, description="Bot of group !")
    
    @bot.event
    async def on_ready():
        print("Bot Started !")

    @bot.command()
    async def load(ctx, name=None):
        if name:
            bot.load_extension(name)
            print(name, "has been loaded")
            await ctx.send(str(name + " has been loaded"))
        
    @bot.command()
    async def unload(ctx, name=None):
        if name:
            bot.unload_extension(name)
            print(name, "has been unloaded")
            await ctx.send(str(name + " has been unloaded"))

    @bot.command()
    async def reload(ctx, name=None):
        if name:
            try:
                bot.reload_extension(name)
                print(name, "has been reloaded")
                await ctx.send(str(name + " has been reloaded"))
            except:
                bot.load_extension(name)
                print(name, "has been loaded")
                await ctx.send(str(name + " has been loaded"))

    for file in os.listdir("./commands"):
        if file.endswith(".py"):
            bot.load_extension(f'commands.{file[:-3]}')
            print(file, "has been loaded")

    @bot.event
    async def on_raw_reaction_add(payload):
        guild = bot.get_guild(payload.guild_id)
        user = bot.get_user(payload.user_id)
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        if not user == bot.user:
            if payload.emoji.name == "✅":
                if message.author == bot.user:
                    url = ""
                    guild = bot.get_guild(payload.guild_id)
                    message = await channel.fetch_message(payload.message_id)
                    for emb in message.embeds:
                        url=emb.description
                        for i in guild.voice_channels:
                            voice_channel=i
                            if str(i) == str(emb.author.name):
                                voice_channel=i
                                break
                    client = guild.voice_client
                    if client and client.channel:
                        video = music.Video(url)
                        music.musics[guild].append(video)
                        await channel.send("+" + video.url)
                    else:
                        video = music.Video(url)
                        music.musics[guild] = []
                        client = await voice_channel.connect()
                        await channel.send(f"Je lance : {video.url}")
                        music.play_song(bot, client, music.musics[guild], video)


    bot.run(token)
