import discord
from discord.ext import commands

import music

from youtube_search import YoutubeSearch

musics=music.musics

def setup(bot):
    bot.add_cog(Play(bot))

def play(bot):
    bot.add_cog(Play(bot))

class Play(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, uri):
        if(uri.startswith("https")):
            if(uri.startswith("https://www.youtube.com/")):
                client = ctx.guild.voice_client
                if client and client.channel:
                    video = music.Video(uri)
                    musics[ctx.guild].append(video)
                    await ctx.send("+" + video.url)
                else:
                    channel = ctx.author.voice.channel
                    video = music.Video(uri)
                    musics[ctx.guild] = []
                    client = await channel.connect()
                    await ctx.send(f"Je lance : {video.url}")
                    music.play_song(self.bot, client, musics[ctx.guild], video)
        else:
            results = YoutubeSearch(uri, max_results=2).to_dict()     
            embed = discord.Embed(title=""+results[0]["title"], description="https://www.youtube.com/watch?v="+results[0]["id"]).set_image(url=results[0]["thumbnails"][0]).set_author(name=ctx.author.voice.channel)
            message = await ctx.channel.send(embed=embed)
            await message.add_reaction("✅")
            await message.add_reaction("❌")


