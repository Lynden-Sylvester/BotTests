import datetime
from datetime import timedelta
from discord.ext import commands

class Login(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.cooldowns.BucketType.user)
    async def login(self, ctx):
        #set %H:%M:%S to 00:00:00 for Live Counter
        midnight = "00:00:00"
        #now
        currentTime = datetime.datetime.now()
        timedelta(days=0, hours=0, minutes=0)
        #tmr
        nextDay = currentTime + timedelta(days=0)
        nextDay = nextDay.strptime(nextDay.strftime("%Y/%m/%d ") + midnight, "%Y/%m/%d %H:%M:%S")
        print(nextDay)
        currentTime = currentTime.strptime(currentTime.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        print(currentTime)
        #Live Counter
        diff = currentTime - nextDay
        await ctx.send(diff)
        #embed here
        await ctx.send("\u200b")

def setup(bot):
    bot.add_cog(Login(bot))