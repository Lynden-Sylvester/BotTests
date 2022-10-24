from discord.ext import commands
import os

Developer = os.getenv('Developer')

class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def admin():
        def predicate(ctx):
            return commands.check_any(commands.is_owner(),
                                      commands.has_role(Developer))

        return commands.check(predicate)

    #Unload command
    @commands.command()
    @commands.has_any_role(commands.is_owner(), Developer)
    async def unload(self, ctx, extension):
        try:
            self.bot.unload_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.send(f"{extension} could not be unloaded")
            await print(f"{extension} could not be unloaded")
            return
        await ctx.send(f"{extension} unloaded")
        await print(f"{extension} unloaded")

    #load command
    @commands.command()
    @commands.has_any_role(commands.is_owner(), Developer)
    async def load(self, ctx, extension):
        try:
            self.bot.load_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.send(f"{extension} could not be loaded")
            await print(f"{extension} could not be loaded")
            return
        await ctx.send(f"{extension} loaded")
        await print(f"{extension} loaded")

    #reload command
    @commands.command()
    @commands.has_any_role(commands.is_owner(), Developer)
    async def reload(self, ctx, extension):
        try:
            self.bot.unload_extension(f"cogs.{extension}")
            self.bot.load_extension(f"cogs.{extension}")
        except Exception as e:
            await ctx.send(f"{extension} could not be reloaded")
            await print(f"{extension} could not be reloaded")
            return
        await ctx.send(f"{extension} reloaded")
        await print(f"{extension} reloaded")


def setup(bot):
    bot.add_cog(Dev(bot))
