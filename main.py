import hikari
from extensions.mangadexAPI import getCoverArtLink
import lightbulb
import os
from dotenv import load_dotenv

load_dotenv()

Bot = lightbulb.BotApp(
    token=os.getenv("DISCORD_TOKEN"),
    default_enabled_guilds=(int(os.getenv("DISCORD_SERVER")))
)

@Bot.listen(hikari.GuildMessageCreateEvent)
async def listenForManga(event):
    if event.content.startswith("!manga-"):
        try:
            await event.message.respond(getCoverArtLink(event.content[7:]))
        except:
            await event.message.respond("No cover art")

@Bot.command
@lightbulb.command("hello", "hello user")
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond("Hello Human")

Bot.run()
