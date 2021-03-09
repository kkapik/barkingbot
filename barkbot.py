#importation module
import discord
import time

from discord.ext import commands

#créer le bot
bot = commands.Bot(command_prefix='$')

#détecter quand bor est pret
@bot.event
async def on_ready():
    print("bot prêt")
    await bot.change_presence(status= discord.Status.idle, activity=discord.Game("Prêt à barker"))
  


#cmd bienvenue
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



#vérifier erreur
@bark_on.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Il manque un argument")








#donner le jeton pour connection
jeton = ""

#connection serveur
bot.run(jeton)


