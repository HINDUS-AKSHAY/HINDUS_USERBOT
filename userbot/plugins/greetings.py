import random

from userbot import hinduub

from ..funcs.managers import edit_or_reply
from . import hindumemes

plugin_category = "tools"

# ===========================================================================================
S = (
    "..... (¯`v´¯)♥️\n"
    ".......•.¸.•´\n"
    "....¸.•´  🅷🅸\n"
    "... (   BABYy\n"
    "☻/ \n"
    "/▌✿🌷✿\n"
    "/ \     \|/\n"
)


U = (
    "🌙.     *       ☄️      \n"
    "🌟   .  *       .         \n"
    "                       *   .      🛰     .        ✨      *\n"
    "  .     *   SLEEP WELL        🚀     \n"
    "      .              . . SWEET DREAMS 🌙\n"
    ". *       🌏 GOOD NIGHT         *\n"
    "                     🌙.     *       ☄️      \n"
    "🌟   .  *       .         \n"
    "                       *   .      🛰     .        ✨      *\n"
)

W = (
    "G🌷o🍃o🌷D\n"
    "M🍃o🌷r🍃N🌷i🍃N🌷g\n"
    "            \n"
    "No matter how good or \n"
    "bad your life is,\n"
    "wake up each morning\n"
    "and be thankful.\n"
    "You still have a new day.\n"
    "        \n"
    "🌞   \n"
    "         \n"
    "╱◥████◣\n"
    "│田│▓ ∩ │◥███◣\n"
    "╱◥◣ ◥████◣田∩田│\n"
    "│╱◥█◣║∩∩∩ 田∩田│\n"
    "║◥███◣∩田∩ 田∩田│\n"
    "│∩│ ▓ ║∩田│║▓田▓\n"
    "🌹🌷🌹🌷🌹🍃🌷🌹🌷🌹\n"
)

X = (
    ".......🦋🦋........🦋🦋\n"
    "...🦋.........🦋🦋.......🦋\n"
    "...🦋............💙..........🦋\n"
    ".....🦋🅣🅗🅐🅝🅚🅢 🦋\n"
    "....... 🦋.................🦋\n"
    "..............🦋......🦋\n"
    "...................💙\n"
)
# =========================================================================================


@hinduub.hindu_cmd(
    pattern="baby$",
    command=("baby", plugin_category),
    info={
        "header": "Hi Baby art",
        "usage": "{tr}baby",
    },
)
async def baby(event):
    "Hi Baby art."
    await edit_or_reply(event, S)


@hinduub.hindu_cmd(
    pattern="hbd(?:\s|$)([\s\S]*)",
    command=("hbd", plugin_category),
    info={
        "header": "Happy birthday art.",
        "usage": "{tr}hbd <text>",
    },
)
async def hbd(event):
    "Happy birthday art."
    inpt = event.pattern_match.group(1)
    text = f"**♥️{inpt}♥️**"
    if not inpt:
        text = ""
    await edit_or_reply(
        event,
        f"▃▃▃▃▃▃▃▃▃▃▃\n┊ ┊ ┊ ┊ ┊ ┊\n┊ ┊ ┊ ┊ ˚✩ ⋆｡˚ ✩\n┊ ┊ ┊ ✫\n┊ ┊ ✧🎂🍰🍫🍭\n┊ ┊ ✯\n┊ . ˚ ˚✩\n........♥️♥️..........♥️♥️\n.....♥️........♥️..♥️........♥️\n...♥️.............♥️............♥️\n......♥️.....Happy.......♥️__\n...........♥️..............♥️__\n................♥️.....♥️__\n......................♥️__\n...............♥️......♥️__\n..........♥️...............♥️__\n.......♥️..Birthday....♥️\n.....♥️..........♥️..........♥️__\n.....♥️.......♥️_♥️.......♥️__\n.........♥️♥️........♥️♥️.....\n.............................................\n..... (¯`v´¯)♥️\n.......•.¸.•´STAY BLESSED\n....¸.•´      LOVE&FUN\n... (   YOU DESERVE\n☻/ THEM A LOT\n/▌✿🌷✿\n/ \     \|/\n▃▃▃▃▃▃▃▃▃▃▃\n\n{text}",
    )


@hinduub.hindu_cmd(
    pattern="thanks$",
    command=("thanks", plugin_category),
    info={
        "header": "Thanks art.",
        "usage": "{tr}thanks",
    },
)
async def gn(event):
    "Thanks art."
    await edit_or_reply(event, X)


@hinduub.hindu_cmd(
    pattern="gm$",
    command=("gm", plugin_category),
    info={
        "header": "Good morning random strings.",
        "usage": "{tr}gm",
    },
)
async def morning(morning):
    "Good morning random strings."
    txt = random.choice(hindumemes.GDMORNING)
    await edit_or_reply(morning, txt)


@hinduub.hindu_cmd(
    pattern="gnoon$",
    command=("gnoon", plugin_category),
    info={
        "header": "Good afternoon random strings.",
        "usage": "{tr}gnoon",
    },
)
async def noon(noon):
    "Good afternoon random strings."
    txt = random.choice(hindumemes.GDNOON)
    await edit_or_reply(noon, txt)


@hinduub.hindu_cmd(
    pattern="gn$",
    command=("gn", plugin_category),
    info={
        "header": "Good night random strings.",
        "usage": "{tr}gm",
    },
)
async def night(night):
    "Good night random strings."
    txt = random.choice(hindumemes.GDNIGHT)
    await edit_or_reply(night, txt)


@hinduub.hindu_cmd(
    pattern="gmg$",
    command=("gmg", plugin_category),
    info={
        "header": "Good morning art.",
        "usage": "{tr}gmg",
    },
)
async def gm(event):
    "Good morning art."
    await edit_or_reply(
        event,
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･\n╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮\n╭━┳━┳━┳╯┃╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n┣╮┣━┻━┻━╯╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･",
    )


@hinduub.hindu_cmd(
    pattern="gmg2$",
    command=("gmg2", plugin_category),
    info={
        "header": "Good morning art.",
        "usage": "{tr}gmg2",
    },
)
async def gm(event):
    "Good morning art."
    await edit_or_reply(
        event,
        "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗──────────╔╗\n║╔═╬═╦═╦╝║╔══╦═╦╦╦═╦╬╬═╦╦═╗\n║╚╗║╬║╬║╬║║║║║╬║╔╣║║║║║║║╬║\n╚══╩═╩═╩═╝╚╩╩╩═╩╝╚╩═╩╩╩═╬╗║\n────────────────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･",
    )


@hinduub.hindu_cmd(
    pattern="gmg3$",
    command=("gmg3", plugin_category),
    info={
        "header": "Good morning art.",
        "usage": "{tr}gmg3",
    },
)
async def gm(event):
    "Good morning art."
    await edit_or_reply(event, W)


@hinduub.hindu_cmd(
    pattern="gnt$",
    command=("gnt", plugin_category),
    info={
        "header": "Good night art.",
        "usage": "{tr}gnt",
    },
)
async def gn(event):
    "Good night art."
    await edit_or_reply(
        event,
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･\n╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮\n╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫\n┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯\n╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥° ♥｡･ﾟ♡ﾟ･",
    )


@hinduub.hindu_cmd(
    pattern="gnt2$",
    command=("gnt2", plugin_category),
    info={
        "header": "Good night art.",
        "usage": "{tr}gnt2",
    },
)
async def gn(event):
    "Good night art."
    await edit_or_reply(
        event,
        "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗╔═╦╦╗─╔╗╔╗\n║╔═╬═╦═╦╝║║║║╠╬═╣╚╣╚╗\n║╚╗║╬║╬║╬║║║║║║╬║║║╔╣\n╚══╩═╩═╩═╝╚╩═╩╬╗╠╩╩═╝\n──────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･",
    )


@hinduub.hindu_cmd(
    pattern="gnt3$",
    command=("gnt3", plugin_category),
    info={
        "header": "Good night art.",
        "usage": "{tr}gnt3",
    },
)
async def gn(event):
    "Good night art."
    await edit_or_reply(event, U)


# @PhycoNinja13b 's Part begin from here


@hinduub.hindu_cmd(
    pattern="hi(?:\s|$)([\s\S]*)",
    command=("hi", plugin_category),
    info={
        "header": "Hi text art.",
        "usage": [
            "{tr}hi <emoji>",
            "{tr}hi",
        ],
    },
)
async def hi(event):
    "Hi text art."
    giveVar = event.text
    hindu = giveVar[4:5]
    if not hindu:
        hindu = "🌺"
    await edit_or_reply(
        event,
        f"{hindu}✨✨{hindu}✨{hindu}{hindu}{hindu}\n{hindu}✨✨{hindu}✨✨{hindu}✨\n{hindu}{hindu}{hindu}{hindu}✨✨{hindu}✨\n{hindu}✨✨{hindu}✨✨{hindu}✨\n{hindu}✨✨{hindu}✨{hindu}{hindu}{hindu}\n☁☁☁☁☁☁☁☁",
    )


@hinduub.hindu_cmd(
    pattern="cheer$",
    command=("cheer", plugin_category),
    info={
        "header": "Cheer text art.",
        "usage": "{tr}cheer",
    },
)
async def cheer(event):
    "cheer text art."
    await edit_or_reply(
        event,
        "💐💐😉😊💐💐\n☕ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐",
    )


@hinduub.hindu_cmd(
    pattern="getwell$",
    command=("getwell", plugin_category),
    info={
        "header": "Get Well art.",
        "usage": "{tr}getwell",
    },
)
async def getwell(event):
    "Get Well art."
    await edit_or_reply(
        event, "🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹"
    )


@hinduub.hindu_cmd(
    pattern="luck$",
    command=("luck", plugin_category),
    info={
        "header": "luck art.",
        "usage": "{tr}luck",
    },
)
async def luck(event):
    "Luck art."
    await edit_or_reply(
        event, "💚~🍀🍀🍀🍀🍀\n🍀╔╗╔╗╔╗╦╗✨🍀\n🍀║╦║║║║║║👍🍀\n🍀╚╝╚╝╚╝╩╝。 🍀\n🍀・・ⓁⓊⒸⓀ🍀\n🍀🍀🍀 to you💚"
    )


@hinduub.hindu_cmd(
    pattern="sprinkle$",
    command=("sprinkle", plugin_category),
    info={
        "header": "sprinkle art.",
        "usage": "{tr}sprinkle",
    },
)
async def sprinkle(event):
    "Sprinkle text art."
    await edit_or_reply(
        event,
        "✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n🌸🌺🌸🌺🌸🌺🌸🌺\n Sprinkled with love❤\n🌷🌻🌷🌻🌷🌻🌷🌻\n ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n🌹🍀🌹🍀🌹🍀🌹🍀",
    )
