from asyncio import sleep

from userbot import hinduub

plugin_category = "utils"


@hinduub.hindu_cmd(
    pattern="schd (\d*) ([\s\S]*)",
    command=("schd", plugin_category),
    info={
        "header": "To schedule a message after given time(in seconds).",
        "usage": "{tr}schd <time_in_seconds>  <message to send>",
        "examples": "{tr}schd 120 hello",
    },
)
async def _(event):
    "To schedule a message after given time"
    hindu = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = hindu[1]
    ttl = int(hindu[0])
    await event.delete()
    await sleep(ttl)
    await event.respond(message)
