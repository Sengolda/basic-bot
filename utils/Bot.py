import discord
from discord.ext import commands,tasks
import os
import traceback

from discord.ext.commands.core import command
from discord.flags import Intents

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or("!"),
        intents=Intents.all()
        )
    
    
    def load_ext(self,name):
        return super().load_extension(name)

    def run(self,token:str = None):
        return super().run(token or '')
    def load_extensions(self):
        for i in os.listdir('cogs'):
            if i.endswith(".py"):
                if not i.startswith("_"):
                    try:
                        e = i[:-3]
                        self.load_ext("cogs.{0}".format(e))
                    except Exception as ee:
                        traceback.print_exception(type(ee), ee, ee.__traceback__)
    @tasks.loop(seconds=0,count=1)
    async def load_exts(self):
        self.load_extensions()


    async def on_ready(self):
        print("Logged in as",self.user)
        print("Loading cogs")
        await self.load_exts.start()
        print("loaded all of the cogs!")
        print("-------------------")