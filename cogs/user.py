from discord.ext import commands
import os


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 120, commands.cooldowns.BucketType.user)
    async def fb(self, ctx):

        msg = ctx.message.content.lower()
        author = ctx.message.author

      # Read user msg
      # Translate it into a bash echo command
      # Echo msg directly to feedback.md
        if "~fb" in msg:
            os.system(f"echo **Author:** {author} >> ~/BotTests/feedback.md")

            os.system(
                f"echo **Feedback:** {msg[4:]} >> ~/BotTests/feedback.md")

            os.system(f"echo " " >> ~/BotTests/feedback.md")


def setup(bot):
    bot.add_cog(Games(bot))
