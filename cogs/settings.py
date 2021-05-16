from discord.ext import commands

Developer = 826114633106063420

class Settings(commands.Cog):

  def __init__(self, bot):
      self.bot = bot

  def admin():
        def predicate(ctx):
          return commands.check_any(commands.is_owner(), commands.has_role(Developer))
        return commands.check(predicate)

def setup(bot):
    bot.add_cog(Settings(bot))