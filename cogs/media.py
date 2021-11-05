import discord
from discord.ext import commands

class Media(commands.Cog):

  def __init__(self, bot):
      self.bot = bot

  @commands.command()
  @commands.cooldown(1, 3600, commands.cooldowns.BucketType.user)
  async def youtube(self, ctx):
    em = discord.Embed(title="Official YouTube", description='[Watch Our Videos!](https://www.youtube.com/channel/UCtfqVfWW5AnHVZ7_D7BjoHA/featured "Subscribe to Tinker MC on YouTube!")', color = ctx.author.color)
    await ctx.send(embed = em)
    
  @commands.command()
  @commands.cooldown(1, 3600, commands.cooldowns.BucketType.user)
  async def tiktok(self, ctx):
    em = discord.Embed(title="Official TikTok", description='[Join Us!](https://vm.tiktok.com/ZMen2xwg8/ "Official Tiktok")', color = ctx.author.color)
    await ctx.send(embed = em)
    
  ''''
  #Twitch
  @commands.command()
  @commands.cooldown(1, 3600, commands.cooldowns.BucketType.user)
  async def twitch(self, ctx):
    em = discord.Embed(title="cosnexx", description='[Follow](https://www.twitch.tv/cosnexx "Twitch")', color = ctx.author.color)
    await ctx.send(embed = em)
'''

def setup(bot):
    bot.add_cog(Media(bot))



