import discord
import random

TOKEN = 'xxx'
SERVER_ID = 123

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    for guild in client.guilds:
        if guild.id == SERVER_ID:
            print(f'Connected to server: {guild.name}')
            await reset_nicknames(guild)
            print(f'Nicknames reset for all members in the server.')
            break
    else:
        print(f'Bot is not a member of the specified server (ID: {SERVER_ID}). Exiting...')
        await client.close()

async def reset_nicknames(guild):
    for member in guild.members:
        try:
            await member.edit(nick=None)
        except Exception as e:
            print(f'An error occurred while resetting nickname for user {member.name} (ID: {member.id}): {e}')

client.run(TOKEN)
