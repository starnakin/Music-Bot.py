import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(pause(bot))

class pause(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pause(self, ctx):
        client = ctx.guild.voice_client
        if not client.is_paused():
            client.pause()