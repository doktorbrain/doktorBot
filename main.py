import discord
import os
from dotenv import load_dotenv
import random

#https://discord.com/api/oauth2/authorize?&client_id=795213505162248202&scope=bot&permissions=8
class MyClient(discord.Client):
  async def on_ready(self):
    print("Connected!")

  async def on_message(self,message):
    if message.author == myclient.user:
      return

    if message.content.startswith("Hi Bot"):
      await message.channel.send("Hi. Wie geht's?")
      # await message.delete(delay=3)
    elif message.content.startswith("$help"):
      await message.channel.send("Was ich weiß: $help, spiel")
    elif message.content.startswith("spiel"):
      await message.channel.send("$roulette [BID] \n [BID]->red,black,number")
    elif message.content.startswith("$roulette"):
      bid = message.content.split(' ')[1]
      bid_param = -3
      if bid.lower() == "black":
        bid_param = -1
      elif bid.lower() == "red":
        bid_param = -2
      else:
        try:
          bid_param = int(bid)
        except:
          bid_param = -3
      if bid_param == -3:
        await message.channel.send("BID Input not Valid")
        return
      result = random.randint(0,36)
      print(result)
      if bid_param == -1:
        won = result%2 == 0 and not result == 0
      elif bid_param == -2:
        won = result%2 == 1
      else:
        won = result == bid_param
      if won:
        await message.channel.send("$$$ Gewonnen! $$$")
      else:
        await message.channel.send("Leider verloren :-( - "+str(result))

  async def on_message_delete(self,message):
    print("deleted message: "+ message.content)

  async def on_message_edit(self,before,after):
    print("Changed message " + before.content + " to " + after.content)

load_dotenv(".env")

myToken = os.environ.get("DISCORD_TOKEN")
myclient=MyClient()
myclient.run(myToken)