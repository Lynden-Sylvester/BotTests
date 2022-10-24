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

        if msg != "~rps":
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
        bal = await ctx.send(f"You now have: **$" + str(bal[0] + values) +
                             "!**")

        cols = crsr.fetchall()
        for row in cols:
            print(f"{row[0]} {row[1]} {row[2]}")
        bal = crsr.execute("SELECT user_cash FROM tinker WHERE user_id = ?",
                           (author.id, )).fetchone()
        connection.close()

    @commands.command()
    async def Slots(self, ctx, arg):
        # Emojis
        sacrifice = '<:Sacrifice_Currency:836728434251268137>'
        mythic = '<:Mythic_Currency:836723947268866049>'
        legend = '<:Legendary_Currency:836723947130716231>'
        epic = '<:Epic_Currency:836723947148017725>'
        rare = '<:Rare_Currency:836723947373723678>'
        uncommon = '<:Uncommon_Currency:836723947394433034>'
        common = '<:Common_Currency:836723947348557855>'

        options = [common, uncommon, rare, epic, legend, mythic, 7, sacrifice]

        Machine = [10, 11, 12]

        bet = int(arg)
        roll = 0
        while roll < len(Machine):

            Machine[roll] = random.randint(0, 7)

            roll += 1

        if Machine[0] == Machine[1] == Machine[2]:
            bet = bet * 2
            await ctx.send(
                f"{options[Machine[0]]}{options[Machine[1]]}{options[Machine[2]]}"
            )
            await ctx.send(f"You won **${bet}**!")

        elif (Machine[0] == Machine[1]) or (Machine[1] == Machine[2]) or (Machine[2] == Machine[0]):
            bet = int(bet * 1.5)
            await ctx.send(
                f"{options[Machine[0]]}{options[Machine[1]]}{options[Machine[2]]}"
            )
            await ctx.send(f"You won **${bet}**!")

        else:
            bet = bet
            await ctx.send(
                f"{options[Machine[0]]}{options[Machine[1]]}{options[Machine[2]]}"
            )
            await ctx.send(f"You won **${bet}**!")

    @commands.command()
    async def turtle(self, ctx, arg):
        Grid = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

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
