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

kol = crsr.fetchall()
print(kol, "kol")
print("**************")

db.commit()
db.close()


db = sqlite3.connect("tinker.db")

crsr = db.cursor()

#sql_command = """SELECT * from users u INNER JOIN tinker t ON u.user_id = t.user_token;"""
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
    if mins > 1:
      mins = mins -1
    sec = error.retry_after % 60
    await ctx.send(f"😡 You must wait **{mins:.0f}:{sec:.0f}s!**")

'''
@bot.event
async def on_guild_join(guild, ctx):
  if guild.channel == 'general':
    await ctx.send("Use `eg!work` to get your first money, then try out other commands!")
'''

@bot.event
async def currency(self, ctx):
  reward = random.randint(0, 100)

  if reward >= 51:
    #Common
    await ctx.send("<:Common_Currency:836723947348557855>")
  if reward >= 26:
    #Uncommon
    await ctx.send("<:Uncommon_Currency:836723947394433034>")
  if reward >= 12:
    #Rare
    await ctx.send("<:Rare_Currency:836723947373723678>")
  if reward >= 7:
    #Epic
    await ctx.send("<:Epic_Currency:836723947148017725>")
  if reward >= 4:
    #Legend
    await ctx.send("<:Legendary_Currency:836723947130716231>")
  if reward >= 2:
    #Mythic
    await ctx.send("<:Mythic_Currency:836723947268866049>")
  if reward <= 1:
    #Sacrifice
    await ctx.send("<:Sacrifice_Currency:836728434251268137>")

@bot.event
#@bot.listen('on_message')
async def on_message(msg):
  #if f"<@{bot.user.id}>" in msg.content.split():
  #if msg.content.startswith(f"<@{bot.user.id}>"):
  if bot.user.mentioned_in(msg):
    await msg.channel.send("Use `~work` to get your first money, then try out other commands!")
  await bot.process_commands(msg)


def db_test():
  db = sqlite3.connect("tinker.db")

  crsr = db.cursor()

  #sql_command = ("""CREATE table IF NOT EXISTS discord_Web  as SELECT t.*, u.user from users as u INNER JOIN tinker as t ON t.user_token = u.user_id;""")

  crsr.execute("""SELECT t.*, u.user from users as u INNER JOIN tinker as t ON t.user_id = u.user_id;""")
  #crsr.execute(sql_command)
  print("Joined")

  db.commit()
  #crsr.execute("""SELECT * FROM discord_Web;""")

  rows = crsr.fetchall()
  print("Rows:" + str(rows))
  for row in rows:
    print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
  db.close()

db_test()
keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)