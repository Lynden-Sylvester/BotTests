import discord
from discord.ext import commands
from cogs.settings import Settings, Developer

vip = Settings.admin
Settings.admin == False

class CustomHelp(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        author = ctx.message.author
        dev_role = ctx.guild.get_role(Developer)

        em = discord.Embed(title = "Help", description = "use !help <command> for more info on a command", color = ctx.author.color)

        em.add_field(name = "Games", value = "don | rps") #, turtle, + more")
        em.add_field(name = "Dailies", value = "work") #login, + more")
        em.add_field(name = "Support", value = "donate | support")
        #em.add_field(name = "Shops", value = "shop, echange, stock")
        if dev_role in ctx.author.roles:
        
          em.add_field(name = "Dev", value = "load | unload | reload")
          em.add_field(name = "Media", value = "youtube | tiktok")
        await ctx.send(embed = em)

    @help.command()
    async def rps(self, ctx):
        em = discord.Embed(title = "rps", description = "!rps is a rs a rock-paper-scissors game", color = ctx.author.color)

        em.add_field(name = "!rps", value = "Chance to win, lose or draw! Use !rps <arg>. <arg> can be scissors, paper, or rock")

        await ctx.send(embed = em)

    @help.command()
    async def don(self, ctx):
        em = discord.Embed(title = "Don", description = "!don is an all or nothing command", color = ctx.author.color)

        em.add_field(name = "!don", value = "Chance of x2 cash or x0!")

        await ctx.send(embed = em)

    @help.command()
    async def turtle(self, ctx):
        em = discord.Embed(title = "Turtle", description = "!turtle is a game where you smash turtles to make IceBreakei explode!", color = ctx.author.color)

        em.add_field(name = "!turtle", value = "Earn Game currency or a rare chance of premium currency!!")

        await ctx.send(embed = em)

    @help.command()
    async def login(self, ctx):
        em = discord.Embed(title = "Login", description = "!login is a command that rewards you for playing every day!", color = ctx.author.color)

        em.add_field(name = "!login", value = "Free cash every day! Each day is x2 of the day before! Max cap: 817.2K")

        await ctx.send(embed = em)

    @help.command()
    async def work(self, ctx):
        em = discord.Embed(title = "Work", description = "!work earns you $$!", color = ctx.author.color)

        em.add_field(name = "!work", value = "Earn anywhere from $0 to $100!")

        await ctx.send(embed = em)

    @help.command()
    async def shop(self, ctx):
        em = discord.Embed(title = "Shop", description = "!shop has items that can be bought for obtaining more currency **or** an advantage in games", color = ctx.author.color)

        em.add_field(name = "!shop", value = "Allows various benifits for cash, gives custom roles, and more!")

        await ctx.send(embed = em)

    @help.command()
    async def donate(self, ctx):
        em = discord.Embed(title = "Donate", description = "!donate to help fund bot development by becoming a Patreon supporter!", color = ctx.author.color)

        em.add_field(name = "!donate", value = "Support bot development for as little as $3/Month! It really helps!")

        await ctx.send(embed = em)

    @help.command()
    async def support(self, ctx):
        em = discord.Embed(title = "Support", description = "Join the Support Server!", color = ctx.author.color)

        em.add_field(name = "!support", value = "Allows you to influence bot development, access Beta commands, and help improve user experience!")

        await ctx.send(embed = em)

    @help.command()
    async def youtube(self, ctx):
        em = discord.Embed(title = "YouTube", description = "Watch our Videos!", color = ctx.author.color)

        em.add_field(name = "!youtube", value = "Support the server by subscribimg to our videos!")

        await ctx.send(embed = em)

    @help.command()
    async def tiktok(self, ctx):
        em = discord.Embed(title = "Tiktok", description = "Follow us on Tiktok!", color = ctx.author.color)

        em.add_field(name = "!tiktok", value = "Support the server by following us on Tiktok!")

        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(CustomHelp(bot))