#https://discordapp.com/api/oauth2/authorize?client_id=696961682014076992&permissions=8&scope=bot

from discord.ext import commands, tasks
import random
import os
import discord
import requests
import json
import string
import twitter
import datetime
import pathlib


def log( command, args, user , server ,failed = False ):
    with open(str(pathlib.Path(__file__).parent.absolute())+"/log_file.txt", "a+") as f:
        if failed:
            print('\n'+ str(datetime.datetime.now()) + '\n' + 'ran command ' +command + ' | by the user ' +str(user) +  ' | with the arguments: ' +str(args) + ' | on server: ' + str(server))
        else:
            print( '\n' + str(datetime.datetime.now()) + '\n' + 'failed to run command ' +command + ' | by the user ' +str(user) +  ' | with the arguments: ' +str(args) + ' | on server: ' + str(server))


tapi = twitter.Api(consumer_key='<ENTER RESPECTIVE API KEY>',
                  consumer_secret='<ENTER RESPECTIVE API KEY>',
                  access_token_key='<ENTER RESPECTIVE API KEY>',
                  access_token_secret='<ENTER RESPECTIVE API KEY>')

alphabet = string.digits + string.ascii_lowercase
def enc(n, base=36):
    out = []
    while n > 0:
        n, r = divmod(n, base)
        out.append(alphabet[r])
    return(''.join(reversed(out)))



client = commands.Bot(command_prefix = ">")

with open(str(pathlib.Path(__file__).parent.absolute())+'/whitelst.txt','r') as f:
    kill_blacklist = f.read().split(',')


@client.command()
async def die(ctx, amount=5):
    try:
        await ctx.channel.purge(limit = amount + 1)
        log('die',amount+1,ctx.author,ctx.message.guild)
    except:
        log('die',amount+1,ctx.author,ctx.message.guild,True)


@client.command()
async def meme(ctx):
    try:
        x = requests.get('https://meme-api.herokuapp.com/gimme').text
        p = json.loads(x)
        np = (p['url'])
        await ctx.message.channel.send(content = np)
        log('meme',['NONE'],ctx.author)
    except:
        log('meme',['NONE'],ctx.author,ctx.message.guild,True)

@client.command()
async def dank(ctx):
    try:
        x = requests.get('http://meme-api.herokuapp.com/gimme/dankmemes').text
        p = json.loads(x)
        np = (p['url'])
        await ctx.message.channel.send(content = np)
        log('meme',['NONE'],ctx.author)
    except:
        log('meme',['NONE'],ctx.author,ctx.message.guild,True)


@client.command()
async def killme(ctx,arg1):
    try:
        for i in range(int(arg1)):
            await ctx.author.send('die')
        log('killme',arg1,ctx.author,ctx.message.guild)
    except:
        log('killme',arg1,ctx.author,ctx.message.guild,True)


@client.command()
async def trump(ctx):
    try:
        statuses = tapi.GetUserTimeline('25073877')
        await ctx.message.channel.send('Straight from The King Of America, Donald Trump\'  Twitter!  :  \n \n " ' + statuses[random.randint(0, len(statuses)-1)].text.split('https')[0]  + ' "  \n 🇺🇸 🇺🇸 🇺🇸 🇺🇸 🇺🇸' )
        log('trump',['NONE'],ctx.author,ctx.message.guild)
    except:

        log('trump',['NONE'],ctx.author,ctx.message.guild,True)


@client.command()
async def cursed(ctx):
    try:
        with open(str(pathlib.Path(__file__).parent.absolute())+'/cursed.json') as jf:
            await ctx.message.channel.send(content = json.load(jf)[random.randint(0,17)])
        log('cursed',['NONE'],ctx.author,ctx.message.guild)
    except:
        log('cursed',['NONE'],ctx.author,ctx.message.guild,True)


@client.command()
async def victory(ctx):
    try:
        with open(str(pathlib.Path(__file__).parent.absolute())+'/victory.json') as jf:
            await ctx.message.channel.send(content = json.load(jf)[random.randint(0,10)])
        log('victory',['NONE'],ctx.author,ctx.message.guild)
    except:
        log('victory',['NONE'],ctx.author,ctx.message.guild,True)



@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason = None):
    try:
        await member.kick(reason = reason)
        log('kick',[member,reason],ctx.author,ctx.message.guild)
    except:
        log('kick',[member,reason],ctx.author,ctx.message.guild,True)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason = None):
    try:
        await member.ban(reason = reason)
        log('ban',[member,reason],ctx.author,ctx.message.guild)
    except:
        log('ban',[member,reason],ctx.author,ctx.message.guild,True)

@client.event
async def on_ready():
    print("bot is ready")
    await client.change_presence(activity=discord.Game(name=" withma balls"))

client.run("<ENTER RESPECTIVE API KEY>")
