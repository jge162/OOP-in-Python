import discord
import random
from discord.ext import commands


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await self.change_presence(status=discord.Status.online, activity=discord.Game('Apex Legends'))
        print('Bot is Ready')

    @commands.command()
    async def random(self, ctx):
        items = ["item 1", "item 2", "item 3"]
        await ctx.send(random.choice(items))
        return

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
                response = f'This is your random number: {random.randrange(1000000)}'
                await message.channel.send(response)
                return

        if user_message.lower() == '!anywhere':
            await message.channel.send('This can be used anywhre')
            return


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents, command_prefix='!')
client.run('')
