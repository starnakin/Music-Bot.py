import discord
from discord.ext import commands

import database_manager

def setup(bot):
    bot.add_cog(DatabaseInit(bot))

class DatabaseInit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def db_init(self, ctx):
        database_manager.init()