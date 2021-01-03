import discord
import os
from dotenv import load_dotenv

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
      await message.channel.send("ich überlege mir noch eins...")

  async def on_message_delete(self,message):
    print("deleted message: "+ message.content)

  async def on_message_edit(self,before,after):
    print("Changed message " + before.content + " to " + after.content)

load_dotenv(".env")

myToken = os.environ.get("DISCORD_TOKEN")
myclient=MyClient()
myclient.run(myToken)