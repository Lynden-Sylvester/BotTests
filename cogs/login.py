import datetime
from datetime import timedelta
import discord
from discord.ext import commands

gmt =["GMT", "GMT+1", "GMT+2", "GMT+3",
      "GMT+4", "GMT+5", "GMT+6", "GMT+7",
      "GMT+8", "GMT+9", "GMT+10", "GMT+11",
      "GMT+12", "GMT-11", "GMT-10", "GMT-9",
      "GMT-8", "GMT-7", "GMT-6", "GMT-5",
      "GMT-4", "GMT-3", "GMT-2", "GMT-1"]

alias =["UTC","ETC", "EET/ART", "EAT",
        "NET", "PLT", "BST", "VST",
        "CTT", "JST", "AET", "SST",
        "NST", "MIT", "HST", "AST",
        "PST", "PNT", "MST", "CST",
        "EST/IET", "PRT", "AGT/BET", "CAT"]

class Login(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 86400, commands.cooldowns.BucketType.user)
    async def login(self, ctx):
        #set %H:%M:%S to 00:00:00 for Live Counter
        midnight = "00:00:00"
        #now
        currentTime = datetime.datetime.now()
        #tmr
        nextDay = currentTime + timedelta(days=1)
        nextDay = nextDay.strptime(nextDay.strftime("%Y/%m/%d ") + midnight, "%Y/%m/%d %H:%M:%S")
        print(nextDay)
        currentTime = currentTime.strptime(currentTime.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        print(currentTime)
        #Live Counter
        diff = nextDay - currentTime

        await ctx.send(diff)
        #embed here
        await ctx.send("\u200b")

def setup(bot):
    bot.add_cog(Login(bot))