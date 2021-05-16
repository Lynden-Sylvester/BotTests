from discord.ext import commands
import math
import sqlite3
import random

class Economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 300, commands.cooldowns.BucketType.user)
    async def work(self, ctx):
        #random number Gen
        cash_to_add = math.floor(random.random()*100)
        #Retrieve discord author message
        author = ctx.message.author
        #Connect to database
        connection = sqlite3.connect('tinker.db')
        #create cursor
        crsr = connection.cursor()
        #if the table is not empty update it
        try:
            crsr.execute("""INSERT INTO tinker (user_cash, user_token) VALUES (?, ?);""", (cash_to_add, author.id))
        except sqlite3.IntegrityError:
            crsr.execute("""UPDATE tinker SET user_cash = user_cash + ? WHERE user_token = ?;""", (cash_to_add, author.id))
        connection.commit()
        crsr.execute("""SELECT * FROM tinker""")
        rows = crsr.fetchall()
        for row in rows:
            print(f"{row[0]} {row[1]} {row[2]}")
        print("=========================")
        balance = crsr.execute("SELECT user_cash FROM tinker WHERE user_token = ?", (author.id,)).fetchone()
        connection.close()
        await ctx.send(f"Your Wallet: **$" + str(balance[0]) + "**\n")

    @commands.command()
    async def test(self, ctx):
      await ctx.send("Sacrifice: <:Sacrifice_Currency:836728434251268137>")
    

def setup(bot):
    bot.add_cog(Economy(bot))