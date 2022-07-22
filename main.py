#libraries
import discord
from utils import *
from discord.ext import commands

#intents (used to detect member joins)
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

#client object
client = commands.Bot(command_prefix = 'z', case_insensitive = True, intents = intents)

#when the bot is ready to be used
@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')

#when the bot sees a message
@client.event
async def on_message(message):
    if message.guild.id == int(guild_id):
        if message.mentions:
            for user in message.mentions:
                if is_afk(str(user.id)) == True and str(user.id) != str(message.author.id):
                    await message.reply(f'**{user.name}** is AFK: `{get_message(user.id)}`')
        if is_afk(str(message.author.id)) == True:
            remove_afk(message.author.id)
            await message.channel.send(f'**{message.author.mention}**, you are no longer AFK')

#a simple command which sends the bots latency
@client.slash_command(name = 'ping', description = 'returns the client latency', usage = 'ping')
async def ping(ctx):
    if not int(guild_id)== ctx.guild.id:
        guild = client.get_guild(int(guild_id))
        await ctx.respond(f'{error_emoji} This command is only available in the `{guild}` server.')
    await ctx.respond(f'Pong! **{round(client.latency * 1000)}**ms 🏓')

#the command which sets a users afk status
@client.slash_command(name = 'afk', description = 'sets your afk status', usage = 'afk [status]')
async def afk(ctx, *, status:str):
    if not int(guild_id)== ctx.guild.id:
        guild = client.get_guild(int(guild_id))
        await ctx.respond(f'{error_emoji} This command is only available in the `{guild}` server.')
    if is_afk(ctx.author.id) == True:
        await ctx.respond(f'{error_emoji} You are already afk.')
    else:
        add_afk(ctx.author.id, status)
        await ctx.respond(f'{success_emoji} You are now afk.')


#logging in to the bot
client.run(token)
