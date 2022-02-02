import nekos

from userbot import hinduub

from ..funcs.managers import edit_or_reply

plugin_category = "fun"


@hinduub.hindu_cmd(
    pattern="thindu$",
    command=("thindu", plugin_category),
    info={
        "header": "Some random hindu facial text art",
        "usage": "{tr}thindu",
    },
)
async def hmm(hindu):
    "Some random hindu facial text art"
    reacthindu = nekos.texthindu()
    await edit_or_reply(hindu, reacthindu)


@hinduub.hindu_cmd(
    pattern="why$",
    command=("why", plugin_category),
    info={
        "header": "Sends you some random Funny questions",
        "usage": "{tr}why",
    },
)
async def hmm(hindu):
    "Some random Funny questions"
    nekos.why()
    await edit_or_reply(hindu, whycat)


@hinduub.hindu_cmd(
    pattern="fact$",
    command=("fact", plugin_category),
    info={
        "header": "Sends you some random facts",
        "usage": "{tr}fact",
    },
)
async def hmm(hindu):
    "Some random facts"
    facthindu = nekos.fact()
    await edit_or_reply(hindu, facthindu)
