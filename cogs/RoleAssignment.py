import discord
from discord.ext import commands
import discord.utils
import os
import functools
import json
import sys


class roleAssign(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def on_member_join(self, ctx, member):
        await ctx.send('Hello new spoon!')

def setup(bot):
    bot.add_cog(roleAssign(bot))