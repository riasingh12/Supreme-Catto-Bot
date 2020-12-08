import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.event #function decorator denoting function is going to reperesent an event
async def on_ready(): #this function puts bot in ready-state
    await client.change_presence(status = discord.Status.idle, activity=discord.Game('crying'))
    print("Bot is ready")

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server")

@client.event
async def on_member_remove(member):
    print(f"{member} has left the server")

@client.command()
async def ping(ctx): #context is passed in automatically
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'test'])#these are the command words which can be used for the func _8ball
async def _8ball(ctx,*,question):#aestrisk allows to take in multiple arguments
    responses = ['Yes','No','Maybe']
    await ctx.send(f'Question:{question}\nAnswer:{random.choice(responses)}')

@client.command()
async def clear(ctx, amount=5): #amount of messages to delete (default = 5 messages)
    await ctx.channel.purge(limit=amount) #just taking context and acessing channel running and we're calling purge method and setting a limit of the amt of messages to be removed

@client.command()
async def kick(ctx, member : discord.member, *, reason= None):#user to be kicked, reading the member as memeber object
    await member.kick(reason=reason)#kick is a method of member


@client.command()
async def ban(ctx, member : discord.member, *, reason= None):#user to be kicked, reading the member as memeber object, this mentions the member in the chat, asterisk cauze we gon type a whole sentence so it should take them all
    await member.ban(reason=reason)#ban is a method of member


client.run('')#add bot token

