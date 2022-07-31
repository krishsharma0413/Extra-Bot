import nextcord 
from nextcord.ext import commands

class ytsearch(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Youtube Search Command
    @commands.command(pass_context=True)
    async def ytSearch(self,ctx, arg):
        ytEmbed = nextcord.Embed(
        title=arg,
        color=0x2852fa,
        description=f"Click The Text Above To Got To Your Youtube Search \n\nRequested By <@{ctx.author.id}>",
        url=f"https://www.youtube.com/results?search_query={arg}"
        )
        await ctx.send(embed=ytEmbed)    

    #Youtube Search Exception
    @ytSearch.error
    async def ytSearch_error(self,error,ctx):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send(f"<@{ctx.author.id}> \nThe Command Usage Of This Command Is ` -ytSearch [Query]")

#Setup 
def setup(client):
    client.add_cog(ytsearch(client))