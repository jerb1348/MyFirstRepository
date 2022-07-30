import discord
import random
from discord.ext import commands
from random import randint

bot = commands.Bot(command_prefix='+')

pet = {
    'health': 100,
    'strength': 1,
    'defence': 1,
    'energy': 30,
    'hunger': 25,
    'soul': 0,
}


@bot.command('ТренироватьСилу')
async def train(ctx):
    pet['strength'] += 4
    pet['energy'] -= 2
    pet['hunger'] += 5
    await ctx.send('Ваш питомец прошел изнурительные тренировки по силе')
    await ctx.send(str(pet))
    randomm = random.randint(1, 4)
    if randomm == 4:
        await ctx.send('Ваш питомец усердно тренировался и смог улчшить свой боевой дух!')
        pet['soul'] += 10
        await ctx.send(str(pet))


@bot.command('Отдых')
async def sleep(ctx):
    pet['energy'] += 20
    pet['health'] += 5
    pet['hunger'] += 10
    await ctx.send('Ваш питомец прошел изнурительные тренировки по здоровью')
    await ctx.send(str(pet))


@bot.command('ТренироватьЗдоровье')
async def train(ctx):
    pet['energy'] -= 4
    pet['health'] += 15
    pet['hunger'] += 10
    await ctx.send('Ваш питомец прошел изнурительные тренировки по здоровью')
    await ctx.send(str(pet))


@bot.command('ТренироватьЗащиту')
async def train(ctx):
    pet['defence'] += 5
    pet['health'] += 5
    pet['hunger'] += 10
    await ctx.send('Ваш питомец прошел изнурительные тренировки по защите')
    await ctx.send(str(pet))


@bot.command('Покушать')
async def feed(ctx):
    pet['energy'] += 4
    pet['hunger'] -= 15
    await ctx.send('Ваш питомец хорошо покушал')
    await ctx.send(str(pet))
    if pet['hunger'] < 0 or pet['hunger'] == 0:
        await ctx.send('Ваш питомец не хочет больше еды')


@bot.command('Аттака!')
async def fight(ctx):
    enemy = {
        'health': randint(1, 100),
        'strength': randint(1, 100),
        'defence': randint(1, 100),
    }
    await ctx.send('Вы атакуете врага')
    while enemy['health'] >= 0 and pet['health'] >= 0:
        pet['health'] -= enemy['strength'] - pet['defence']
        enemy['health'] -= pet['strength'] - enemy['defence'] - pet['soul']
        await ctx.send('Ваш питомец: ' + str(pet))
        await ctx.send('Враг : ' + str(enemy))
    if enemy['health'] > pet['health']:
        await ctx.send('Вы проиграли')
    else:
        await ctx.send('Вы победили')


@bot.command('Комманды')
async def cmd(ctx):
    await ctx.send('Комманды')
    await ctx.send('ТренироватьСилу')
    await ctx.send('ТренироватьЗдоровье')
    await ctx.send('ТренироватьЗащиту')
    await ctx.send('Отдых')
    await ctx.send('Покушать')
    await ctx.send('Аттака!')


@bot.command('МойПитомецПлохой')
async def cmd(ctx):
    await ctx.send('https://tenor.com/view/aboba-gif-22062699')


bot.run("OTkzMDk2NDY5OTAzMDUyODUw.Gpnk6e.K4pR-3KD8yddI1_n-7xv2_m3LT51YgpzB906F8")
