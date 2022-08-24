import nextcord
from nextcord.ext import commands
from configparser import ConfigParser
from sys import platform

config=ConfigParser()
if platform == "linux" or platform == "linux2":
    config.read("../config.ini")
elif platform == "win32":
    config.read(".\config.ini")
 
guild_id_1=config["options"]["guild1_id"]
guild_id_2=config["options"]["guild2_id"]
guilds=[int(guild_id_1),int(guild_id_2)]

class GoogleSearch(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Google Search Command
    @nextcord.slash_command(guild_ids=guilds, description="Google Search Command")
    async def gsearch(self, interaction:nextcord.Interaction, query: str = nextcord.SlashOption(description="Query", required=True)):
        gEmbed = nextcord.Embed(
            title=query,
            description=f"Click The Text Above To Go To Your Google Search",
            url=f"https://www.google.com/search?query={query}",
            color=0x2852fa,
        )
        gEmbed.set_thumbnail("https://cdn.discordapp.com/attachments/991958269012758548/1003379889069641758/google.png")
        await interaction.response.defer()
        await interaction.followup.send(embed=gEmbed)

# Setup
def setup(client):
    client.add_cog(GoogleSearch(client))
