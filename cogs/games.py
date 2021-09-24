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
    async def Slots(self, ctx, arg):
      ''''
      <:Sacrifice_Currency:836728434251268137> 
      <:Mythic_Currency:836723947268866049> 
      <:Legendary_Currency:836723947130716231> 
      <:Epic_Currency:836723947148017725> 
      <:Rare_Currency:836723947373723678> 
      <:Uncommon_Currency:836723947394433034>
      <:Common_Currency:836723947348557855>
      '''
      options = ["<:Common_Currency:836723947348557855>", 2, 3, 4, 5, 6, 7, 8]

      slot_machine = []

      bet = int(arg)
      print(bet)
      roll = 0
      while roll < 3:
        choose = random.randint(0, 7)
        print("choose:" + str(choose))
        slot_machine.append(options[choose])
        print("options[choose]: " + str(options[choose]))
        print("slots:" + str(slot_machine))
        roll += 1
      if slot_machine[0] == slot_machine[1] == slot_machine[2]:
        bet = bet * 2
        slot_machine = str(slot_machine).strip("[],")
        await ctx.send(f"{slot_machine} \nYou won and got {bet}!")
      elif ((slot_machine[0] == slot_machine[1]) or (slot_machine[1] == slot_machine[2]) or (slot_machine[2] == slot_machine[0])):
        bet = int(bet * 0.5)
        slot_machine = str(slot_machine).strip("[],")
        await ctx.send(f"{slot_machine} \nYou got {bet}! Better luck next time!")
      else:
        slot_machine = str(slot_machine).strip("[],")
        await ctx.send(f"{slot_machine} \nYou lost {bet}! Better luck next time!")

    @commands.command()
    async def turtle(self, ctx, arg):
      Grid = [["1", "2", "3"],
              ["4", "5", "6"],
              ["7", "8", "9"]]

      if "HammerTime" == arg:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        smash = Grid[row][col]

        print("\n" + smash + "\n")
        i = 0
        while i < 3:
          print(Grid[i])
          i += 1
        

def setup(bot):
    bot.add_cog(Games(bot))
