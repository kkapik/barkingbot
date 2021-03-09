import discord
import time
#import keep_alive from keep_alive

from discord.ext import commands


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
#    print("Ready")
    await bot.change_presence(status= discord.Status.online, activity=discord.Game("Prêt à barker"))
  


@bot.command()
async def bark_on(ctx, member : discord.Member):
    pseudo = member.mention
    auteur = ctx.author.mention
    await ctx.send(f"{auteur} m'a demandé de bark sur {pseudo} :dog: Ouaf :dog:")
    print(f"{auteur} m'a demandé de bark sur {pseudo} :dog: Ouaf :dog:")
    await member.send(f":dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog:")
    time.sleep(0.5)
    await member.send(f":dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog:")
    time.sleep(0.5)
    await member.send(f":dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog:")
    time.sleep(0.5)
    await member.send(f":dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog:")
    time.sleep(0.5)
    await member.send(f":dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog:")
    time.sleep(0.5)
    await member.send(f":dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog:")
    time.sleep(0.5)
    await member.send(f":dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog:")
    time.sleep(0.5)
    await member.send(f":dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog:")
    time.sleep(0.5)
    await member.send(f":dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog:")
    time.sleep(0.5)
    await member.send(f":dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog: \n:dog: Ouaf Ouaf Ouaf :dog:")



@bark_on.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Il manque un argument")




token = "EnterYourTokenHere"

#keep_alive()
bot.run(token)


