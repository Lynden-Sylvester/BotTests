from discord.ext import commands
import os

class DevTools(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  #async def contextCheck(msg):
    
  
  async def nfile(self, ctx):
    msg = ctx.message.content.lower()

    ctxArray = msg.split(" ")
    
    if "~nfile" in msg:

      if "." in msg:
        Direc = ctxArray[2]
        fileName = ctxArray[1]
        
      
      if Direc in msg:
        os.system(f"cd {Direc}")
        os.system(f"touch {fileName}")
      else:
        await ctx.send("Directory not found, could not create file in nonexistent directory.")
        print("Directory not found, could not create file in nonexistent directory")


  async def ndir(self, ctx):

    msg = ctx.message.content.lower()
    ctxArray = msg.split("/")

    if "~ndir" in msg:

      os.system(f"cd {ctxArray[2]}")
      os.system(f"mkdir {ctxArray[1]}")

    else :
      await ctx.send("Directory Path not Found, could not create directory to nonexistent path")
      print("Directory Path  not found, could not create directory in nonexistent path")

  async def wfile(self, ctx):
    msg = ctx.message.content.lower()
    ctxArray = msg.split(" ")

    fileName = ctxArray[1]
    filePath = ctxArray[2]
    fileContents = ctxArray[3]
    
    if "~wfile" in msg:
      #contextCheck(msg)
      os.system(f"cd {filePath}")
      os.system(f"touch {fileName}")
      os.system(f"echo {fileContents} > {fileName}")
    else:
      await ctx.send("File Path not Found, could not write to file in nonexistent path")
      print("File Path  not found, could not write to file in nonexistent path")

  async def rfile (self, ctx):
    msg = ctx.message.content.lower()

    ctxArray = msg.split(" ")
    fileName = ctxArray[1]
    filePath = ctxArray[2]

    if "~rfile" in msg:
      os.system(f"cd {filePath}")
      fileContents = os.popen(f"cat {fileName}").read()
      await ctx.send(fileContents)
    else:
      await ctx.send("File Path not Found, could not read from file in nonexistent path")
      print("File Path  not found, could not read from file in nonexistent path")

  async def rmfile(self, ctx):
    msg = ctx.message.content.lower()
    ctxArray = msg.split(" ")
    fileName = ctxArray[1]
    filePath = ctxArray[2]
    
    if "~rmfile" in msg:
      os.system(f"cd {filePath}")
      os.system(f"rm {fileName}")
    else:
      await ctx.send("File Path not Found, could not remove file in nonexistent path")
      print("File Path  not found, could not remove file in nonexistent path")

  async def mergefile(self, ctx):
    msg = ctx.message.content.lower()
    ctxArray = msg.split(" ")
    NewFile = ctxArray[1]
    fileName1 = ctxArray[2]
    fileName2 = ctxArray[3]
    filePath = ctxArray[4]

    if "~mergefile" in msg:
      os.system(f"cd {filePath}")
      os.system(f"touch {NewFile}")
      os.system(f"cat {fileName1} >> {NewFile}")
      os.system(f"cat {fileName2} >> {NewFile}")
    else:
        await ctx.send("File Path not Found, could not merge files in nonexistent path")
        print("File Path  not found, could not merge files in nonexistent path")
      
def setup(bot):
  bot.add_cog(DevTools(bot))