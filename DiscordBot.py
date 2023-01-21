import discord
import random

from discord import client
from discord.ext import commands


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await self.change_presence(status=discord.Status.online, activity=discord.Game('Apex Legends'))
        print('Bot is Ready')

    @commands.command()
    async def random(self, ctx, username=None):
        items = ["item 1", "item 2", "item 3"]

        await ctx.send(random.choice(items))
        return

    """
    @commands.has_permissions(administrator=True)
    @client.command(aliases=["purge", "delete", "clear"])
    async def sell(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        embed = discord.Embed(description=f"**Successfully Sold {amount} message(s) in {ctx.channel}!**",
                              color=discord.Colour.green())
        await ctx.send(embed=embed, delete_after=5)
     """

    async def on_message(self, message):
        # don't respond to ourselves
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.content)
        print(f'f{username}: {user_message} ({channel}')

        if message.author == client.user:
            return

        if message.channel.name == 'chat-bot':
            if user_message.lower() == 'hello':
                await message.channel.send(f'Hello {username}!')
                return
            elif user_message.lower() == 'bye':
                await message.channel.send(f'See you later {username}')
                return
            elif user_message.lower() == 'random':
                response = f'This is your random number: {random.randrange(1000000)}'  # set random to million
                await message.channel.send(response)
                return

        if user_message.lower() == '!anywhere':
            await message.channel.send('This can be used anywhre')
            return

        if message.author == client.user:
            return

        if message.content == 'cool':
            await message.add_reaction('\U0001F92C')

        @client.event
        async def on_message_edit(before, after):
            await before.channel.send(
                f'{before.author} edited a message\n'
                f'Before: {before.content}\n'
                f'After: {after.content}'
            )

        @client.event
        async def on_reaction_add(reaction, user):
            await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents, command_prefix='/')
client.run('')
