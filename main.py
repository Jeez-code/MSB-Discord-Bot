import discord
import os

client = discord.Client()

online_players = []
channel_exists = True


@client.event
async def on_ready():
    print("BOT IS ONLINE")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ".msb":

        await message.channel.send(
            "```Available commands:\n.msb -> Commands List\n.on -> Set yourself as connected in the minecraft server\n.off -> Set yourself as disconnected in the minecraft server\n.players -> Check who is currently connected to the server\n.start -> Gives you the link to the aternos Control Panel\n.clear -> Clear all recent messages```")

    elif message.content == ".on":

        if message.author.name not in online_players:
            online_players.append(message.author.name)
            await message.channel.send(
                "```{} connected!\n{} connected players.```".format(message.author.name, len(online_players)))

        else:
            await message.author.send("You are connected already!")

    elif message.content == ".off":
        if message.author.name in online_players:
            online_players.remove(message.author.name)
            await message.channel.send(
                "```{} disconnected!\n{} connected players.```".format(message.author.name, len(online_players)))
        else:
            await message.author.send("You are disconnected already!")

    elif message.content == ".players":
        await message.channel.send("```Connected Players:```")
        for i in range(len(online_players)):
            await message.channel.send("``` - {}```".format(online_players[i]))

    elif message.content == ".start":
        await message.author.send("If u don't know the credentials i'm not telling u :))\nhttps://aternos.org/go/")
        await message.channel.send("```Sent to you on private...```")
    elif message.content == ".clear":
        with message.channel.typing():
            await message.delete()
            await message.channel.purge(limit=100)

    await message.delete()


client.run(os.getenv('TOKEN'))
