import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(skip(bot))

class skip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def skip(self, ctx):
        client = ctx.guild.voice_client
        client.stop()