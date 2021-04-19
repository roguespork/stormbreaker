import discord
import os
import time
import random
import requests
import json
import asyncio

with open('dconfig.json') as f:
    data = json.load(f)

fireside_token = data['token']
fireside_prefix = data['prefix']

from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True)
# intents.reactions = True

rules = [
    ':one: Make sure to follow Discord TOS and Guidelines.',
    ':two: Do not be an assbutt. We will kick you.',
    ':three: When in doubt, ask for permission rather than begging for forgiveness.'
]

spork_rules = [
    '**THIS IS GOING TO WORK!!**'
]

client = commands.Bot(command_prefix = fireside_prefix, intents = intents)

@client.event
async def on_ready():
    print('Hello boys. Miss me?')

# @client.event
# async def on_message(ctx, message):
#     if "wanker" in message.content:
#         print('Hello World')
#         #or
#         await message.channel.send("somthing else")
#         await ctx.send('Hey! We don\'t say that on this server')
#     await client.process_commands(message)
# @client.command()
# async def wanker(ctx, *, message):
#     await ctx.send(f'HEY {ctx.author.mention}! We don\'t say that here!')
#     await ctx.channel.purge(limit=2)

@client.command()
async def ping(ctx):
    await ctx.send(f'PONG! {round(client.latency * 1000)}ms')

@client.command(aliases=['rules'])
async def rule(ctx, *, number):
    
    choice = int(number)
    rule_total = len(rules)
    
    if choice > rule_total:
        await ctx.message.delete()
        await ctx.send('Not enough rules yet.')
        return
    if choice <= rule_total or choice == rule_total:
        await ctx.send(rules[int(number)-1])
        await ctx.message.delete()
        print(f'Rule was requested by {ctx.author}')


@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit = amount)

@client.command(aliases=['valerie'])
async def ping_random(ctx):
    member = random.choice(ctx.guild.memebers)
    await ctx.send(f"{member.mention}")
    await ctx.message.delete()
    
@client.command(aliases=['winchester'])
async def waywardson(ctx):
    await ctx.message.delete()
    print(f'WaywardSon Protocol activated by {ctx.author}')
    await ctx.send(':notes: Carry on my wayward son... :notes:')
    time.sleep(2)
    await ctx.send(':notes: There\'ll be peace when you are done.:notes:')
    time.sleep(3)
    await ctx.send(':notes: Lay your weary head to rest...:notes:')
    time.sleep(10)
    await ctx.send(':notes:*Don\'t you cry no more*:notes:')
    # await ctx.send(':notes:  Carry on my wayward son... \n There\'ll be peace when you are done.\n Lay your weary head to rest...\n *Don\'t you cry no more*:notes:')



@client.command(aliases = ['8ball', 'test'])
async def _8ball(ctx, *, question):
    print(f'8 ball activated by {ctx.author}')
    responses = ["Yes, most definitely!", 
        "The chances are high!", 
        "Not likely!", 
        "May the odds be ever in your favor.", 
        "You got no shot, kid.", 
        "Try it out and see!", 
        "23 percent of working", 
        "99.9 percent success rate",
        "Congratulations, yes!", 
        "Ask a probably question," 
        "Ask again later", 
        "Better not tell you now",
        "Cannot predict now", 
        "Concentrate and ask again", 
        "Don't count on it"
	]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    await ctx.message.delete()

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server... rude!')

for filename in os.listdir('./cogs'):
    if filename.endswith('py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(fireside_token)