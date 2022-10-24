from discord.ext import commands
import os
import dbl

dbl_token = os.environ.get("dblpy")

class TopGG(commands.Cog):
     """
     This example uses dblpy's webhook system.
     In order to run the webhook, at least webhook_port must be specified (number between 1024 and 49151).
     """

     def __init__(self, bot):
         self.bot = bot
         self.token = dbl_token  # set this to your DBL token
         self.dblpy = dbl.DBLClient(self.bot, self.token, webhook_path='/webhook', webhook_auth='Lynden Sylvester', webhook_port=8080)

     @commands.Cog.listener()
     async def on_dbl_vote(self, data):
         """An event that is called whenever someone votes for the bot on top.gg."""
         print("Received an upvote:", "\n", data, sep="")

     @commands.Cog.listener()
     async def on_dbl_test(self, data):
         """An event that is called whenever someone tests the webhook system for your bot on top.gg."""
         print("Received a test upvote:", "\n", data, sep="")


def setup(bot):
    bot.add_cog(TopGG(bot))