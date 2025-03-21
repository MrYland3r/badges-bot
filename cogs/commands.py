from discord.ext import commands
from utils.postfix_generator import generate_postfix
from utils.counter_utils import load_counter, save_counter

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command(name='update_nicknames')
async def update_nicknames(self, ctx):
    for member in ctx.guild.members:
        counter = load_counter()
        postfix = generate_postfix(counter)
        save_counter (counter +1)
        try:
            await member.edit(nick=f"{member.name} // {postfix}")
        except discord.Forbidden:
            print(f"Failed to update nickname for {member.name}")

def setup(bot):
    bot.add_cog(Commands(bot))
