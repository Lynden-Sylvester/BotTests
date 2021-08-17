from discord.ext import commands
import math
import sqlite3
import random


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 120, commands.cooldowns.BucketType.user)
    async def don(self, ctx):
        doubleOrNothing = math.floor(random.randint(0, 1))
        if doubleOrNothing == 1:
            doubleOrNothing += 1
        #Retrieve discord author message
        author = ctx.message.author
        connection = sqlite3.connect('tinker.db')
        #create cursor
        crsr = connection.cursor()
        crsr.execute(
            """UPDATE tinker SET user_cash = user_cash * ? WHERE user_id = ?;""",
            (doubleOrNothing, author.id))
        connection.commit()
        crsr.execute("""SELECT * FROM tinker""")
        rows = crsr.fetchall()
        for row in rows:
            print(f"{row[0]} {row[1]} {row[2]}")
        print("=========================")
        balance = crsr.execute(
            "SELECT user_cash FROM tinker WHERE user_id = ?",
            (author.id, )).fetchone()
        connection.close()
        if doubleOrNothing == 2:
            await ctx.send("🤑 Your wallet doubled to: **$" + str(balance[0]) +
                           "!**\n")
        else:
            await ctx.send("😔 You lost your wallet, and now have: **$" +
                           str(balance[0]) + "!**\n")

    @commands.command()
    @commands.cooldown(1, 60, commands.cooldowns.BucketType.user)
    async def rps(self, ctx):

        words = ["rock", "paper", "scissors"]
        choices = random.randint(0, 2)
        result = ["win", "draw", "lose"]
        botPick = words[choices]
        values = 0
        win = result[0]
        draw = result[1]
        lose = result[2]
        outcome = None
        msg = ctx.message.content.lower()

        #Retrieve discord author message
        author = ctx.message.author
        connection = sqlite3.connect('tinker.db')

        if msg != "!rps":
            await ctx.send(f"I chose {botPick}!")

        #Rock conditions
        if (words[0] in msg):

            if (botPick == words[0]):
                await ctx.send(f"**{draw}!**")
                outcome = 1

            elif (botPick == words[1]):
                await ctx.send(f" You **{lose}!**")
                outcome = 2

            elif (botPick == words[2]):
                await ctx.send(f" You **{win}!**")
                outcome = 0

            else:
                await ctx.send("Evaluation Failed")

        #Paper conditions
        elif (words[1] in msg):

            if (botPick == words[0]):
                await ctx.send(f"You **{win}!**")
                outcome = 0

            elif (botPick == words[1]):
                await ctx.send(f"**{draw}!**")
                outcome = 1

            elif (botPick == words[2]):
                await ctx.send(f" You **{lose}!**")
                outcome = 2

            else:
                await ctx.send("Evaluation Failed")

        #Scissor conditions
        elif (words[2] in msg):

            if (botPick == words[0]):
                await ctx.send(f"You **{lose}!**")
                outcome = 2

            elif (botPick == words[1]):
                await ctx.send(f" You **{win}!**")
                outcome = 0

            elif (botPick == words[2]):
                await ctx.send(f"**{draw}!**")
                outcome = 1

            else:
                await ctx.send("Evaluation Failed")

        #Exit upon initial fail
        else:
            await ctx.send("No valid arguments")
            return

        #create cursor
        crsr = connection.cursor()

        #Money transaction
        crsr.execute("""SELECT * FROM tinker""")
        rows = crsr.fetchall()
        print("=========================")
        for row in rows:
            print(f"{row[0]} {row[1]} {row[2]}")
        print("=========================")
        bal = crsr.execute("SELECT user_cash FROM tinker WHERE user_id = ?",
                           (author.id, )).fetchone()

        if outcome == 0:
            values = 50
            print("Win")
            crsr.execute(
                """UPDATE tinker SET user_cash = user_cash + ? WHERE user_id = ?;""",
                (values, author.id))
            connection.commit()

        elif outcome == 2:
            values = -50
            print("Lose")
            crsr.execute(
                """UPDATE tinker SET user_cash = user_cash + ? WHERE user_id = ?;""",
                (values, author.id))
            connection.commit()

        else:
            print("Draw")
            pass
        bal = await ctx.send(f"You now have: **" + str(bal[0] + values) +
                             "!**")

        cols = crsr.fetchall()
        for row in cols:
            print(f"{row[0]} {row[1]} {row[2]}")
        bal = crsr.execute("SELECT user_cash FROM tinker WHERE user_id = ?",
                           (author.id, )).fetchone()
        connection.close()

    @commands.command()
    async def slots(self, ctx, arg):
      options = [1, 2, 3, 4, 5, 6, 7, 8]

      slots = []

      bet = arg
      print(bet)
      roll = 0
      while roll < 3:
        choose = random.randint(0, 8)
        print("choose:" + str(choose))
        slots.append(options[choose])
        print("options[choose]: " + str(options[choose]))
        print("slots:" + str(slots))
        roll += 1
      slots = slots.strip("[],")
      if slots[0] == slots[1] == slots[2]:
        print("if clause")
        await ctx.send(f"{slots} \nYou won and got {bet*2}!")
      elif ((slots[0] == slots[1]) or (slots[1] == slots[2]) or (slots[2] == slots[0])):
        print("elif clause")
        await ctx.send(f"{slots} \nYou got {bet*0.5}! Better luck next time!")
      else:
        print("else clause")
        await ctx.send(f"{slots} \nYou lost {bet}! Better luck next time!")

    @commands.command()
    async def turtle(self, ctx):
        pass


def setup(bot):
    bot.add_cog(Games(bot))
