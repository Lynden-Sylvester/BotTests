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
        cash_to_add = math.floor(random.random() * 100)
        #Retrieve discord author message
        author = ctx.message.author
        #Connect to database
        connection = sqlite3.connect('tinker.db')
        #create cursor
        crsr = connection.cursor()
        #if the table is not empty update it
        try:
            crsr.execute(
                """INSERT INTO tinker (user_cash, user_id) VALUES (?, ?);""",
                (cash_to_add, author.id))
        except sqlite3.IntegrityError:
            crsr.execute(
                """UPDATE tinker SET user_cash = user_cash + ? WHERE user_id = ?;""",
                (cash_to_add, author.id))
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
        await ctx.send(f"Your Wallet: **$" + str(balance[0]) + "**\n")

    @commands.command()
    @commands.cooldown(1, 300, commands.cooldowns.BucketType.user)
    async def bal(self, ctx):
        #Retrieve discord author message
        author = ctx.message.author
        #Connect to database
        connection = sqlite3.connect('tinker.db')
        #create cursor
        crsr = connection.cursor()
        # get user bal from the database
        balance = crsr.execute(
            """SELECT user_cash FROM tinker WHERE user_id = ?;""",
            (author.id, )).fetchone()
        connection.close()
        await ctx.send(f"Your Wallet: **$" + str(balance[0]) + "**\n")

    @commands.command()
    @commands.cooldown(1, 300, commands.cooldowns.BucketType.user)
    async def pay(self, ctx):
        #Retrieve Discord author message
        author = ctx.message.author
        #connect to database
        connection = sqlite3.connect('tinker.db')
        #create cursor
        crsr = connection.cursor()

        crsr.execute("""SELECT * FROM tinker""")
        rows = crsr.fetchall()
        print("=========================")
        for row in rows:
            print(f"{row[0]} {row[1]} {row[2]}")
        print("=========================")
        print("Before DB Update")

        connection.commit()

        # Break down the message into its core components
        msg = ctx.message.content.lower()
        listOfPay = msg.split()

        k = 0
        for i in listOfPay:
            if k != 2:
                print(listOfPay[k])
            k += 1
        recipient = listOfPay[2]
      #.strip("<>!@")
        print(listOfPay[2])

        cash_difference = int(listOfPay[1])

        # Update the author's balance
        crsr2 = connection.cursor()
        
        crsr2.execute(
            """UPDATE tinker SET user_cash = user_cash - ? WHERE user_id = ?;""",
            (cash_difference, author.id))
       
        connection.commit()
       
        crsr2.execute("""SELECT * FROM tinker""")

        rows2 = crsr2.fetchall()

        print("=========================")
        for row2 in rows2:
            print(f"{row2[0]} {row2[1]} {row2[2]}")
        print("=========================")

        connection.commit()
        # get user bal from the database
        author_balance = crsr2.execute(
            """SELECT user_cash FROM tinker WHERE user_id = ?""",
            (author.id, )).fetchone()

        author_balance = crsr2.execute(
            """SELECT user_cash FROM tinker WHERE user_id = ?;""",
            (author.id, )).fetchone()
        print(f" new author balance: " + str(author_balance[0]))

        connection.commit()
      
        # Update the recipient's balance
        crsr3 = connection.cursor()
        
        crsr3.execute(
            """UPDATE tinker SET user_cash = user_cash + ? WHERE user_id = ?;""",
            (cash_difference, recipient))
       
        connection.commit()
       
        crsr3.execute("""SELECT * FROM tinker""")

        rows3 = crsr3.fetchall()

        print("=========================")
        for row3 in rows3:
            print(f"{row3[0]} {row3[1]} {row3[2]}")
        print("=========================")

        connection.commit()
        # get user bal from the database
        recipient_balance = crsr3.execute(
            """SELECT user_cash FROM tinker WHERE user_id = ?""",
            (recipient, )).fetchone()

        recipient_balance = crsr3.execute(
            """SELECT user_cash FROM tinker WHERE user_id = ?;""",
            (recipient, )).fetchone()
        print(f" new recipient balance: " + str(recipient_balance[0]))

        connection.commit()
      
        connection.close()

        print(
            f"Your balance is now: **${author_balance[0]}**\n You paid **{recipient}** **${cash_difference}**\n **{recipient}'s** balance is now: **{recipient_balance[0]}**")

        await ctx.send(
            f"Your balance is now: **${author_balance[0]}**\n You paid **{recipient}** **${cash_difference}**\n **{recipient}'s** balance is now: **{recipient_balance[0]}**")

def setup(bot):
    bot.add_cog(Economy(bot))
