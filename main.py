import hikari
from extensions.mangaClass import *
import lightbulb
import os
from dotenv import load_dotenv

load_dotenv()

Bot = lightbulb.BotApp(
    token=os.getenv("DISCORD_TOKEN"),
    default_enabled_guilds=(int(os.getenv("DISCORD_SERVER")))
)

@Bot.listen()
async def listenForManga(event: hikari.GuildMessageCreateEvent):
    if event.content.startswith("!manga-"):
        try:
            manga = Manga(event.content[7:])
            embedmsg = hikari.Embed(title= manga.titles['en'])
            embedmsg = embedmsg.set_image(manga.manga_cover_link)
            await event.message.respond(embedmsg)
            await event.message.delete()
        except:
            await event.message.respond("error")

@Bot.command
@lightbulb.command("hello", "hello user")
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond("Hello Human")

Bot.run()
