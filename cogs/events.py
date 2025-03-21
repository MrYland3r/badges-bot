from discord.ext import commands
from utils.postfix_generator import generate_postfix
from utils.counter_utils import load_counter, save_counter

class Events(commands.Cog):
    def __ini(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Update nickname when new member joins."""
        counter = load_counter()
        postfix = generate_postfix(counter)
        save_counter(counter +1)
        try:
            await member.edit(nick=f"{member.name} // {postfix}")
        except discord.Forbidden:
            print(f"Failed to update nickname for {member.name}")

def setup(bot):
    bot.add_cog(Events(bot))
