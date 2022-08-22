import discord
import os
from discord.ext import commands
import sqlite3
from keep_alive import keep_alive
import random

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = "~", help_command=None)

#connect to database
db = sqlite3.connect('tinker.db')
#create a cursor
crsr = db.cursor()
#create the table if it doesn't exist
sql_command = """CREATE TABLE IF NOT EXISTS tinker (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_cash INTEGER,
user_id INTEGER UNIQUE);"""
crsr.execute(sql_command)

db.commit()
db.close()

db = sqlite3.connect("tinker.db")

crsr = db.cursor()

crsr.execute(sql_command)

db.commit()
rows = crsr.fetchall()
for row in rows:
  print(f"Rows: {row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]}")
db.close()

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    mins = error.retry_after / 60
    hrs = mins % 24
    hrs = hrs - 1
    mins = mins % 60
    if mins > 1:
      mins = mins -1
    sec = error.retry_after % 60
    if error.retry_after > 3600:
      await ctx.send(f"😡 You must wait **{hrs:.0f}:{mins:.0f}:{sec:.0f}s!**")
    elif error.retry_after > 60:
      await ctx.send(f"😡 You must wait **{mins:.0f}:{sec:.0f}s!**")
    else:
      await ctx.send(f"😡 You must wait **{sec:.0f}s!**")

'''
@bot.event
async def on_guild_join(guild, ctx):
  if guild.channel == 'general':
    await ctx.send("Use `eg!work` to get your first money, then try out other commands!")
'''

@bot.event
#@bot.listen('on_message')
async def on_message(ctx):
  '''try:
    if ctx.message.raw_role_mentions or '@everyone' in ctx.message.content or '@here' in ctx.message.content:
      print("nope")
  except AttributeError:
    pass
  else:'''
    #set your timezone with `~tz gmt[+/-offset]`,
  if bot.user.mentioned_in(ctx):
      await ctx.channel.send("Use ``~work`` to get your first money,then try out other commands!")
  await bot.process_commands(ctx)



def db_test():
  db = sqlite3.connect("tinker.db")

  crsr = db.cursor()

  crsr.execute("""SELECT t.*, u.user from users as u INNER JOIN tinker as t ON t.user_id = u.user_id;""")
  print("Joined")

  db.commit()

  rows = crsr.fetchall()
  for row in rows:
    print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
  db.close()

db_test()
keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
try:
  bot.run(token)
except:
  os.system("kill 1")