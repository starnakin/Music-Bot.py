import youtube_dl
import discord
import asyncio

musics = {}
ytdl = youtube_dl.YoutubeDL()
actually_song=""

class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

def next(bot, queue, client):
    if len(queue) > 0:
        new_song = queue[0]
        del queue[0]
        play_song(bot, client, queue, new_song)
    else:
        asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)

def play_song(bot, client, queue, song): 
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))
    def next2(_):
        next(bot,queue,client)
    client.play(source, after=next2)
    actually_song=song