from discord.ext import commands
import math
import sqlite3
import random
import os


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 120, commands.cooldowns.BucketType.user)
    async def fb(self, ctx):

        msg = ctx.message.content.lower()

        #Retrieve discord author message
        author = ctx.message.author
        print(msg)
        if "~fb" in msg:
            print(msg)
            os.system(f"echo **Author:** {author} >> ~/BotTests/feedback.md")
          
            os.system(
                f"echo **Feedback:** {msg[4:]} >> ~/BotTests/feedback.md")
          
            os.system(
                f"echo "" >> ~/BotTests/feedback.md")

def setup(bot):
    bot.add_cog(Games(bot))
