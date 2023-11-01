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
            for member in guild.members:
                new_nickname = generate_random_nickname()
                try:
                    await member.edit(nick=new_nickname)
                except discord.Forbidden:
                    print(f'Unable to change nickname for user: {member.name} (ID: {member.id}) due to permissions.')
                except Exception as e:
                    print(f'An error occurred while changing nickname for user {member.name} (ID: {member.id}): {e}')
            print(f'Nicknames changed for all members in the server.')
            break
    else:
        print(f'Bot is not a member of the specified server (ID: {SERVER_ID}). Exiting...')
        await client.close()

def generate_random_nickname():
    emojis = ["👻", "💀", "☠️", "🎃", "🕸️", "⚰️", "🪦"]
    random.shuffle(emojis)
    return ''.join(emojis)

client.run(TOKEN)
