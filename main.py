from asyncio.tasks import wait
import discord
from discord import embeds
from discord import emoji
from discord import message
from discord.ext import commands
from discord.utils import get,find
from datetime import date, datetime
import asyncio

intents = discord.Intents.all()
intents.members = True
intents.reactions = True
bot = commands.Bot(command_prefix="!")
emoji = "\N{THUMBS UP SIGN}"
available_commands = ["Tnx", "tnx", "thanks"]

with open("Token.txt", "r") as f:
    TOKEN = f.readline()

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


@bot.command(pass_context=True)
async def remind(ctx, *, message):
    global channel
    channel = ctx.channel
    split_message = message.split()
    time_to_remind = split_message[-1]
    what_to_remember = " ".join(split_message[:-1])
    e = discord.Embed(title="Remind", description=f"I'll remind you **{what_to_remember}** in **{time_to_remind}**", color=discord.Color.random())
    CURR_TIME = datetime.now()
    CURR_TIME = CURR_TIME.strftime("%d/%m/%y · %H:%M:%S")
    e.set_footer(text=f"Command recognized in {CURR_TIME} by {ctx.author.name}")
    message1 = await channel.send(embed=e)

    await message1.add_reaction(emoji)
    CURR_TIME_H = datetime.now().hour
    CURR_TIME_M = datetime.now().minute
    CURR_TIME_S = datetime.now().second
    time_to_remind = time_to_remind.split(":")
    time_to_remind_h = int(CURR_TIME_H) - int(time_to_remind[0])
    if time_to_remind_h < 0:
        time_to_remind_h = time_to_remind_h * (-1)
    else:
        pass
    time_to_remind_m = int(CURR_TIME_M) - int(time_to_remind[-1])
    if time_to_remind_m < 0:
        time_to_remind_m = time_to_remind_m *(-1)
    else:
        pass
    await asyncio.sleep((time_to_remind_h*3600) + (time_to_remind_m*60) - (CURR_TIME_S + 2))
    CURR_TIME = datetime.now()
    CURR_TIME = CURR_TIME.strftime("%d/%m/%y · %H:%M:%S")
    e_done = discord.Embed(title="Reminder", description=f"Hello {ctx.author.name},\n you told me to remind you to **{what_to_remember}**, So thats what I did.", color=discord.Color.random())
    e_done.set_footer(text=f"Command recognized in {CURR_TIME} by {ctx.author.name}")
    global message2
    message2 = await channel.send(embed=e_done)
    reaction = await message2.add_reaction(emoji)

@bot.command(name="Thanks")
async def Thanks(ctx):
    await ctx.channel.send("That's why I am here.")


bot.run(TOKEN)
