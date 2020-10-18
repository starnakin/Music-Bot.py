import discord 
from discord.ext import commands
import youtube_dl
import asyncio
from youtube_search import YoutubeSearch

bot = commands.Bot(command_prefix='+')
musics = {}
ytdl = youtube_dl.YoutubeDL()

@bot.event
async def on_ready():
    print("Reda")

class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

def play_song(client, queue, song): 
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))
    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)
    client.play(source, after=next)

@bot.command()
async def skip(ctx):
    client = ctx.guild.voice_client
    client.stop()

@bot.command()
async def quit(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild].clear()

@bot.command()
async def pause(ctx):
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()

@bot.command()
async def resume(ctx):
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()

@bot.command()
async def now(ctx):
    await ctx.send(musics[ctx.guild])

import time
@bot.command()
async def BISMILLAH(ctx):
    #for i in ctx.guild.get:

    await ctx.send(" « Maman ! Pourquoi on doit toujours dire Bismillah. ? » ")
    time.sleep(1)
    await ctx.send("« Parce que quand tu dis Bismillah, Dieu est avec toi, et met la Baraka dans tout ce que tu fais.» ")
    time.sleep(1)
    await ctx.send("bismillah")
    time.sleep(1)
    await ctx.send("bismillah")
    time.sleep(1)
    await ctx.send("Bismillah au nom dAllah ")
    time.sleep(1)
    await ctx.send("bismillah")
    time.sleep(1)
    await ctx.send("bismillah")
    time.sleep(1)
    await ctx.send("in the name of Allah  ")
    time.sleep(1)
    await ctx.send("Je me lève tous les matins, jatteste que Dieu nest quun Jai faim, je me lave les mains. ")
    time.sleep(1)
    await ctx.send("Mais avant tout Bismillah")
    time.sleep(1)
    await ctx.send("Quand je déjeune à midi, joublie pas de dire merci, a ceux qui mont nourris.. ")
    time.sleep(1)
    await ctx.send("Mais avant tout Bismillah ")
    time.sleep(1)
    await ctx.send("Quand lécole est terminée, super je vais mamuser, dabord je vais prier.. ")
    time.sleep(1)
    await ctx.send("Mais avant tout Bismillah ")
    time.sleep(1)
    await ctx.send("Le soir quand il fait noire, je lis une belle histoire, je dis le Doua du soir")
    time.sleep(1)
    await ctx.send("Mais avant tout Bismillah ")
    time.sleep(1)
    await ctx.send("Bismillah... Avant de dormir, Bismillah... Avant de sortir ")
    time.sleep(1)
    await ctx.send("Bismillah... Avant de sassoir, Bismillah... Avant de boire ")
    time.sleep(1)
    await ctx.send("Bismillah... Avant de chanter, Bismillah... Avant de jouer ")
    time.sleep(1)
    await ctx.send("Bismillah... Avant de lire, Bismillah... Avant d'écrire ")
    time.sleep(1)

@bot.event()
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
                        print(i)
                        if str(i) == str(emb.author.name):
                            voice_channel=i
                            break
                    print(voice_channel)
                client = guild.voice_client
                if client and client.channel:
                    video = Video(url)
                    musics[guild].append(video)
                    await channel.send("+" + video.url)
                else:
                    video = Video(url)
                    musics[guild] = []
                    client = await voice_channel.connect()
                    await channel.send(f"Je lance : {video.url}")
                    play_song(client, musics[guild], video)

@bot.command()
async def play(ctx, uri):
    if(uri.startswith("https")):
        if(uri.startswith("https://www.youtube.com/")):
            client = ctx.guild.voice_client
            print(type(ctx.author))
            if client and client.channel:
                video = Video(uri)
                musics[ctx.guild].append(video)
                await ctx.send("+" + video.url)
            else:
                channel = ctx.author.voice.channel
                video = Video(uri)
                musics[ctx.guild] = []
                client = await channel.connect()
                await ctx.send(f"Je lance : {video.url}")
                play_song(client, musics[ctx.guild], video)
    else:
        results = YoutubeSearch(uri, max_results=2).to_dict()     
        print(results[0]["thumbnails"]) 
        embed = discord.Embed(title=""+results[0]["title"], description="https://www.youtube.com/watch?v="+results[0]["id"]).set_image(url=results[0]["thumbnails"][0]).set_author(name=ctx.author.voice.channel)
        message = await ctx.channel.send(embed=embed)
        await message.add_reaction("✅")
        await message.add_reaction("❌")

bot.run("NzU5ODQ2OTY3OTY2MzAyMjY4.X3Dcog.-CTZJTQ19mSoFZGIn3mCgkWz72A")

"""
{
    "videos":
        [
            {
                "id":
                    "IFcxEfRO3n4",
                    "thumbnails": 
                        [
                            "https://i.ytimg.com/vi/IFcxEfRO3n4/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLC0PV7sMx6OnIl1Fi4b5B4pqz-zAQ", 
                            "https://i.ytimg.com/vi/IFcxEfRO3n4/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDjnZOV9NoYdqEQ1CU6-inxxDgDew"
                        ], 
                        "title": 
                            "Michou - FIER (Clip Officiel)",
                        "long_desc": 
                            "Le son est dispo partout, sur Spotify, Deezer, Apple Music etc ... go stream \u00e7a en balle https://michou.backl.ink/", 
                        "channel": 
                            "Michou", 
                        "duration": 
                            "2:23", 
                        "views": 
                            "18\u202f926\u202f651\u00a0vues", 
                        "url_suffix": 
                                "/watch?v=IFcxEfRO3n4"
                }, 
                {
                "id": 
                    "d07Q6SEqNBg",
                    "thumbnails": 
                    [
                        "https://i.ytimg.com/vi/d07Q6SEqNBg/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCFfPKhB1mnLyH_doz6bPpd55_1IA",
                        "https://i.ytimg.com/vi/d07Q6SEqNBg/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBIuTuq0Qaq016qTPYRQXMUrqeZIw"
                    ], 
                    "title": 
                        "CHANTER \"FIER\" DE MICHOU AVEC LA VOIX DE MICHOU (Parodie)", 
                        "long_desc": "Merci \u00e0 BIGO Live de Sponsoris\u00e9e cette Vid\u00e9o ! ^^ Le Lien pour t\u00e9l\u00e9charger l'appli\u00a0...", 
                        "channel":
                            "JESSY", "duration": "4:41", "views": "995\u202f525\u00a0vues", "url_suffix": "/watch?v=d07Q6SEqNBg"}, {"id": "rNOuH8NsjXM", "thumbnails": ["https://i.ytimg.com/vi/rNOuH8NsjXM/hqdefault.jpg?sqp=-oaymwEjCOADEI4CSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDNxLVtEd2UaaQkiVNXvTZO7YJYog"], "title": "Michou - FIER 1h", "long_desc": "On est tous fiehiehier!", "channel": "1M vues", "duration": "59:23", "views": "236\u202f653\u00a0vues", "url_suffix": "/watch?v=rNOuH8NsjXM"}, {"id": "Z9vcgGU6BQ4", "thumbnails": ["https://i.ytimg.com/vi/Z9vcgGU6BQ4/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDusrM7kYGYmHhcsDgAWUm0DPd-Qg", "https://i.ytimg.com/vi/Z9vcgGU6BQ4/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBsy7IHWyd6gkej05d2_Jn68UUNgQ"], "title": "Fier", "long_desc": "Provided to YouTube by Believe SAS ", "channel": "Michou - Topic", "duration": "2:21", "views": "1\u202f092\u202f406\u00a0vues", "url_suffix": "/watch?v=Z9vcgGU6BQ4"}, {"id": "PaPVQ3NSdLM", "thumbnails": ["https://i.ytimg.com/vi/PaPVQ3NSdLM/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLC6smVEGp-pt860X17XGgevG2LxOg", "https://i.ytimg.com/vi/PaPVQ3NSdLM/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLB4qSw_OdT6sGCl8AYRR8YMLQ7JZQ"], "title": "MICHOU - FIER [ PARODIE FORTNITE ]", "long_desc": "SALUT \u00c0 TOUS AUJOURD'HUI ON SE RETROUVE POUR UNE TOUTE NOUVELLE VID\u00c9O ! SI VOUS AVEZ AIMEZ L\u00c0 VID\u00c9O\u00a0...", "channel": "JENATHANPAS", "duration": "2:44", "views": "84\u202f325\u00a0vues", "url_suffix": "/watch?v=PaPVQ3NSdLM"}]}
"""