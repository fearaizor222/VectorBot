import hikari
import mangadex
import lightbulb
import os
#from dotenv import load_dotenv

#load_dotenv()

def findCoverArt(name):
    api = mangadex.Api()
    manga = api.get_manga_list(title = name)
    manga = manga[0]
    manga = api.get_cover(manga.coverId)
    return manga.fetch_cover_image()

Bot = lightbulb.BotApp(
    token=os.getenv("DISCORD_TOKEN"),
    default_enabled_guilds=(int(os.getenv("DISCORD_SERVER")))
)

@Bot.listen(hikari.GuildMessageCreateEvent)
async def listenForManga(event):
    if event.content.startswith("!manga-"):
        try:
            await event.message.respond(findCoverArt(event.content[7:]))
        except:
            await event.message.respond("No cover art")

@Bot.command
@lightbulb.command("hello", "hello user")
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond("Hello Human")

Bot.run()
