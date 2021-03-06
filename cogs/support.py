import discord
from discord.ext import commands

class Support(commands.Cog):

  def __init__(self, bot):
      self.bot = bot

  @commands.command()
  @commands.cooldown(1, 300, commands.cooldowns.BucketType.user)
  async def donate(self, ctx):
    em = discord.Embed(title="Patreon", description='[Donate Here!](https://www.patreon.com/lynden_sylvester "Donate")', color = ctx.author.color)
    await ctx.send(embed = em)
  
  @commands.command()
  @commands.cooldown(1, 300, commands.cooldowns.BucketType.user)
  async def support(self, ctx):
    em = discord.Embed(title="Support", description='[Join Us!](https://discord.gg/FFhw4nH5TZ "Support Server")', color = ctx.author.color)
    await ctx.send(embed = em)

  @commands.command()
  @commands.cooldown(1, 300, commands.cooldowns.BucketType.user)
  async def fb(self, ctx):

    author = ctx.message.author

    msg = ctx.content.message.lower()
    
    

def setup(bot):
    bot.add_cog(Support(bot))
