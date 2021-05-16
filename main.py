import discord
import os
from discord.ext import commands
import sqlite3
from keep_alive import keep_alive


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = "!", help_command=None)

#connect to database
db = sqlite3.connect('tinker.db')
#create a cursor
crsr = db.cursor()
#create the table if it doesn't exist
sql_command = """CREATE TABLE IF NOT EXISTS tinker (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_cash INTEGER,
user_token INTEGER UNIQUE);"""
crsr.execute(sql_command)

kol = crsr.fetchall()
print(kol, "kol")
print("**************")

db.commit()
db.close()


db = sqlite3.connect("tinker.db")

crsr = db.cursor()

sql_command = """SELECT * from users u INNER JOIN tinker t ON u.user_id = t.user_token;"""
crsr.execute(sql_command)

db.commit()
rows = crsr.fetchall()
for row in rows:
  print(f"row{[0]} row{[1]} row{[2]} row{[3]} row{[4]} row{[5]} row{[6]}")
db.close()


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    mins = error.retry_after / 60
    if mins > 1:
      mins = mins -1
    sec = error.retry_after % 60
    await ctx.send(f"😡 You must wait **{mins:.0f}:{sec:.0f}s!**")



keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)


