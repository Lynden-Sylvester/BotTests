import datetime
import discord
import random
import math
import sqlite3
from datetime import timedelta
from discord.ext import commands

color_choice = ["Red", "Orange", "Yellow", "Green",
                "Blue", "Indigo", "Violet"]

rank_role = ["Unranked", "Bronze", "Silver", "Gold",
              "Crystal", "Master", "Champion", "Titain"]

class Shops(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 300, commands.cooldowns.BucketType.user)
    async def shop(self, ctx):

        #set %H:%M:%S to 00:00:00 for Live Counter
        midnight = "00:00:00"
        #now
        currentTime = datetime.datetime.now()
        timedelta(days=1, hours=0, minutes=0)
        #tmr
        nextDay = currentTime + timedelta(days=1)
        nextDay = nextDay.strptime(nextDay.strftime("%Y/%m/%d ") + midnight, "%Y/%m/%d %H:%M:%S")
        currentTime = currentTime.strptime(currentTime.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        #Live Counter
        diff = nextDay - currentTime
        await ctx.send(diff)
        #embed here
        await ctx.send("\u200b")
        await ctx.send("Red")

    @commands.command()
    @commands.cooldown(1, 3600, commands.cooldowns.BucketType.user)
    async def stock(self, ctx):
      author = str(ctx.message.author)
      icon = str(ctx.author.avatar_url)
      gold = random.randint(0, 100)
      iron = random.randint(0, 200)
      coal = random.randint(0, 50)

      await ctx.send("<a:Increase:827968820559347742> <a:Decrease:828303375266873385>  <a:No_Change:828434647226384415> ")
      em = discord.Embed(title = "Stock", description = "Different items and their price values", color = ctx.author.color)

      em.add_field(name = "Gold", value = str(gold) + " <:Increase_Static:827971307819892806> ", inline = True)
      em.add_field(name = "Iron", value = str(iron) + "<:Decrease_Static:828303375124791317> ", inline = True)
      em.add_field(name = "Coal", value = str(coal) + "<:No_Change_Static:828434647200956428> ", inline = True)
      em.set_footer(text = "Requested by " + author[:-5], icon_url = icon)
      await ctx.send(embed = em)


      #Broken @L59 Revisit
      connection = sqlite3.connect('shops.db')
      crsr = connection.cursor()
      crsr.execute("""INSERT INTO shops (gold, iron, coal) VALUES (?, ?, ?);""", (gold, iron, coal))
      connection.commit()
      crsr.execute("""Select * FROM shops""")
      ans = crsr.fetchall()
      for row in ans:
          print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")
      print("**************")
      mine = crsr.execute("SELECT gold, iron, coal FROM shops", (gold, iron, coal)).fetchone()
      print(str(mine[0]))
      connection.close()

def setup(bot):
    bot.add_cog(Shops(bot))