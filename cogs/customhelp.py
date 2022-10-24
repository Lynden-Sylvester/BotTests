import discord
from discord.ext import commands
from cogs.settings import Settings
import os

vip = Settings.admin
Settings.admin == False


class CustomHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # Generalize Embed into a functin
    # Append Dev Cogs to Embed
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        author = ctx.message.author
        author_roles = ctx.author.roles
        dev_role = ctx.guild.get_role(os.getenv('Developer'))

        # Developer Help Embed
        if (dev_role in author_roles):

            emDev = discord.Embed(
                title="Help",
                description="use ~help <command> for more info on a command",
                color=ctx.author.color)

            emDev.add_field(name="Games",
                            value="don | rps")  #, turtle, + more")
            emDev.add_field(name="Dailies", value="work")  #login, + more")
            emDev.add_field(name="Support", value="donate | support")

            emDev.add_field(name="QoL", value="bal")

            #em.add_field(name = "Shops", value = "shop, echange, stock")

            emDev.add_field(name="Dev", value="load | unload | reload")
            emDev.add_field(name="In-Progress",
                            value="tz | shop | stock | login")
            emDev.add_field(name="Media", value="youtube | tiktok | twitch")
            emDev.add_field(name="Timezones", value="tz gmt<+/-><1-12>")

            await ctx.send(embed=emDev)

        # User Help Embed
        else:

            em = discord.Embed(
                title="Help",
                description="use ~help <command> for more info on a command",
                color=ctx.author.color)

            em.add_field(name="Games", value="don | rps")  #, turtle, + more")
            em.add_field(name="Dailies", value="work")  #login, + more")
            em.add_field(name="Support", value="donate | support")

            em.add_field(name="QoL", value="bal")

            await ctx.send(embed=em)

    @help.command()
    async def rps(self, ctx):
        em = discord.Embed(
            title="rps",
            description="~rps is a rock-paper-scissors game",
            color=ctx.author.color)

        em.add_field(
            name="~rps",
            value="Chance to win, lose or draw! Use ~rps <arg>. <arg> can be scissors, paper, or rock"
        )

        await ctx.send(embed=em)

    @help.command()
    async def don(self, ctx):
        em = discord.Embed(title="don",
                           description="~don is an all or nothing command",
                           color=ctx.author.color)

        em.add_field(name="~don", value="Chance of x2 cash or x0!")

        await ctx.send(embed=em)

    @help.command()
    async def bal(self, ctx):
        em = discord.Embed(
            title="bal",
            description="~bal is a Quality Of Life (QOL) command",
            color=ctx.author.color)

        em.add_field(name="~bal", value="CDisplays your current balance!")

        await ctx.send(embed=em)

    @help.command()
    async def turtle(self, ctx):
        em = discord.Embed(
            title="Turtle",
            description=
            "~turtle is a game where you smash turtles to make IceBreakei explode!",
            color=ctx.author.color)

        em.add_field(
            name="~turtle",
            value="Earn Game currency or a rare chance of premium currency!!")

        await ctx.send(embed=em)

    @help.command()
    async def login(self, ctx):
        em = discord.Embed(
            title="Login",
            description=
            "~login is a command that rewards you for playing every day!",
            color=ctx.author.color)

        em.add_field(
            name="~login",
            value=
            "Free cash every day! Each day is x2 of the day before! Max cap: 817.2K"
        )

        await ctx.send(embed=em)

    @help.command()
    async def work(self, ctx):
        em = discord.Embed(title="Work",
                           description="~work earns you $$!",
                           color=ctx.author.color)

        em.add_field(name="~work", value="Earn anywhere from $0 to $100!")

        await ctx.send(embed=em)

    @help.command()
    async def shop(self, ctx):
        em = discord.Embed(
            title="Shop",
            description=
            "~shop has items that can be bought for obtaining more currency **or** an advantage in games",
            color=ctx.author.color)

        em.add_field(
            name="~shop",
            value=
            "Allows various benifits for cash, gives custom roles, and more!")

        await ctx.send(embed=em)

    @help.command()
    async def donate(self, ctx):
        em = discord.Embed(
            title="Donate",
            description=
            "~donate to help fund bot development by becoming a Patreon supporter!",
            color=ctx.author.color)

        em.add_field(
            name="~donate",
            value=
            "Support bot development for as little as $3/Month! It really helps!"
        )

        await ctx.send(embed=em)

    @help.command()
    async def support(self, ctx):
        em = discord.Embed(title="Support",
                           description="Join the Support Server!",
                           color=ctx.author.color)

        em.add_field(
            name="~support",
            value=
            "Allows you to influence bot development, access Beta commands, and help improve user experience!"
        )

        await ctx.send(embed=em)

    @help.command()
    async def youtube(self, ctx):
        em = discord.Embed(title="YouTube",
                           description="Watch our Videos!",
                           color=ctx.author.color)

        em.add_field(name="~youtube",
                     value="Support the server by subscribimg to our videos!")

        await ctx.send(embed=em)

    @help.command()
    async def tiktok(self, ctx):
        em = discord.Embed(title="Tiktok",
                           description="Follow us on Tiktok!",
                           color=ctx.author.color)

        em.add_field(name="~tiktok",
                     value="Support the server by following us on Tiktok!")

        await ctx.send(embed=em)

    @help.command()
    async def twitch(self, ctx):
        em = discord.Embed(title="Twitch",
                           description="Follow us on Twitch!",
                           color=ctx.author.color)

        em.add_field(name="~twitch",
                     value="Support the server by following us on Twitch!")

        await ctx.send(embed=em)

    @help.command()
    async def tz(self, ctx):
        em = discord.Embed(title="Timezones",
                           description="Set your timezone to your local time!",
                           color=ctx.author.color)

        em.add_field(name="Timezones",
                     value="use ~tz <arg> to select your time zone!")

        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(CustomHelp(bot))
