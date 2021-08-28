import discord
import random
import json
import emoji
import os
import datetime
import asyncio
import pytz
from discord.ext.commands import has_permissions, MissingPermissions
from datetime import datetime
from discord.ext import commands
from discord.ext import tasks

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='#', intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
	activity = discord.Game(name="With My Feelings", type=3)
	await client.change_presence(status=discord.Status.online, activity=activity)
	print('Bot is up and running :)'.format(client))

@tasks.loop(seconds = 15)
async def myLoop():
	await client.wait_until_ready()
	activity = discord.Activity(type=discord.ActivityType.listening, name="Click On My Profile!")
	await client.change_presence(status=discord.Status.online,
	                             activity=activity)
	await asyncio.sleep(15)
	activity = discord.Game(name="With My Feelings", type=3)
	await client.change_presence(status=discord.Status.online,
	                             activity=activity)
	await asyncio.sleep(15)
myLoop.start()

@client.event
async def on_message(ctx, reason=None):
    prefixes = ["!","@","#","$","%","^","&","*","/","~"]  
    if ctx.content.startswith("prefix"):
      await ctx.channel.send("My Prefix Is: **#**")
    for prefix in prefixes:
        if ctx.content.startswith(prefix + "prefix"):
            await ctx.channel.send("My Prefix Is: **#**")
    await client.process_commands(ctx)

#The code below will send the info of the bot.
@client.command()
async def info(ctx):
    embed=discord.Embed(title="Decks Bot Info", url="https://runningute72.github.io/", 
    description="**Created by**: SomeoneRandom#0150 \nVersion 0.0.1", 
    color=discord.Color.orange())
    await ctx.send(embed=embed)

@client.command()
async def Info(ctx):
    embed=discord.Embed(title="Decks Bot Info", url="https://runningute72.github.io/", 
    description="**Created by**: SomeoneRandom#0150 \nVersion 0.0.1", 
    color=discord.Color.orange())
    await ctx.send(embed=embed)

#The code below will show the version.
@client.command()
async def version(ctx):
    embed=discord.Embed(title="Decks Bot Version", url="https://runningute72.github.io/", 
    description="**Version**: 0.0.1", 
    color=discord.Color.orange())
    await ctx.send(embed=embed)

@client.command()
async def Version(ctx):
    embed=discord.Embed(title="Decks Bot Version", url="https://runningute72.github.io/", 
    description="**Version**: 0.0.1", 
    color=discord.Color.orange())
    await ctx.send(embed=embed)

#The code below will show the creator of the bot.
@client.command()
async def creator(ctx):
    embed=discord.Embed(title="Decks Bot Creator", url="https://runningute72.github.io/", 
    description="**Creator**: SomeoneRandom#0150", 
    color=discord.Color.orange())
    await ctx.send(embed=embed)

@client.command()
async def Creator(ctx):
    embed=discord.Embed(title="Decks Bot Creator", url="https://runningute72.github.io/", 
    description="**Creator**: SomeoneRandom#0150", 
    color=discord.Color.orange())
    await ctx.send(embed=embed)

#The code below gives the support server.
@client.command()
async def support(ctx):
    embed=discord.Embed(title="Decks Bot Support", url="https://runningute72.github.io/", 
    description="**Support Server**: https://discord.gg/yCSVTh2h8M", 
    color=discord.Color.orange())
    await ctx.send(embed=embed)

#The code below gives the bot invite.
@client.command()
async def invite(ctx):
    embed=discord.Embed(title="Decks Bot Invite", url="", 
    description="**Bot Invite**: \n https://discord.com/api/oauth2/authorize?client_id=792991139686383646&permissions=8&scope=bot", 
    color=discord.Color.orange())
    await ctx.send(embed=embed)

@client.command()
async def Invite(ctx):
    embed=discord.Embed(title="Decks Bot Invite", url="", 
    description="**Bot Invite**: \n https://discord.com/api/oauth2/authorize?client_id=792991139686383646&permissions=8&scope=bot", 
    color=discord.Color.orange())
    await ctx.send(embed=embed)

#The code below sends images of decks
@client.command(pass_context=True)
async def deck(message):
	await message.channel.send(
	    'https://www.thespruce.com/thmb/g8LoI_ZW3-K5r37nXcRkYIn8JXc=/3000x2000/filters:fill(auto,1)/Woodendeck-GettyImages-912332782-2473b41993164927aa6605cf13f6cacf.jpg'
	)


@client.command(pass_context=True)
async def deck2(message):
	await message.channel.send(
	    'https://www.decks.com/media/2k3aa35z/15092620134433.jpg')


@client.command(pass_context=True)
async def hi(ctx):
  await ctx.send(f"Hi {ctx.author.mention}")

@client.command()
async def serverpfp(ctx):
  await ctx.send(f"{ctx.guild.icon_url}")

@client.command()
async def pfp(ctx, member:discord.Member):
  await ctx.send(f"{member.icon_url}")

#The code below will send rules
@client.command()
async def rules(ctx):
    embed=discord.Embed(title="Server Rules", url="", 
    description="Ask if you need anything clarified. \n \n  Minor Offenses: Warn ➝ 30 Min Mute ➝ Kick ➝ Soft Ban ➝ 1d Ban \n Moderate Offenses: 1 Hour Mute ➝ Soft ban ➝ 3d Ban ➝ Perm Ban \n Major Offenses: Perm Ban \n \n :yellow_circle: Minor :yellow_circle: \n :white_small_square: Profanity \n :white_small_square: Spamming Channels \n :white_small_square: Impersonation \n :white_small_square: Disrespectful to other players \n :white_small_square: Spam joining/leaving voice channels \n :white_small_square: Screaming into your mic \n :white_small_square: Voice Changers \n :white_small_square: Inappropriate Discord Name/Nickname \n :white_small_square: Misusing channels \n :white_small_square: Excessively tagging others \n \n :orange_circle: Moderate :orange_circle: \n :white_small_square: Misusing bots \n :white_small_square: Breaking rules without actually breaking them \n \n :red_circle: Major :red_circle: \n :white_small_square: Sending Misc. Links/Harmful/Porn Media \n :white_small_square: IRL Scamming \n :white_small_square: Punishment Evasion \n :white_small_square: Spam Or Major @‘ing Of People \n :white_small_square: Any Racism Or Discrimination Is NOT Tolerated. \n \n Racist, sexist etc jokes will be discussed on a case by case basis by the ENTIRE staff team.", 
    color=discord.Color.blue())
    await ctx.send(embed=embed)

#The code below sends the help message
@client.command(aliases=["Help"])
@commands.guild_only()
async def help(ctx):
    embed=discord.Embed(title="Decks Bot Help", url="", 
    description="Ban - Bans the user mentioned.\nUnban - **SOON TO COME** \n \nMute - **SOON TO COME!** \nUnmute - **SOON TO COME!** \n \nKick - Kicks the user mentioned from the server. \n \nClean/Purge - Deletes the amount of messages listed. \n \nInfo - Shows the info of the bot. \n \nVersion - Shows the version of the bot. \n \nCreator - Shows the creator of the bot. \n \nSupport - Gives you the support server invite. \n \nInvite - Gives you the bot invite. \n \nOther Custom Commands - Ask <@503641822141349888> for those commands/any help!", 
    color=discord.Color.blue())
    await ctx.message.delete()
    await ctx.author.send(embed=embed)
    await ctx.send(f'{ctx.author.mention}, You have gotten mail!', delete_after=10)


#The code below sends OKUP6
@client.command(pass_context=True)
async def aeiou(message):
	await message.channel.send(':ok::up::six:')
#The code below sends duck messages
@client.command(pass_context=True)
async def duck(message):
	await message.channel.send('<:Duck:776670146428796948>')
@client.command(pass_context=True)
async def Duck(message):
	await message.channel.send('<:Duck:776670146428796948>')
#The code below sends rainbow blob messages
@client.command(pass_context=True)
async def RAINBOWBUB(message):
	await message.channel.send('<a:RainbowBlob:870479595244249148>')
@client.command(pass_context=True)
async def rainbowbub(message):
	await message.channel.send('<a:RainbowBlob:870479595244249148>')
#The code below sends default emoji messages
@client.command(pass_context=True)
async def default(message):
	await message.channel.send('<a:Default:783589456509796363>')
@client.command(pass_context=True)
async def default5(message):
	await message.channel.send(
	    '<a:Default:783589456509796363><a:Default:783589456509796363><a:Default:783589456509796363><a:Default:783589456509796363><a:Default:783589456509796363>'
	)


#The code below cleans/purges messages
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
	await ctx.channel.purge(limit=limit+1)
	await ctx.send('Cleared By: {}'.format(ctx.author.mention), delete_after=2)
	await ctx.message.delete()

@clean.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send("You cannot do that!")
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def Clean(ctx, limit: int):
	await ctx.channel.purge(limit=limit+1)
	await ctx.send('Cleared By: {}'.format(ctx.author.mention), delete_after=2)
	await ctx.message.delete


@Clean.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send("You cannot do that!")
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx, limit: int):
	await ctx.channel.purge(limit=limit+1)
	await ctx.send('Cleared By: {}'.format(ctx.author.mention), delete_after=2)


@clean.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send("You cannot do that!")
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def Purge(ctx, limit: int):
	await ctx.channel.purge(limit=limit+1)
	await ctx.send('Cleared By: {}'.format(ctx.author.mention), delete_after=2)


@clean.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send("You cannot do that!")

#The code below kicks a user
@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
	await user.kick(reason=reason)
	kick = discord.Embed(
	    title=f"**Kicked** {user.name}!",
	    description=f"Reason: {reason}\nBy: {ctx.author.mention}")
	await ctx.message.delete()
	await ctx.channel.send(embed=kick)
	await user.send(embed=kick)

@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("Hey, {}! You cannot do that!".format(ctx.author.mention), delete_after=10)

#The code below bans a user
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
	await member.ban(reason=reason)

@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("Hey, {}! You cannot do that!".format(ctx.author.mention), delete_after=10)

@client.command()
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!", delete_after=5)

#The code below will mute a user
@client.command()
async def mute(ctx, member : discord.Member = None, *, reason=None):
    authorperms = ctx.author.permissions_in(ctx.channel)
    if authorperms.manage_roles:
        if member == None:
            await ctx.send("Please specify who you want to mute!")
        if member != None:
            embed = discord.Embed(
                title=f'{member} has been muted',
                description=f'{member.mention} has been muted',
                colour= discord.Colour.blurple()
            )
            embed.add_field(name='Reason :', value=f'{reason}', inline=True)
            embed.set_thumbnail(url='')

            embed.add_field(name='Muted by :', value=f'{ctx.author.mention}')
            await ctx.send(embed=embed)
            role = discord.utils.get(ctx.guild.roles, name='Muted')
            await member.add_roles(role)
            role1 = discord.utils.get(ctx.guild.roles, name='Members')
            await member.remove_roles(role1)
    else:
        if authorperms.manage_roles:
            pass
        else:
            await ctx.message.delete()
            await ctx.send(f"**{ctx.author.mention} you don't have the permissions to do that!**")

@client.command()
async def unmute(ctx, member : discord.Member = None, *, reason=None):
    authorperms = ctx.author.permissions_in(ctx.channel)
    if authorperms.manage_roles:
        if member == None:
            await ctx.send("Please specify who you want to unmute!")
        if member != None:
            embed = discord.Embed(
                title=f'{member} has been unmuted',
                description=f'{member.mention} has been unmuted',
                colour= discord.Colour.blurple()
            )
            embed.add_field(name='Reason :', value=f'{reason}', inline=True)
            embed.set_thumbnail(url='')

            embed.add_field(name='Muted by :', value=f'{ctx.author.mention}')
            await ctx.send(embed=embed)
            role = discord.utils.get(ctx.guild.roles, name='Muted')
            await member.remove_roles(role)
            role1 = discord.utils.get(ctx.guild.roles, name='Members')
            await member.add_roles(role1)
    else:
        if authorperms.manage_roles:
            pass
        else:
            await ctx.message.delete()
            await ctx.send(f"**{ctx.author.mention} you don't have the permissions to do that!**")

@client.command()
async def announce(ctx, *, reason):
    embed=discord.Embed(title="Announcement", url="", 
    description=f"{reason}",
    color=discord.Color.blue())
    await ctx.channel.send(embed=embed)
    await ctx.message.delete()

@client.command(pass_context=True)
async def serverslist(ctx):
    await ctx.channel.send("I'm In " + str(len(client.guilds)) + " Servers")

@client.command()
async def fakebump(ctx):
    embed=discord.Embed(title="DISBOARD: The Public Server List", url="https://disboard.org/", 
    description=f"{ctx.author.mention} \nBump done :thumbsup: \nCheck it on DISBOARD: https://disboard.org/",
    color=discord.Color.blue())
    embed.set_image(url="https://disboard.org/images/bot-command-image-bump.png")
    await ctx.channel.send(embed=embed)
    await ctx.message.delete()

@client.command()
async def fakebump2(ctx):
    embed=discord.Embed(title="DISBOARD: The Public Server List", url="https://disboard.org/", 
    description="bump done",
    color=discord.Color.blue())
    embed.set_image(url="https://disboard.org/images/bot-command-image-bump.png")
    await ctx.channel.send(embed=embed)
    await ctx.message.delete()

@client.command()
async def enlarge(ctx, emoji: discord.PartialEmoji = None):
    if not emoji:
        await ctx.send("You need to provide an emoji!")
    else:
        await ctx.send(emoji.url)

client.run('')
