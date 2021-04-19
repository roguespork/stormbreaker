import random
from discord.ext import commands

class GuessTheNumber(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def startgame_guessthenumber(self, ctx):
        await ctx.send('Generating number...')

    @commands.command()
    async def guess(self, ctx, number):
        await ctx.send(f'Guess: {number}')
        await ctx.message.delete()

    @commands.command()
    async def resetguessingnumber(self, ctx):
        print('Hello world!')        


def setup(bot):
    bot.add_cog(GuessTheNumber(bot))
