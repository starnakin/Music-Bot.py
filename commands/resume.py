import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(resume(bot))

class resume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def resume(self, ctx):
        client = ctx.guild.voice_client
        if client.is_paused():
            client.resume()
