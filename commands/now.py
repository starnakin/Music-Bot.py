import discord
from discord.ext import commands

import music

def setup(bot):
    bot.add_cog(now(bot))

class now(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def now(self, ctx):
        try:
            await ctx.send(music.actually_song)
        except:
            await ctx.send("pas song")