import discord
from discord.ext import commands

import music

def setup(bot):
    bot.add_cog(quit(bot))

class quit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quit(self, ctx):
        client = ctx.guild.voice_client
        await client.disconnect()
        music.musics[ctx.guild].clear()