import datetime
import discord
from discord.ext import commands
import random
import time
import sqlite3

'''commands.Cog'''

class cash2():
  ''''
  def __init__(self, bot):
      self.bot = bot
  '''
  emoji_pos = random.randint(0,7)

  common = "<:Common_Currency:836723947348557855>"
  uncommon = "<:Uncommon_Currency:836723947394433034>"
  rare = "<:Rare_Currency:836723947373723678>"
  epic = "<:Epic_Currency:836723947148017725>"
  legendary = "<:Legendary_Currency:836723947130716231>"
  mythic = "<:Mythic_Currency:836723947268866049>"
  sacrifice = "<:Sacrifice_Currency:836728434251268137>"

  emoji_array = [common, uncommon, rare, epic, legendary, mythic, sacrifice]

  amt = 0
  emoji = emoji_array[emoji_pos]

  def randomize_prize2():
    amt = random.randint(0, 5)
    emoji_pos = random.randint(0,7)

    common = "<:Common_Currency:836723947348557855>"
    uncommon = "<:Uncommon_Currency:836723947394433034>"
    rare = "<:Rare_Currency:836723947373723678>"
    epic = "<:Epic_Currency:836723947148017725>"
    legendary = "<:Legendary_Currency:836723947130716231>"
    mythic = "<:Mythic_Currency:836723947268866049>"
    sacrifice = "<:Sacrifice_Currency:836728434251268137>"

    emoji_array = [common, uncommon, rare, epic, legendary, mythic, sacrifice]
    emoji = emoji_array[emoji_pos]
    #common
    if emoji_pos == 0:
      amt = random.randint(10, 15)
    #uncommon
    if emoji_pos == 1:
      amt = random.randint(5, 10)
    #rare
    if emoji_pos == 2:
      amt = random.randint(0, 5)
    #epic
    if emoji_pos == 3:
      amt = random.randint(0, 3)
    #legendary
    if emoji_pos == 4:
      chance = random.randint(0, 1)
      if chance == 1:
        amt = random.randint(0, 2)
      else:
        amt = 0
    #mythic
    if emoji_pos == 5:
      chance = random.randint(0, 3)
      if chance == 3:
        amt = random.randint(0, 1)
      else:
        amt = 0
    #sacrifice
    if emoji_pos == 6:
      chance = random.randint(0, 7)
      if chance == 7:
        amt = random.randint(0, 1)
      else:
        amt = 0

    print(f"You earned: {amt} {emoji}")
    return amt, emoji
      
  ''''
  def setup(bot):
    bot.add_cog(cash(bot))
  '''