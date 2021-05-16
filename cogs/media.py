import discord
from discord.ext import commands

class Media(commands.Cog):

  def __init__(self, bot):
      self.bot = bot

  @commands.command()
  async def youtube(self, ctx):
    em = discord.Embed(title="YouTube", description='[Watch Our Videos!](https://www.youtube.com/channel/UCtfqVfWW5AnHVZ7_D7BjoHA/featured "Subscribe to Tinker MC on YouTube!")', color = ctx.author.color)
    await ctx.send(embed = em)
  
  @commands.command()
  async def tiktok(self, ctx):
    em = discord.Embed(title="Support", description='[Join Us!](https://discord.gg/FFhw4nH5TZ "Tiktok")', color = ctx.author.color)
    await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Media(bot))



