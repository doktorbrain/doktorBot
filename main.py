import discord
#https://discord.com/api/oauth2/authorize?&client_id=795213505162248202&scope=bot
class MyClient(discord.Client):
  async def on_ready(self):
    print("Connected!")

  async def on_message(self,message):
    if message.author == myclient.user:
      return

    if message.content.startswith("Hi Bot"):
      await message.channel.send("Hi. Wie geht's?")


myclient=MyClient()
myclient.run("Nzk1MjEzNTA1MTYyMjQ4MjAy.X_GGSQ.maD2qOKso8yHbByp76Dj2teusVM")