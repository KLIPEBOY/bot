import discord
from discord.ext import commands

prefix = ('.')

bot = commands.Bot(command_prefix = (prefix)) # Создаем переменную bot используемую для всех наших взаимодействий с ботом


bot.remove_command('help') # Удаляем изначальную команду "help"


@bot.event # Объявление события
async def on_ready(): # Объявление асинхронной функции

    
    await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f'vanillacountry-project', url='https://www.youtube.com/watch?v=fQIanvUye4o')) # Статус бота (Для примера выбрал стриминг)
    # Cообщение/команда которая отображается в статусе у бота (https://prnt.sc/uog6r6), меняется с помощью: name=f'{prefix}help' (Пример: name=f'Hello world!') (https://prnt.sc/uog9hx)

# Пример команды с выводом результата через обычное сообщение:
# Ping
@bot.command(aliases = ['Ping', 'PING', 'pING', 'ping', 'Пинг', 'ПИНГ', 'пИНГ', 'пинг', 'Понг', 'ПОНГ', 'пОНГ', 'понг'])
#@bot.command - объявление команды | (aliases = ['Ping', 'PING' ...]) - Альтернативное название команды
async def __ping(ctx): # Объявление асинхронной функции __ping с возможностью публикации сообщения
    ping = bot.ws.latency # Получаем пинг клиента

    ping_emoji = '🟩🔳🔳🔳🔳' # Эмоция пинга, если он меньше 100ms

    if ping > 0.10000000000000000:
        ping_emoji = '🟧🟩🔳🔳🔳' # Эмоция пинга, если он больше 100ms

    if ping > 0.15000000000000000:
        ping_emoji = '🟥🟧🟩🔳🔳' # Эмоция пинга, если он больше 150ms

    if ping > 0.20000000000000000:
        ping_emoji = '🟥🟥🟧🟩🔳' # Эмоция пинга, если он больше 200ms

    if ping > 0.25000000000000000:
        ping_emoji = '🟥🟥🟥🟧🟩' # Эмоция пинга, если он больше 250ms

    if ping > 0.30000000000000000:
        ping_emoji = '🟥🟥🟥🟥🟧' # Эмоция пинга, если он больше 300ms

    if ping > 0.35000000000000000:
        ping_emoji = '🟥🟥🟥🟥🟥' # Эмоция пинга, если он больше 350ms

    message = await ctx.send('Пожалуйста, подождите. . .') # Переменная message с первоначальным сообщением
    await message.edit(content = f'Понг! {ping_emoji} `{ping * 1000:.0f}ms` :ping_pong:') # Редактирование первого сообщения на итоговое (На сам пинг)
    print(f'[Logs:utils] Пинг сервера был выведен | {prefix}ping') # Информация в консоль, что команда "ping" была использована
    print(f'[Logs:utils] На данный момент пинг == {ping * 1000:.0f}ms | {prefix}ping') # Вывод пинга в консоль
@bot.command()
async def очистить(ctx, amount=1000):
    await ctx.channel.purge(limit=amount) #очищаем
    print(f"[Logs:moderation] Пользователь [{ctx.author}]  очистил чат!")



@bot.command()
async def Донат(ctx):
  embed = discord.Embed(
    title="Наши привелегии :",
   description = f' Модер-500р Премиум-150р Вип-50р',colour = discord.Color.purple() )
  await ctx.author.send(embed=embed)

@bot.command()
async def Купить(ctx):
  embed = discord.Embed(
    title="Купить донат:",
   description = f'На карту 2202 2032 7781 9746',colour = discord.Color.purple() )
  await ctx.author.send(embed=embed)


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def maf(ctx):
    emb = discord.Embed(title=f'Донат ',
                        description='1️⃣-Модер-500р 2️⃣-Премиум-150р 3️⃣-Вип-50р',
                        colour=discord.Color.purple())

    message = await ctx.send(embed=emb) # Возвращаем сообщение после отправки
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
    await message.add_reaction('3️⃣')




bot.run('ODIyODk3NDIwNDY3NDM3NTk5.YFY88Q.GLUr0p-FvjkyN8GO2RFuaEyVqJY')
