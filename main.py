import discord
import os
from dotenv import load_dotenv
import random
from keep_alive import keep_alive


#https://discord.com/api/oauth2/authorize?&client_id=795213505162248202&scope=bot&permissions=8
class MyClient(discord.Client):
    async def on_ready(self):
        print("Connected!")

    async def on_message(self, message):
        if message.author == myclient.user:
            return

        if message.content.startswith("Hi Bot"):
            await message.channel.send("Hi. Wie geht's? Ich kann Dir mit $help sagen, was ich kann.")
            # await message.delete(delay=3)
        elif message.content.startswith("$help"):
            await message.channel.send("Was ich kann: $help, $spiel")
        elif message.content.startswith("$spiel"):
            await message.channel.send(
                "$roulette [BID] \n [BID] -> red or black or number")
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
            result = random.randint(0, 36)
            print(result)
            if bid_param == -1:
                won = result % 2 == 0 and not result == 0
            elif bid_param == -2:
                won = result % 2 == 1
            else:
                won = result == bid_param
            if won:
                await message.channel.send("$$$ Gewonnen! $$$ | Zahl: " + str(result))
            else:
                await message.channel.send("Leider verloren :-( die Zahl war: " + str(result))
        elif message.content.startswith("$rm*"):
          await message.channel.send("removing messages...")
          await message.delete()
          nachrichten = await message.channel.history(limit=200).flatten()
          print(nachrichten[0])

    async def on_message_delete(self, message):
        print("deleted message: " + message.content)

    async def on_message_edit(self, before, after):
        print("Changed message " + before.content + " to " + after.content)


load_dotenv(".env")
keep_alive()
myToken = os.environ.get("DISCORD_TOKEN")
myclient = MyClient()
myclient.run(myToken)
