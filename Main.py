import os
from datetime import time, timezone, date
from dotenv import load_dotenv
load_dotenv()
import discord
from discord.ext import commands, tasks
from discord.ui import Button, View, Select
from discord.commands import Option
import asyncio
import random
from random import randint
import youtube_dl
from Classes import HelpSelectView, CreateBetModal
from Version import code_version
import sqlite3



# --------------------------------------------------------------------

secretbot = commands.Bot(intents=discord.Intents.all())
bot = discord.Bot(intents=discord.Intents.all())
voice = discord.VoiceClient


@bot.event
async def on_ready():
  bday_check.start()
  nday_check.start()
  allmemberset = {"GamingGuyLV#4075"}
  member_count = 0
  server_count = 0
  for guild in bot.guilds:
    server_count += 1
    for member in guild.members:
      if member not in allmemberset:
        allmemberset.add(f"{member}")
  x = 0
  for z in allmemberset:
    x += 1
    member_count += 1
  print(f"Logged in as {bot.user}")
  print(f"Bot ID: {bot.user.id}")
  print(f"Bot is operational and in {server_count} servers over {member_count} people!")
  print("---------------------------------------------------")
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{server_count} servers and {member_count} members."))


#################################################################################################################### COMMANDLINE

@bot.slash_command(guild_ids=[701802417129390153])
async def commandline(ctx):
  if ctx.author.id == 323516632880250890:
    await ctx.respond("Opened", ephemeral=True)
    print("Ko darit?")
    print("1 - Kick")
    print("2 - Ban")
    print("3 - Un-Ban")
    print("4 - Un-Time")
    print("5 - Give Role")
    print("6 - Remove Role")
    print("7 - Print invites")

    x = int(input())

    if x == 1: # Kick
      print("Ievadiet Nick#****")
      user = str(input())
      print("Ievadiet serveri")
      servername = str(input())

      if user != None:
        for guild in bot.guilds:
          guilds = str(guild)
          if servername in guilds:
            for member in guild.members:
              members = str(member)
              if user in members:
                await member.kick()
    
    if x == 2: # Ban
      print("Ievadiet Nick#****")
      user = str(input())

      if user != None:
        for guild in bot.guilds:
          for member in guild.members:
            members = str(member)
            if user in members:
              await member.ban()
    if x == 3: # Un-ban
      print("Ievadiet Nick#****")
      user = str(input())

      for guild in bot.guilds:
        bans = await guild.bans()
        for ban in bans:
          entry = ban.user
          entrys = str(entry)
          if user in entrys:
            await guild.unban(entry)

    if x == 4: # Un-time
      print("Ievadiet Nick#****")
      user = str(input())

      for guild in bot.guilds:
        for member in guild.members:
          members = str(member)
          if user in members:
            await member.remove_timeout()

    if x == 5: # Give role
      print("Ievadiet Nick#****")
      user = str(input())
      print("Ievadiet serveri")
      servername = str(input())

      for guild in bot.guilds:
        guilds = str(guild)
        if servername in guilds:
          for member in guild.members:
            members = str(member)
            if user in members:
              print("Member found")
              print("Input role name")
              giverole = str(input())
              for role in guild.roles:
                roles = str(role)
                if giverole in roles:
                  await member.add_roles(role)

    if x == 6: # Remove role
      print("Ievadiet Nick#****")
      user = str(input())
      print("Ievadiet serveri")
      servername = str(input())

      for guild in bot.guilds:
        guilds = str(guild)
        if servername in guilds:
          for member in guild.members:
            members = str(member)
            if user in members:
              print("Member found")
              print("Input role name")
              giverole = str(input())
              for role in guild.roles:
                roles = str(role)
                if giverole in roles:
                  await member.remove_roles(role)

    if x == 7: # Print invites
      print("Ievadiet Serveri")
      server = str(input())

      for guild in bot.guilds:
        guilds = str(guild)
        if server in guilds:
          invites = await guild.invites()
          for invite in invites:
            print(f"{invite}")

# --------------------------------------------------------------------------------------------Database

con = sqlite3.connect("Main.db")
cur = con.cursor()

# -------------------------------------------balance
cur.execute('''
  CREATE TABLE IF NOT EXISTS balances (
    servermemberid TEXT NOT NULL,
    balance REAL NOT NULL,
    membername TEXT NOT NULL,
    servername TEXT NOT NULL,
    PRIMARY KEY (servermemberid)
    )
''')

# ---------------------------------------bdays
cur.execute('''
  CREATE TABLE IF NOT EXISTS birthdays (
    servermemberid TEXT NOT NULL,
    membername TEXT NOT NULL,
    servername TEXT NOT NULL,
    birthday INT NOT NULL,
    birthmonth INT NOT NULL,
    age INT
    )
''')

#-------------------------------------------ndays
cur.execute('''
  CREATE TABLE IF NOT EXISTS namedays (
    servermemberid TEXT NOT NULL,
    membername TEXT NOT NULL,
    servername TEXT NOT NULL,
    nameday INT NOT NULL,
    namemonth INT NOT NULL,
    name TEXT
    )
''')

#-----------------------------------------activebets
cur.execute('''
  CREATE TABLE IF NOT EXISTS activebets (
    servermemberid TEXT NOT NULL,
    servername TEXT NOT NULL,
    creatorname TEXT NOT NULL,
    msgid TEXT,
    betid INT NOT NULL
    )
''')

#-------------------------------------------betting
cur.execute('''
  CREATE TABLE IF NOT EXISTS betters (
    servermemberid TEXT NOT NULL,
    servername TEXT NOT NULL,
    membername TEXT NOT NULL,
    betid INT NOT NULL,
    betoption INT NOT NULL,
    betamount REAL NOT NULL
    )
''')

#-----------------------------------------blacklist
cur.execute('''
  CREATE TABLE IF NOT EXISTS blacklist (
    servermemberid TEXT NOT NULL,
    servername TEXT NOT NULL,
    frases TEXT
    )
''')



# --------------------------------------------------------------------------------------------Server counter
@bot.event
async def on_guild_join(guild):
  allmemberset = {"GamingGuyLV#4075"}
  member_count = 0
  server_count = 0
  for guild in bot.guilds:
    server_count += 1
    for member in guild.members:
      if member not in allmemberset:
        allmemberset.add(f"{member}")
  x = 0
  for z in allmemberset:
    x += 1
    member_count += 1
  print(f"Added to guild - {guild}")
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{server_count} servers and {member_count} members."))

@bot.event
async def on_guild_remove(guild):
  allmemberset = {"GamingGuyLV#4075"}
  member_count = 0
  server_count = 0
  for guild in bot.guilds:
    server_count += 1
    for member in guild.members:
      if member not in allmemberset:
        allmemberset.add(f"{member}")
  x = 0
  for z in allmemberset:
    x += 1
    member_count += 1
  print(f"Removed from guild - {guild}")
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{server_count} servers and {member_count} members."))


#############################################################################################################
#############################################################################################################
# ---------------------------------------------------------------------------------------------Moderation commands
@bot.slash_command(description = "Clears the specified amount of messages.") # ------------------------------------------------------------------------Clear
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
  await ctx.respond("Deleting messages...")
  await asyncio.sleep(3)
  x = amount + 1
  for y in range(x):
      await ctx.channel.purge(limit=1)
      await asyncio.sleep(0.1)
  
  embed = discord.Embed(
  colour = discord.Colour.blurple(),
  )
  embed.add_field(name="Clear", value=f"{amount} messages cleared!")
  embed.set_footer(text=f"Geary - executed by @{ctx.author.display_name}")

  await ctx.send(embed=embed)

@bot.slash_command(description = "Bans specified member.") # ------------------------------------------------------------------------Ban
@commands.has_permissions(ban_members=True)
async def ban(
  ctx: discord.ApplicationContext,
  member: discord.Member,
  reason: Option(str, "Enter the reason.", default="No reason given.")
):
  await member.ban(reason=reason)

  embed = discord.Embed(
  colour = discord.Colour.red(),
  )
  embed.add_field(name="Ban", value=f"{member.mention} has been banned for {reason}")
  embed.set_footer(text=f"Code version - {code_version}")

  await ctx.respond(embed=embed)

@bot.slash_command(description = "Unbans specified member.") # -------------------------------------------------------------------------Unban
@commands.has_permissions(ban_members=True)
async def unban(
  ctx: discord.ApplicationContext,
  member: discord.Member
):

  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      embed = discord.Embed(
      colour = discord.Colour.green(),
      )
      embed.add_field(name="Un-ban", value=f"@{user.name}#{user.discriminator} has been unbanned")
      embed.set_footer(text=f"Code version - {code_version}")

      await ctx.respond(embed=embed)

@bot.slash_command(description = "Prints out banned members.") # ---------------------------------------------------------------------------Banlist
@commands.has_permissions(ban_members=False)
async def banlist(
  ctx: discord.ApplicationContext,
  amount: Option(int, "The amount to print out.", min_value=1, max_value=1000, default=10)
):
  x = 0
  embed = discord.Embed(
  colour = discord.Colour.red(),
  )
  embed.add_field(name="Banlist", value="Fetching banned accounts...")
  await ctx.respond(embed=embed)
  await asyncio.sleep(1.5)
  bans = await ctx.guild.bans()
  for ban in bans:
    embed = discord.Embed(
    colour = discord.Colour.red(),
    )
    embed.add_field(name="Banlist", value=f"{ban.user} , reason={ban.reason}")
    await ctx.send(embed=embed)
    x += 1
    await asyncio.sleep(1)
    if x == amount:
      break
  embed = discord.Embed(
  colour = discord.Colour.red(),
  )
  embed.add_field(name="Banlist", value=f"{x} ban entries were printed out.")
  embed.set_footer(text=f"Geary - executed by @{ctx.author.display_name}")
  await ctx.send(embed=embed)
      


@bot.slash_command(description = "Kicks specified member.") # -----------------------------------------------------------------------------Kick
@commands.has_permissions(kick_members=True)
async def kick(
  ctx: discord.ApplicationContext,
  member: discord.Member,
  reason: Option(str, "Enter the reason.", default="No reason given.")
):

  await member.kick(reason=reason)

  embed = discord.Embed(
    colour = discord.Colour.red(),
  )
  embed.add_field(name="Kick", value=f"{member.mention} was kicked for {reason}")
  embed.set_footer(text=f"Code version - {code_version}")

  await ctx.respond(embed=embed)


@bot.slash_command(description = "Blacklists a frase.") # ------------------------------------------------------------------------Blacklist
@commands.has_permissions(manage_messages=True)
async def blacklist(
  ctx: discord.ApplicationContext,
  frase: Option(str, "Enter the frase you want blacklisted.", required = True)
):

  
  return

#######################################################################################################################
# ----------------------------------------------------------------------------------------------------Music commands

youtube_dl.utils.bug_reports_message = lambda: ""


ytdl_format_options = {
  "format": "bestaudio/best",
  "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
  "restrictfilenames": True,
  "noplaylist": True,
  "nocheckcertificate": True,
  "ignoreerrors": False,
  "logtostderr": False,
  "quiet": True,
  "no_warnings": True,
  "default_search": "auto",
  "source_address": "0.0.0.0",  # Bind to ipv4 since ipv6 addresses cause issues at certain times
}

ffmpeg_options = {"options": "-vn"}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
  def __init__(self, source, *, data, volume=0.5):
      super().__init__(source, volume)

      self.data = data

      self.title = data.get("title")
      self.url = data.get("url")

  @classmethod
  async def from_url(cls, url, *, loop=None, stream=False):
      loop = loop or asyncio.get_event_loop()
      data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

      if "entries" in data:
          # Takes the first item from a playlist
          data = data["entries"][0]

      filename = data["url"] if stream else ytdl.prepare_filename(data)
      return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)



@bot.slash_command(description = "Connects bot to your voice channel.")
async def connect(ctx: discord.ApplicationContext, self): # ----------------------------------------------------------------------------Connect
  if ctx.author.voice is None:
    await ctx.respond("You are not in a voice channel.", ephemeral = True)

  elif ctx.voice_client is None:
    channel = ctx.author.voice.channel
    await discord.VoiceChannel.connect(channel)
    await ctx.respond("Connected.", ephemeral = True)

  elif ctx.voice_client is not None:
    channel = ctx.author.voice.channel
    await ctx.voice_client.move_to(channel)
    await ctx.respond("Moved to your channel.", ephemeral = True)

@bot.slash_command(description = "Disconnects bot to your voice channel.")
async def disconnect(ctx): # -----------------------------------------------------------------------Disconnect
  if ctx.voice_client is None:
    await ctx.respond("I am not in a channel right now.", ephemeral = True)
  elif ctx.voice_client is not None:
    await ctx.voice_client.disconnect()
    await ctx.respond("Disconnected.", ephemeral = True)

@bot.slash_command(description = "Plays audio from the entered youtube URL.")
async def plays(
  self,
  ctx,
  *,
  url: Option(str, "Enter the URL/Link.", default=None)
): # -------------------------------------------------------------------------------------------------Play
  async with ctx.typing():
    player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
    ctx.voice_client.play(player, after=lambda e: print(f"Player error: {e}") if e else None)

  await ctx.respond(f"Now playing: {player.title}")


@bot.slash_command(description = "Pauses playback.")
async def pause(ctx):
  return

@bot.slash_command(description = "Resumes playback.")
async def resume(ctx):
  return

@bot.slash_command()
async def skip(ctx):
  return

@bot.slash_command()
async def loopsong(ctx):
  return

@bot.slash_command()
async def loopqueue(ctx):
  return

@bot.slash_command()
async def current(ctx):
  return

###################################################################################################################
# ----------------------------------------------------------------------------------------------------Fun commands



@bot.slash_command(description = "Insults the mentioned member.") # --------------------------------------------------------Insult
async def insult(ctx, member : discord.Member):
  f = open("insults.txt", "r")
  insults = f.readlines()
  insult = random.choice(insults)
  prev = open("previousinsult.txt", "r")
  previous = prev.readline()
  if previous == insult:
    insult = random.choice(insults)
  await ctx.respond(f"{member.mention}, {insult}")
  prev = open("previousinsult.txt", "w")
  prev.write(f"{insult}")
  prev.close()
  f.close()

@bot.slash_command(description = "Add an insult to the list.") # -------------------------------------------------------------Add insult
async def addinsult(ctx, insult):
  f = open("insults.txt", "a")
  f.write(f"\n{insult}")
  f.close()
  embed = discord.Embed(
  colour = discord.Colour.nitro_pink(),
  )
  embed.add_field(name="Added insult", value=f"{insult}")
  embed.set_footer(text=f"Code version - {code_version}")
  await ctx.respond(embed=embed, ephemeral=True)

@bot.slash_command() # --------------------------------------------------------------------------------------------------------Insults
async def insults(ctx):
  f = open("insults.txt", "r")
  insults = f.readlines()
  await ctx.respond("Fetching insults...")
  await asyncio.sleep(1)
  x = 0
  for insult in insults:
    x += 1
    embed = discord.Embed(
    colour = discord.Colour.nitro_pink(),
    )
    embed.add_field(name="Insult", value=f"{insult}")
    await ctx.send(embed=embed)
    await asyncio.sleep(1)
  f.close()
  embed = discord.Embed(
  colour = discord.Colour.nitro_pink(),
  )
  embed.add_field(name="Insults", value=f"{x} amount of insults were printed out.")
  await ctx.send(embed=embed)

@bot.slash_command(description = "UwU-sifies your message :P") # -----------------------------------------------------------Uwusify
async def uwusify(ctx, msg):
  text = msg.replace('r', r'w').replace('l', r'w')
  await ctx.respond(text)

@bot.slash_command(description = "Flips a coin.") # -------------------------------------------------------------------------------CoinFlip
async def coinflip(ctx):
  flip = randint(1,2)
  if flip == 1:
    embed = discord.Embed(
    colour = discord.Colour.gold(),
    )
    embed.add_field(name="CoinFlip", value=f"It's heads!")
    embed.set_footer(text=f"Code version - {code_version}")

    await ctx.respond(embed=embed)
  if flip == 2:
    embed = discord.Embed(
    colour = discord.Colour.gold(),
    )
    embed.add_field(name="CoinFlip", value=f"It's tails!")
    embed.set_footer(text=f"Code version - {code_version}")

    await ctx.respond(embed=embed)


@bot.slash_command(description = "Never gonna give you up! Never gonna let you down!") # -------------------------------------------------------------------------------Rick
async def rick(ctx):

  embed = discord.Embed(
    colour = discord.Colour.dark_gold()
  )

  embed.set_author(name='Click Me!', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
  embed.set_footer(text=f"Code version - {code_version}")

  await ctx.respond(embed=embed)

@bot.slash_command(description = "Create an embed with the Title having an URL embeded into it.") # -------------------------------------------------------------------------------HyperLinker
async def hyper(
  ctx: discord.ApplicationContext,
  title: Option(str, "Enter the title."),
  link: Option(str, "Enter the URL link.")
):

  embed = discord.Embed(
    colour = discord.Colour.dark_gold()
  )

  embed.set_author(name=f'{title}', url=f'{link}')
  embed.set_footer(text=f"Code version - {code_version}")

  await ctx.respond(embed=embed)

@bot.slash_command(description = "Play a game ob blackjack!")
async def blackjack(ctx, bet: float):
  return

######################################################################################################## Nameday/Birthday checker
######################################################################################################## 

@tasks.loop(time=time(12,0, tzinfo=timezone.utc))
async def bday_check():
  for guild in bot.guilds:
    guild = str(guild)
  
    for server in cur.execute('''SELECT servername FROM birthdays ORDER BY servername'''):
      server = str(server)
     
      if guild in server:
  
        for member in cur.execute('''SELECT membername FROM birthdays WHERE servername=?''',(guild,)):

          member = str(member)
          member = member.replace("'"," ")
          member = member.replace("("," ")
          member = member.replace(")"," ")
          member = member.replace(","," ")
          member = member.strip()

          cur.execute('''SELECT birthday FROM birthdays WHERE membername=?''', (str(member),))
          days = cur.fetchone()
          for d in days:
            day = int(d)

          cur.execute('''SELECT birthmonth FROM birthdays WHERE membername=?''', (str(member),))
          months = cur.fetchone()
          for m in months:
            month = int(m)

          cur.execute('''SELECT age FROM birthdays WHERE membername=?''', (str(member),))
          ages = cur.fetchone()
          for a in ages:
            if a != None:
              age = int(a)
            else:
              age = 0

          day = int(day)
          month = int(month)
          age = int(age)
          if day < 10:
              day = str(day)
              day = "0" + day

          if month < 10:
            month = str(month)
            month = "0" + month

          day = str(day)
          month = str(month)

          birthday = month + "-" + day

          today = str(date.today())
          if birthday in today:
            if age == 0:
              channel = discord.utils.get(bot.get_all_channels(), guild__name=f"{guild}", name="🧁anniversaries🧁")

              embed = discord.Embed(
                colour = discord.Colour.gold(),
              )
              embed.add_field(name="🥳Birthday!!!🥂", value=f"🧁Let's wish {member} a happy birthday!🧁")
              embed.set_footer(text=f"Code version - {code_version}")

              await channel.send(embed=embed)
            else:
              age += 1

              cur.execute(f'''UPDATE birthdays SET age={age} WHERE membername=? AND servername=?''', (member, guild))
              con.commit()
              channel = discord.utils.get(bot.get_all_channels(), guild__name=f"{guild}", name="🧁anniversaries🧁")

              embed = discord.Embed(
                colour = discord.Colour.gold(),
              )
              embed.set_author(name="🥳Birthday!!!🥂")
              embed.add_field(name=f"🧁Let's wish {member} a happy birthday!🧁", value=f"**🎂He/She is turning {age} today!🎂**")
              embed.set_footer(text=f"Code version - {code_version}")

              await channel.send(embed=embed)

@bday_check.before_loop
async def before_my_task():
  await bot.wait_until_ready()
  print("Birthday Task Started")

@tasks.loop(time=time(12,0, tzinfo=timezone.utc))
async def nday_check():
  for guild in bot.guilds:
    guild = str(guild)
  
    for server in cur.execute('''SELECT servername FROM namedays ORDER BY servername'''):
      server = str(server)
     
      if guild in server:
  
        for member in cur.execute('''SELECT membername FROM namedays WHERE servername=?''',(guild,)):

          member = str(member)
          member = member.replace("'"," ")
          member = member.replace("("," ")
          member = member.replace(")"," ")
          member = member.replace(","," ")
          member = member.strip()

          cur.execute('''SELECT nameday FROM namedays WHERE membername=?''', (str(member),))
          days = cur.fetchone()
          for d in days:
            day = int(d)

          cur.execute('''SELECT namemonth FROM namedays WHERE membername=?''', (str(member),))
          months = cur.fetchone()
          for m in months:
            month = int(m)

          cur.execute('''SELECT name FROM namedays WHERE membername=?''', (str(member),))
          names = cur.fetchone()
          for n in names:
            if n != None:
              name = str(n)
              name = name.replace("'"," ")
              name = name.replace("("," ")
              name = name.replace(")"," ")
              name = name.replace(","," ")
              name = name.strip()
            else:
              name = 0
              name = int(name)

          day = int(day)
          month = int(month)
          
          if day < 10:
              day = str(day)
              day = "0" + day

          if month < 10:
            month = str(month)
            month = "0" + month

          day = str(day)
          month = str(month)

          nameday = month + "-" + day

          today = str(date.today())
          if nameday in today:
            if name == 0:
              channel = discord.utils.get(bot.get_all_channels(), guild__name=f"{guild}", name="🧁anniversaries🧁")

              embed = discord.Embed(
                colour = discord.Colour.gold(),
              )
              embed.add_field(name="🥳Nameday!!!🥂", value=f"🧁Let's wish {member} a happy nameday!🧁")
              embed.set_footer(text=f"Code version - {code_version}")

              await channel.send(embed=embed)
            else:
              channel = discord.utils.get(bot.get_all_channels(), guild__name=f"{guild}", name="🧁anniversaries🧁")

              embed = discord.Embed(
                colour = discord.Colour.gold(),
              )
              embed.set_author(name="🥳Nameday!!!🥂")
              embed.add_field(name=f"🧁Let's wish {member} a happy nameday!🧁", value=f"**🎂His/Her name is {name}!🎂**")
              embed.set_footer(text=f"Code version - {code_version}")

              await channel.send(embed=embed)

@nday_check.before_loop
async def before_my_task():
  await bot.wait_until_ready()
  print("Nameday Task Started")

        

########################################################################################################

@bot.slash_command(description = "Add your birthday to the database! The whole server will know when it comes!") # ----------------------------AddBirthday
async def addbday(
  ctx: discord.ApplicationContext,
  day: Option(int, "Enter the day.", required = True),
  month: Option(int, "Enter the month.", required = True),
  age: Option(int, "Enter your age. (optional)", required = False)
):

  membername = str(ctx.author)
  servername = str(ctx.guild)
  gid = str(ctx.guild.id)
  mid = str(ctx.author.id)
  gmid = str(gid+mid)


  if day < 10:
    day = str(day)
    day = "0" + day
  if month < 10:
    month = str(month)
    month = "0" + month

  birthday = str(str(day) + "/" + str(month))

  cur.execute(f'''SELECT servermemberid FROM birthdays WHERE servermemberid=?''', (gmid,))
  result = cur.fetchone()

  if result:
    
    embed = discord.Embed(
      colour = discord.Colour.dark_red()
    )

    embed.add_field(name="Add Birthday", value=f"You already have a birthday set!")
    embed.set_footer(text=f"Code version - {code_version}")

    await ctx.respond(embed=embed)

  else:

    if age != None:

      cur.execute('''INSERT INTO birthdays (servermemberid, membername, servername, birthday, birthmonth, age) VALUES (?,?,?,?,?,?)''', (gmid, membername, servername, int(day), int(month), age))
      con.commit()

      embed = discord.Embed(
        colour = discord.Colour.green()
      )

      embed.add_field(name="Add Birthday", value=f"Your birthday has been added! Day/Month: {birthday}, age: {age}. We'll be waiting :D")
      embed.set_footer(text=f"Code version - {code_version}")

      await ctx.respond(embed=embed, ephemeral=True)
    
    else:

      cur.execute('''INSERT INTO birthdays (servermemberid, membername, servername, birthday, birthmonth) VALUES (?,?,?,?,?)''', (gmid, membername, servername, int(day), int(month)))
      con.commit()

      embed = discord.Embed(
        colour = discord.Colour.green()
      )

      embed.add_field(name="Add Birthday", value=f"Your birthday has been added! Day/Month: {birthday}. We'll be waiting :D")
      embed.set_footer(text=f"Code version - {code_version}")

      await ctx.respond(embed=embed, ephemeral=True)

@bot.slash_command(description = "Add your nameday to the database! The whole server will know when it comes!") # ----------------------------AddNameday
async def addnday(
  ctx: discord.ApplicationContext,
  day: Option(int, "Enter the day.", required = True),
  month: Option(int, "Enter the month.", required = True),
  name: Option(str, "Enter your name. (optional)", required = False)
):
  membername = str(ctx.author)
  servername = str(ctx.guild)
  gid = str(ctx.guild.id)
  mid = str(ctx.author.id)
  gmid = str(gid+mid)

  if day < 10:
    day = str(day)
    day = "0" + day
  if month < 10:
    month = str(month)
    month = "0" + month

  nameday = str(str(day) + "/" + str(month))

  cur.execute(f'''SELECT servermemberid FROM namedays WHERE servermemberid=?''', (gmid,))
  result = cur.fetchone()

  if result:
    
    embed = discord.Embed(
      colour = discord.Colour.dark_red()
    )

    embed.add_field(name="Add Nameday", value=f"You already have a nameday set!")
    embed.set_footer(text=f"Code version - {code_version}")

    await ctx.respond(embed=embed)

  else:

    if name != None:

      cur.execute('''INSERT INTO namedays (servermemberid, membername, servername, nameday, namemonth, name) VALUES (?,?,?,?,?,?)''', (gmid, membername, servername, int(day), int(month), name))
      con.commit()

      embed = discord.Embed(
        colour = discord.Colour.green()
      )

      embed.add_field(name="Add Nameday", value=f"Your nameday has been added! Day/Month: {nameday}, name: {name}. We'll be waiting :D")
      embed.set_footer(text=f"Code version - {code_version}")

      await ctx.respond(embed=embed, ephemeral=True)
    
    else:

      cur.execute('''INSERT INTO namedays (servermemberid, membername, servername, nameday, namemonth) VALUES (?,?,?,?,?)''', (gmid, membername, servername, int(day), int(month)))
      con.commit()

      embed = discord.Embed(
        colour = discord.Colour.green()
      )

      embed.add_field(name="Add Nameday", value=f"Your nameday has been added! Day/Month: {nameday}. We'll be waiting :D")
      embed.set_footer(text=f"Code version - {code_version}")

      await ctx.respond(embed=embed, ephemeral=True)

@bot.slash_command(description = "Remove your birthday from this server.") # -----------------------------------------------------------Remove bday
async def rmbday(ctx: discord.ApplicationContext):
  gid = str(ctx.guild.id)
  mid = str(ctx.author.id)
  gmid = str(gid+mid)
  cur.execute('''SELECT servermemberid FROM birthdays WHERE servermemberid=?''', (gmid,))
  result = cur.fetchone()

  if result:
    cur.execute('''DELETE FROM birthdays WHERE servermemberid=?''', (gmid,))
    con.commit()

    embed = discord.Embed(
      colour = discord.Colour.green()
    )

    embed.add_field(name="Remove Birthday", value=f"Your birthday has been removed!")
    embed.set_footer(text=f"Code version - {code_version}")

    await ctx.respond(embed=embed, ephemeral=True)
  
  else:
    embed = discord.Embed(
      colour = discord.Colour.dark_red()
    )

    embed.add_field(name="Remove Birthday", value=f"Could not find your birthday for this server.")
    embed.set_footer(text=f"Code version - {code_version}")

    await ctx.respond(embed=embed, ephemeral=True)

@bot.slash_command(description = "Remove your nameday from this server.") # ------------------------------------------------------------------------------------------Remove nameday
async def rmnday(ctx: discord.ApplicationContext):
  gid = str(ctx.guild.id)
  mid = str(ctx.author.id)
  gmid = str(gid+mid)
  cur.execute('''SELECT servermemberid FROM namedays WHERE servermemberid=?''', (gmid,))
  result = cur.fetchone()

  if result:
    cur.execute('''DELETE FROM namedays WHERE servermemberid=?''', (gmid,))
    con.commit()

    embed = discord.Embed(
      colour = discord.Colour.green()
    )

    embed.add_field(name="Remove Nameday", value=f"Your nameday has been removed!")
    embed.set_footer(text=f"Code version - {code_version}")

    await ctx.respond(embed=embed, ephemeral=True)
  
  else:
    embed = discord.Embed(
      colour = discord.Colour.dark_red()
    )

    embed.add_field(name="Remove Nameday", value=f"Could not find your nameday for this server.")
    embed.set_footer(text=f"Code version - {code_version}")

    await ctx.respond(embed=embed, ephemeral=True)

#################################################################################################################################
# -----------------------------------------------------------------------------------------------------Betting/Tournament commands


@bot.slash_command(description = "Opens an account for you in the current server.") # ----------------------------------------------------------------------------------------Register
async def register(ctx):
  gid = str(ctx.guild.id)
  mid = str(ctx.author.id)
  gmid = str(gid+mid)

  cur.execute(f'''SELECT servermemberid FROM balances WHERE servermemberid=?''', (gmid,))
  result = cur.fetchone()

  if result:
    embed = discord.Embed(
    colour = discord.Colour.brand_red(),
    )
    embed.add_field(name="Registration", value=f"You already have an account in this server.")
    embed.set_footer(text=f"Code version - {code_version}")
    await ctx.respond(embed=embed)
  else:
    servername = str(ctx.guild)
    membername = str(ctx.author)

    cur.execute('''INSERT INTO balances (servermemberid, balance, membername, servername) VALUES (?,100,?,?)''', (gmid, membername, servername))
    con.commit()

    embed = discord.Embed(
    colour = discord.Colour.green(),
    )
    embed.add_field(name="Registration", value=f"Your account has been opened. Have a great day!")
    embed.set_footer(text=f"Code version - {code_version}")
    await ctx.respond(embed=embed)

@bot.slash_command(description = "Donate balance to a member.") # -------------------------------------------------------------------------------------------Donate
@commands.has_role("Dealer")
async def donate(ctx, member : discord.Member, amount: float):
  gid = str(ctx.guild.id)
  mid = str(member.id)
  gmid = str(gid+mid)

  cur.execute('''SELECT balance FROM balances WHERE servermemberid=?''', (gmid,))
  x = cur.fetchone()
  for bal in x:
    balance = float(bal)

  newbalance = balance + amount
  
  embed = discord.Embed(
  colour = discord.Colour.dark_gold(),
  )
  embed.set_author(name=f"Dealer Donates - {amount}")
  embed.add_field(name="Previous balance", value=f"{member.display_name} previous balance was {balance} .")
  embed.add_field(name="New balance", value=f"{member.display_name} new balance is {newbalance} .", inline=False)
  embed.set_footer(text=f"Code version - {code_version}")
  await ctx.respond(embed=embed)

  cur.execute(f'''UPDATE balances SET balance = {newbalance} WHERE servermemberid=?''', (gmid,))
  con.commit()

@bot.slash_command(description = "Displays betting balance only from this server.") # -----------------------------------------------------------------------------------------Balance
async def balance(ctx, member : Option(discord.Member, required=False, default="")):
  gid = str(ctx.guild.id)
  if member == "":
    mid = str(ctx.author.id)
  else:
    mid = str(member.id)
  gmid = str(gid+mid)
  
  cur.execute('''SELECT balance FROM balances WHERE servermemberid=?''', (gmid,))
  x = cur.fetchone()
  for bal in x:
    balance = float(bal)
    balance = round(balance, 2)
  
  if member == "":
    embed = discord.Embed(
    colour = discord.Colour.dark_blue(),
    )
    embed.add_field(name="Balance", value=f"Your balance is: {balance}")
    embed.set_footer(text=f"Code version - {code_version}")
    await ctx.respond(embed=embed)
  else:
    embed = discord.Embed(
    colour = discord.Colour.dark_blue(),
    )
    embed.add_field(name="Balance", value=f"{member.display_name} balance is: {balance}")
    embed.set_footer(text=f"Code version - {code_version}")
    await ctx.respond(embed=embed)

@bot.slash_command(description = "Lets you to give your money to someone else.") # --------------------------------------------------------------------------------------Give
async def give(ctx, member : discord.Member, amount : float):
  gid = str(ctx.guild.id)
  amid = str(ctx.author.id)
  mid = str(member.id)
  gamid = str(gid+amid)
  gmid = str(gid+mid)

  cur.execute('''SELECT balance FROM balances WHERE servermemberid=?''', (gamid,))
  x = cur.fetchone()
  for bal in x:
    authorbalanceold = float(bal)
    authorbalanceold = round(authorbalanceold, 2)

  cur.execute('''SELECT balance FROM balances WHERE servermemberid=?''', (gmid,))
  x = cur.fetchone()
  for bal in x:
    memberbalanceold = float(bal)
    memberbalanceold = round(memberbalanceold, 2)

  authorbalancenew = authorbalanceold - amount
  memberbalancenew = memberbalanceold + amount

  authorbalancenew = round(authorbalancenew, 2)
  memberbalancenew = round(memberbalancenew, 2)

  if authorbalancenew < 0:
    embed = discord.Embed(
    colour = discord.Colour.brand_red(),
    )
    embed.set_author(name=f"You do not have enough funds in your account.")
    embed.set_footer(text=f"Code version - {code_version}")
    await ctx.respond(embed=embed)

  elif amount <= 0:
    embed = discord.Embed(
    colour = discord.Colour.brand_red(),
    )
    embed.set_author(name=f"You cannot give null or negative funds.")
    embed.set_footer(text=f"Code version - {code_version}")
    await ctx.respond(embed=embed)

  elif member == ctx.author:
    embed = discord.Embed(
    colour = discord.Colour.brand_red(),
    )
    embed.set_author(name=f"You cannot give funds to yourself.")
    embed.set_footer(text=f"Code version - {code_version}")
    await ctx.respond(embed=embed)

  else:
    memberbalancenew = float(round(memberbalancenew, 2))
    authorbalancenew = float(round(authorbalancenew, 2))

    cur.execute(f'''UPDATE balances SET balance = {authorbalancenew} WHERE servermemberid=?''', (gamid,))
    cur.execute(f'''UPDATE balances SET balance = {memberbalancenew} WHERE servermemberid=?''', (gmid,))
    con.commit()

    embed = discord.Embed(
    colour = discord.Colour.dark_blue(),
    )
    embed.set_author(name=f"Transaction of '{amount}' between {ctx.author.display_name} and {member.display_name} was successful.")
    embed.add_field(name="Balance", value=f"{ctx.author.display_name} old balance was: '{authorbalanceold}', and new balance is: '{authorbalancenew}' .")
    embed.add_field(name="Balance", value=f"{member.display_name} old balance was: '{memberbalanceold}', and new balance is: '{memberbalancenew}' .")
    embed.set_footer(text=f"Code version - {code_version}")
    await ctx.respond(embed=embed)


@bot.slash_command(description = "Lets CEODealer to reset funds of the specified member to a specified amount.") # ----------------------------------------------------------------------ResetBal
@commands.has_role("CEODealer")
async def resetbal(ctx, member : discord.Member, amount : float):
  await ctx.defer()
  gid = str(ctx.guild.id)
  mid = str(member.id)
  gmid = str(gid+mid)

  if amount <= 0:
    embed = discord.Embed(
    colour = discord.Colour.brand_red(),
    )
    embed.set_author(name=f"You cannot set null or negative funds.")
    embed.set_footer(text=f"Code version - {code_version}")
    await ctx.respond(embed=embed)
  else:

    de = await ctx.send("Are you sure? You have 10 sec to respond Y/N .")

    msg = await bot.wait_for("message", timeout=10)
    if msg.author == ctx.author and "Y" in msg.content:
      cur.execute(f'''UPDATE balances SET balance = {amount} WHERE servermemberid=?''', (gmid,))
      con.commit()
      embed = discord.Embed(
      colour = discord.Colour.brand_green(),
      )
      embed.set_author(name=f"Reset of {member.display_name} balance was successful, new balance is: {amount}")
      embed.set_footer(text=f"Code version - {code_version}")
      await ctx.respond(embed=embed)
      await de.delete()
      await msg.delete()

    elif msg.author == ctx.author and "N" in msg.content:
      embed = discord.Embed(
      colour = discord.Colour.dark_red(),
      )
      embed.set_author(name=f"Cancelling operation.")
      embed.set_footer(text=f"Code version - {code_version}")
      await ctx.respond(embed=embed)
      await de.delete()
      await msg.delete()

    else:
      embed = discord.Embed(
      colour = discord.Colour.brand_red(),
      )
      embed.set_author(name=f"{msg.author} replied, cancelling operation.")
      embed.set_footer(text=f"Code version - {code_version}")
      await ctx.respond(embed=embed)
      await de.delete()
      await msg.delete()


@bot.slash_command(description = "Lets CEODealer to reset funds of the whole server to a specified amount.") # -----------------------------------------------------------------ResetServerBal
@commands.has_role("CEODealer")
async def resetserverbal(ctx, amount : float):
  await ctx.defer()
  servername = str(ctx.guild)

  if amount <= 0:
    embed = discord.Embed(
    colour = discord.Colour.brand_red(),
    )
    embed.set_author(name=f"You cannot set null or negative funds.")
    embed.set_footer(text=f"Code version - {code_version}")
    await ctx.respond(embed=embed)
  else:

    de = await ctx.send("Are you sure? You have 10 sec to respond Y/N .")

    msg = await bot.wait_for("message", timeout=10)
    if msg.author == ctx.author and "Y" in msg.content:
      cur.execute(f'''UPDATE balances SET balance = {amount} WHERE servername=?''', (servername,))
      con.commit()
      embed = discord.Embed(
      colour = discord.Colour.brand_green(),
      )
      embed.set_author(name=f"Reset of the server balance was successful, new balance is: {amount}")
      embed.set_footer(text=f"Code version - {code_version}")
      await ctx.respond(embed=embed)
      await de.delete()
      await msg.delete()

    elif msg.author == ctx.author and "N" in msg.content:
      embed = discord.Embed(
      colour = discord.Colour.dark_red(),
      )
      embed.set_author(name=f"Cancelling operation.")
      embed.set_footer(text=f"Code version - {code_version}")
      await ctx.respond(embed=embed)
      await de.delete()
      await msg.delete()

    else:
      embed = discord.Embed(
      colour = discord.Colour.brand_red(),
      )
      embed.set_author(name=f"{msg.author} replied, cancelling operation.")
      embed.set_footer(text=f"Code version - {code_version}")
      await ctx.respond(embed=embed)
      await de.delete()
      await msg.delete()


@bot.slash_command(description = "Create a betting.") # ------------------------------------------------------------------CreateBet
@commands.has_role("Dealer")
async def createbet(ctx):
 
  x = 0
  gid = str(ctx.guild.id)
  mid = str(ctx.author.id)
  gmid = str(gid+mid)
  cur.execute('''SELECT servermemberid FROM activebets WHERE servermemberid=?''', (gmid,))
  result = cur.fetchone()
 
  if result:
    await ctx.respond("You already have a bet open!", ephemeral=True)
    return
  
  betcode = randint(1000,9999)
 
  modal = CreateBetModal()

  await ctx.send_modal(modal)
  await modal.wait()

  cur.execute('''INSERT INTO activebets (servermemberid, servername, creatorname, betid) VALUES (?,?,?,?)''', (gmid, str(ctx.guild), str(ctx.author), int(betcode)))
  con.commit()

  title = modal.children[0].value
  description = modal.children[1].value
  options = modal.children[2].value.split("\n")
  timeout = 3600 if not modal.children[3].value.isdigit() else int(modal.children[3].value)*60
  timetill = timeout / 60

  if " " in options:
    options.remove(" ")
  if "  " in options:
    options.remove("  ")

  embed = discord.Embed(
    colour = discord.Colour.nitro_pink(),
  )
  embed.set_author(name=f"{title} - {betcode}")
  embed.add_field(name="Instructions", value="Bet by /bet <amount> <1/2> <betcode> . 1/2 - are the options, first or second. Betcode is the 4 digits at the end of the title.", inline=False)
  embed.add_field(name="Description", value=f"{description}", inline=False)
  for option in options:
    x += 1
    embed.add_field(name=f"Option - {x}", value=f"{option}", inline=True)
  if timeout is not None and timeout > 0:
    embed.add_field(name="Timeout", value=f"This voting is open for {timetill} minutes since this message till closing!", inline=False)
  embed.set_footer(text=f"Code version - {code_version}")


  message = await ctx.send(embed=embed)

  if timeout is not None and timeout > 0:
    await asyncio.sleep(timeout)
  
  await message.delete()

  cur.execute('''SELECT membername FROM betters WHERE betid=?''', (int(betcode),))
  allmembers = cur.fetchall()

  betamount1 = 0
  betamount2 = 0
  totalamount = 0
  betoption1 = 0
  betoption2 = 0
  totalvotes = 0
  for member in allmembers:

    member = str(member)
    member = member.replace("'"," ")
    member = member.replace("("," ")
    member = member.replace(")"," ")
    member = member.replace(","," ")
    member = member.strip()

    cur.execute('''SELECT betamount FROM betters WHERE membername=?''', (str(member),))
    betamounts = cur.fetchone()
    for bet in betamounts:
      betamount = int(bet)

    cur.execute('''SELECT betoption FROM betters WHERE membername=?''', (str(member),))
    betoptions = cur.fetchone()
    for option in betoptions:
      betoption = int(option)

    if betoption == 1:
      betoption1 += 1
      betamount1 += betamount
      totalamount += betamount
      totalvotes += 1

    if betoption == 2:
      betoption2 += 1
      betamount2 += betamount
      totalamount += betamount
      totalvotes += 1

  if betoption1 == 0:
    betoption1 = 1
  if betoption2 == 0:
    betoption2 = 1
  if betamount1 == 0:
    betamount1 = 1
  if betamount2 == 0:
    betamount2 = 1

  ratiovotes = betoption1 / betoption2
  ratiobets = betamount1 / betamount2
  ratiovotes = round(ratiovotes, 2)
  ratiobets = round(ratiobets, 2)

  embed = discord.Embed(
    colour = discord.Colour.nitro_pink(),
  )
  embed.set_author(name=f"{title} - CONCLUDED({betcode})")
  embed.add_field(name="Thanks for betting!", value="Everything will be paid out when Dealer execudes the command, till then results are as follow:")
  embed.add_field(name="Total amount in bets", value=f"***{totalamount}***", inline=True)
  embed.add_field(name="Total amount in votes", value=f"***{totalvotes}***", inline=True)
  embed.add_field(name="Ratio 1/2 in bets", value=f"***{ratiobets} : {betamount2 / betamount2}***", inline=True)
  embed.add_field(name="Ratio 1/2 in votes", value=f"***{ratiovotes} : {betoption2 / betoption2}***", inline=True)
  embed.add_field(name="|", value="|", inline=True)
  embed.add_field(name="Total amount in bets for option 1", value=f"***{betamount1}***", inline=True)
  embed.add_field(name="Total amount in votes for option 1", value=f"***{betoption1}***", inline=True)
  embed.add_field(name="|", value="|", inline=True)
  embed.add_field(name="Total amount in bets for option 2", value=f"***{betamount2}***", inline=True)
  embed.add_field(name="Total amount in votes for option 2", value=f"***{betoption2}***", inline=True)
  embed.add_field(name="|", value="|", inline=True)
  embed.set_footer(text=f"Code version - {code_version}")

  await ctx.send(embed=embed)


@bot.slash_command(description = "Deal out a betting.") # -----------------------------------------------------------------------------------------------------------------------------Deal bet
@commands.has_role("Dealer")
async def dealbet(ctx, winner: int, betcode: int):
  await ctx.defer()
  servername = str(ctx.guild)

  cur.execute('''SELECT membername FROM betters WHERE betid=? AND servername=?''', (int(betcode), servername))
  allmembers = cur.fetchall()

  betamount1 = 0
  betamount2 = 0
  totalamount = 0
  betoption1 = 0
  betoption2 = 0
  totalvotes = 0
  for member in allmembers:

    member = str(member)
    member = member.replace("'"," ")
    member = member.replace("("," ")
    member = member.replace(")"," ")
    member = member.replace(","," ")
    member = member.strip()

    cur.execute('''SELECT betamount FROM betters WHERE membername=?''', (str(member),))
    betamounts = cur.fetchone()
    for bet in betamounts:
      betamount = int(bet)

    cur.execute('''SELECT betoption FROM betters WHERE membername=?''', (str(member),))
    betoptions = cur.fetchone()
    for option in betoptions:
      betoption = int(option)

    if betoption == 1:
      betoption1 += 1
      betamount1 += betamount
      totalamount += betamount
      totalvotes += 1

    if betoption == 2:
      betoption2 += 1
      betamount2 += betamount
      totalamount += betamount
      totalvotes += 1

    if betoption1 == 0:
      betoption1 = 1
    if betoption2 == 0:
      betoption2 = 1
    if betamount1 == 0:
      betamount1 = 1
    if betamount2 == 0:
      betamount2 = 1

    if winner == 1:
      betamountwin = betamount1
    
    if winner == 2:
      betamountwin = betamount2

  await asyncio.sleep(0.5)

  cur.execute('''SELECT membername FROM betters WHERE betid=?''', (int(betcode),))
  allmembers = cur.fetchall()

  for member in allmembers:
    member = str(member)
    member = member.replace("'"," ")
    member = member.replace("("," ")
    member = member.replace(")"," ")
    member = member.replace(","," ")
    member = member.strip()

    cur.execute('''SELECT betoption FROM betters WHERE membername=? AND betid=?''', (str(member), int(betcode)))
    betoptions = cur.fetchone()
    for option in betoptions:
      betoption = int(option)

    if betoption == winner:
      cur.execute('''SELECT betamount FROM betters WHERE membername=? AND betid=?''', (str(member), int(betcode)))
      betamounts = cur.fetchone()
      for bet in betamounts:
        amount = int(bet)

      percentowed = amount/betamountwin
      owed = float(percentowed*totalamount)
      owed = round(owed, 2)

      cur.execute('''SELECT balance FROM balances WHERE membername=? AND servername=?''', (str(member), servername))
      x = cur.fetchone()
      for bal in x:
        memberbalanceold = float(bal)

      memberbalancenew = memberbalanceold + owed
      memberbalancenew = round(memberbalancenew, 2)

      cur.execute(f'''UPDATE balances SET balance = {memberbalancenew} WHERE membername=? AND servername=?''', (str(member), servername))
      con.commit()

    else:
      continue

  cur.execute('''DELETE FROM betters WHERE betid=?''', (int(betcode),))
  cur.execute('''DELETE FROM activebets WHERE betid=?''', (int(betcode),))
  con.commit()

  await ctx.respond("Everything has been dealt out!")


@bot.slash_command(description = "Bet on a betting.") # ------------------------------------------------------------------------------------------------------------------------------Bet
async def bet(ctx, amount: float, option: int, betcode: int):
  gid = str(ctx.guild.id)
  mid = str(ctx.author.id)
  gmid = str(gid+mid)
  servername = str(ctx.guild)

  cur.execute('''SELECT betid FROM activebets WHERE betid=? AND servername=?''', (betcode, servername))
  y = cur.fetchone()
  if not y:
    await ctx.respond("No bet with such id exists.")
    return

  cur.execute('''SELECT servermemberid FROM betters WHERE betid=? AND servername=? AND membername=?''', (betcode, servername, str(ctx.author)))
  x = cur.fetchone()
  if x:
    await ctx.respond("You already have a bet in place!")
    return

  cur.execute('''SELECT balance FROM balances WHERE membername=? AND servername=?''', (str(ctx.author), str(ctx.guild)))
  z = cur.fetchone()
  
  if z:
    cur.execute('''SELECT balance FROM balances WHERE membername=? AND servername=?''', (str(ctx.author), str(ctx.guild)))
    balanc = cur.fetchone()
    for bal in balanc:
      oldbalance = float(bal)

    if amount > oldbalance:
      await ctx.respond("Not enough funds, try less.")
      return
    elif amount <= 0:
      await ctx.respond("Can't bet zero or negative funds.")
      return
    elif option < 1 or option > 2:
      await ctx.respond("Choose one of the two options.")
      return

    newbalance = oldbalance - amount

    cur.execute(f'''UPDATE balances SET balance = {newbalance} WHERE membername=? AND servername=?''', (str(ctx.author), str(ctx.guild)))
    
    cur.execute('''INSERT INTO betters (servermemberid, servername, membername, betid, betoption, betamount) VALUES (?,?,?,?,?,?)''', (gmid, str(ctx.guild), str(ctx.author), betcode, option, amount))
    con.commit()

    await ctx.respond("Your bet has been registered!")

  else:
    await ctx.respond("You need a balance account to bet. Use /register")


@bot.slash_command()
async def fakey(ctx):
  betcode = randint(1000,9999)
  gid = str(ctx.guild.id)
  mid = str(ctx.author.id)
  gmid = str(gid+mid)
  cur.execute('''DELETE FROM activebets''')
  cur.execute('''DELETE FROM betters''')
  con.commit()
  print("done")


###################################################################################################################
# ----------------------------------------------------------------------------------------------------Misc commands
@bot.slash_command(description = "Pong!") # -------------------------------------------------------------------------------Ping
async def ping(ctx):
  await ctx.respond(f"Pong! {round (bot.latency * 1000)}ms")


@bot.slash_command(description = "Suggest a functionality to me!") # --------------------------------------------------------------------------------Suggest
async def botsuggest(ctx, title, suggestion):
  embed = discord.Embed(
    colour= discord.Colour.brand_green()
  )
  
  embed.set_author(name="Thank you for suggestion! I'll look into it!")
  embed.add_field(name=f"{title}", value=f"{suggestion}", inline=False)
  embed.set_footer(text=f"Geary - sent by @{ctx.author.display_name}#{ctx.author.discriminator}")

  await ctx.respond(embed=embed, ephemeral=True)

  await asyncio.sleep(2)

  embed = discord.Embed(
    colour= discord.Colour.brand_green()
  )
  
  embed.set_author(name="SUGGESTION!!!")
  embed.add_field(name=f"{title}", value=f"{suggestion}", inline=False)
  embed.set_footer(text=f"Geary - sent by @{ctx.author.display_name}#{ctx.author.discriminator}")

  owner = bot.get_user(323516632880250890)
  await owner.send(embed=embed)

  

@bot.slash_command(description = "Report a bug!") # --------------------------------------------------------------------------------Bug Report
async def botbug(ctx, title, bug):
  embed = discord.Embed(
    colour= discord.Colour.magenta()
  )
  
  embed.set_author(name="Thank you for the bug report! I'll look into it!")
  embed.add_field(name=f"{title}", value=f"{bug}", inline=False)
  embed.set_footer(text=f"Geary - sent by @{ctx.author.display_name}#{ctx.author.discriminator}")

  await ctx.respond(embed=embed, ephemeral=True)

  await asyncio.sleep(2)

  embed = discord.Embed(
    colour= discord.Colour.dark_red()
  )
  
  embed.set_author(name="BUG REPORT!!!")
  embed.add_field(name=f"{title}", value=f"{bug}", inline=False)
  embed.set_footer(text=f"Geary - sent by @{ctx.author.display_name}#{ctx.author.discriminator}")

  owner = bot.get_user(323516632880250890)
  await owner.send(embed=embed)


@bot.slash_command(description = "Sends an embed with the selected color.") # ------------------------------------------------------------------ Colors
async def colors(
  ctx: discord.ApplicationContext,
  color: Option(str, "Choose the color", choices=["default", "teal", "dark_teal", "green", "dark_green", "blue", "dark_blue", "purple", "dark_purple",
  "magenta", "dark_magenta", "gold", "dark_gold", "orange", "dark_orange", "red", "dark_red", "lighter_grey", "dark_grey", "light_grey", "darker_grey",
  "blurple", "greyple", "nitro_pink", "fuchsia"])
):
  if color == "default":
    decided = discord.Colour.default()
  if color == "teal":
    decided = discord.Colour.teal()
  if color == "dark_teal":
    decided = discord.Colour.dark_teal()
  if color == "green":
    decided = discord.Colour.green()
  if color == "dark_green":
    decided = discord.Colour.dark_green()
  if color == "blue":
    decided = discord.Colour.blue()
  if color == "dark_blue":
    decided = discord.Colour.dark_blue()
  if color == "purple":
    decided = discord.Colour.purple()
  if color == "dark_purple":
    decided = discord.Colour.dark_purple()
  if color == "magenta":
    decided = discord.Colour.magenta()
  if color == "dark_magenta":
    decided = discord.Colour.dark_magenta()
  if color == "gold":
    decided = discord.Colour.gold()
  if color == "dark_gold":
    decided = discord.Colour.dark_gold()
  if color == "orange":
    decided = discord.Colour.orange()
  if color == "dark_orange":
    decided = discord.Colour.dark_orange()
  if color == "red":
    decided = discord.Colour.red()
  if color == "dark_red":
    decided = discord.Colour.dark_red()
  if color == "lighter_grey":
    decided = discord.Colour.lighter_grey()
  if color == "dark_grey":
    decided = discord.Colour.dark_grey()
  if color == "light_grey":
    decided = discord.Colour.light_grey()
  if color == "darker_grey":
    decided = discord.Colour.darker_grey()
  if color == "blurple":
    decided = discord.Colour.blurple()
  if color == "greyple":
    decided = discord.Colour.greyple()
  if color == "nitro_pink":
    decided = discord.Colour.nitro_pink()
  if color == "fuchsia":
    decided = discord.Colour.fuchsia()
  embed = discord.Embed(
    color=decided
  )
  embed.add_field(name="Colors", value=f"This is the {color} color")
  await ctx.respond(embed=embed)

@bot.slash_command(description="This..uhh..helps...") # ----------------------------------------------------------------------------------------------------- Help
async def help(ctx):
  view = HelpSelectView(ctx)

  embed = discord.Embed(
  colour= discord.Colour.green()
  )
  embed.set_author(name="To start choose a category.")
  await ctx.respond(embed=embed, view=view)

######################################################################################################################################################### Select Roles

  

bot.run(os.environ["TOKEN"])