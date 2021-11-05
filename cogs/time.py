import datetime
import discord
from discord.ext import commands
#from currency import cash
from cogs.currency import cash2
import time
import sqlite3

gmt =["GMT", "GMT+1", "GMT+2", "GMT+3",
      "GMT+4", "GMT+5", "GMT+6", "GMT+7",
      "GMT+8", "GMT+9", "GMT+10", "GMT+11",
      "GMT+12", "GMT-11", "GMT-10", "GMT-9",
      "GMT-8", "GMT-7", "GMT-6", "GMT-5",
      "GMT-4", "GMT-3", "GMT-2", "GMT-1"]

alias =["UTC","ETC", "EET", "EAT",
        "NET", "PLT", "BST", "VST",
        "CTT", "JST", "AET", "SST",
        "NST", "MIT", "HST", "AST",
        "PST", "MST", "CST", "EST",
        "PRT", "BET", "No Alias", "CAT"]

class Time(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.cooldown(1, 5, commands.cooldowns.BucketType.user)
    async def tz(self, ctx, arg):
      tm = datetime.datetime.utcnow()

      author = ctx.message.author

      em = discord.Embed(title = "Timezones", description = "use ~tz <arg> to select your time zone!", color = ctx.author.color)

      if arg.upper() in gmt:
        for i in gmt:

          x = gmt.index(i)
          if (arg.upper() == gmt[x]):

            
            if x == 22:
              dn = tm - datetime.timedelta(hours=-x)
              t = dn.strftime("%m/%d/%Y %H:%M:%S")
              await ctx.send(f"Your timezone is now set to **{gmt[x]}** which has **{alias[x]}**")
              em.add_field(name = f"{gmt[x]}", value = f"{t}")

              
            else:
              await ctx.send(f"Your timezone is now set to **{gmt[x]}**, also known as **{alias[x]}**")
              if x < 13:
                d = tm + datetime.timedelta(hours=x)
                t = d.strftime("%m/%d/%Y %H:%M:%S")
              if x > 12:
                dn = tm - datetime.timedelta(hours=-x)
                t = dn.strftime("%m/%d/%Y %H:%M:%S")

                
              #await ctx.send(t)
              em.add_field(name = f"{gmt[x]}/{alias[x]}", value = f"{t}")
      if arg.upper() in alias:
        for i in alias:

          x = alias.index(i)
          if (arg.upper() == alias[x]):
            await ctx.send(f"Your timezone is now set to **{alias[x]}**, also known as **{gmt[x]}**")
            if x < 13:
              d = tm + datetime.timedelta(hours=x)
              t = d.strftime("%m/%d/%Y %H:%M:%S")
            if x > 12:
              dn = tm - datetime.timedelta(hours=-x)
              t = dn.strftime("%m/%d/%Y %H:%M:%S")
            #await ctx.send(t)
            em.add_field(name = f"{gmt[x]}/{alias[x]}", value = f"{t}")
      
      await ctx.send(embed = em)
      #prize = cash
      amt, emoji = cash2.randomize_prize2()
      #prize.randomize_prize()
      #await ctx.send(f"{prize.amt} {prize.emoji}")
      await ctx.send(f"{amt} {emoji}")

      

def setup(bot):
  bot.add_cog(Time(bot))