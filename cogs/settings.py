from discord.ext import commands
import os



# Store role id
# Give Dev perms depending on role perms in subsequent servers


class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def admin():
        def predicate(ctx):
            return commands.check_any(commands.is_owner(),
                                      commands.has_role(os.getenv('Developer')))

        return commands.check(predicate)


def setup(bot):
    bot.add_cog(Settings(bot))
