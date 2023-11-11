import discord
import random 
from discord.ext import commands
import random
import os 
from googletrans import Translator
import datetime
import asyncio
from datetime import timedelta


intents = discord.Intents.all()


bot = commands.Bot(command_prefix=':', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def haveanidea(ctx):
    print(f"{bot.user}=fikri olan biri var.")

@bot.command()
async def kick(ctx, member: discord.Member,* ,sebep):
    await member.kick(reason = sebep)
    await ctx.send(f"**{member.mention}**kicked from this server, reason=**{sebep}**")

@bot.command()
async def ban(ctx, member: discord.Member,* ,sebep):
    await member.ban(reason = sebep)
    await ctx.send(f"**{member.mention}**banned from this server,reason= **{sebep}**")
@bot.command()
async def clear(ctx , amount=10000000):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send("Messages Deleted")

# Süre dönüştürücüsü
class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        try:
            # timedelta kullanarak süreyi dönüştür
            return timedelta(minutes=int(argument))
        except ValueError:
            raise commands.BadArgument('Geçersiz süre formatı. Örnek: 13m')

# Mute komutu
@bot.command(name='mute')
async def mute(ctx, member: discord.Member, duration: DurationConverter = DurationConverter()):
    # Kullanıcıyı susturma işlemi
    await member.edit(mute=True)

    # Zamanaşımı süresince beklemek için asyncio.sleep kullanın
    await asyncio.sleep(duration.total_seconds())

    # Zamanaşımı süresi bittikten sonra kullanıcıyı tekrar açma
    await member.edit(mute=False)

    # Komutu kullanan kişiye geri bildirim verme
    await ctx.send(f'{member.mention} kullanıcısı {duration} boyunca susturuldu.')
   
@bot.command()
async def stop(ctx):
    print("stop")
    await ctx.send(f"admin_local_host_stop_services")
    await ctx.send(f"Closing...")
    exit()

bot.run("BOTUN TOKENİ BURAYA")
