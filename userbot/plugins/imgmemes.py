#  Copyright (C) 2020  Copyless786(π.$)
# credits to @HINDUS_USERBOT (@HINDUS_USERBOT)
import asyncio
import os
import re

from userbot import hinduub

from ..funcs.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import (
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)

plugin_category = "fun"


@hinduub.hindu_cmd(
    pattern="fakegs(?:\s|$)([\s\S]*)",
    command=("fakegs", plugin_category),
    info={
        "header": "Fake google search meme",
        "usage": "{tr}fakegs search query ; what you mean text",
        "examples": "{tr}fakegs HINDUS USERBOT ; One of the Popular userbot",
    },
)
async def nekobot(hindu):
    "Fake google search meme"
    text = hindu.pattern_match.group(1)
    reply_to_id = await reply_id(hindu)
    if not text:
        if hindu.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            return await edit_delete(hindu, "`What should i search in google.`", 5)
    cate = await edit_or_reply(hindu, "`Connecting to https://www.google.com/ ...`")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await edit_delete(
            hindu,
            "__How should i create meme follow the syntax as show__ `.fakegs top text ; bottom text`",
            5,
        )
        return
    hindufile = await fakegs(search, result)
    await asyncio.sleep(2)
    await hindu.client.send_file(hindu.chat_id, hindufile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(hindufile):
        os.remove(hindufile)


@hinduub.hindu_cmd(
    pattern="trump(?:\s|$)([\s\S]*)",
    command=("trump", plugin_category),
    info={
        "header": "trump tweet sticker with given custom text",
        "usage": "{tr}trump <text>",
        "examples": "{tr}trump HINDUS USERBOT is One of the Popular userbot",
    },
)
async def nekobot(hindu):
    "trump tweet sticker with given custom text_"
    text = hindu.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(hindu)

    reply = await hindu.get_reply_message()
    if not text:
        if hindu.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(hindu, "**Trump : **`What should I tweet`", 5)
    cate = await edit_or_reply(hindu, "`Requesting trump to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    hindufile = await trumptweet(text)
    await hindu.client.send_file(hindu.chat_id, hindufile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(hindufile):
        os.remove(hindufile)


@hinduub.hindu_cmd(
    pattern="modi(?:\s|$)([\s\S]*)",
    command=("modi", plugin_category),
    info={
        "header": "modi tweet sticker with given custom text",
        "usage": "{tr}modi <text>",
        "examples": "{tr}modi HINDUS USERBOT is One of the Popular userbot",
    },
)
async def nekobot(hindu):
    "modi tweet sticker with given custom text"
    text = hindu.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(hindu)

    reply = await hindu.get_reply_message()
    if not text:
        if hindu.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(hindu, "**Modi : **`What should I tweet`", 5)
    cate = await edit_or_reply(hindu, "Requesting modi to tweet...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    hindufile = await moditweet(text)
    await hindu.client.send_file(hindu.chat_id, hindufile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(hindufile):
        os.remove(hindufile)


@hinduub.hindu_cmd(
    pattern="cmm(?:\s|$)([\s\S]*)",
    command=("cmm", plugin_category),
    info={
        "header": "Change my mind banner with given custom text",
        "usage": "{tr}cmm <text>",
        "examples": "{tr}cmm HINDUS USERBOT is One of the Popular userbot",
    },
)
async def nekobot(hindu):
    text = hindu.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(hindu)

    reply = await hindu.get_reply_message()
    if not text:
        if hindu.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(hindu, "`Give text to write on banner, man`", 5)
    cate = await edit_or_reply(hindu, "`Your banner is under creation wait a sec...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    hindufile = await changemymind(text)
    await hindu.client.send_file(hindu.chat_id, hindufile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(hindufile):
        os.remove(hindufile)


@hinduub.hindu_cmd(
    pattern="kanna(?:\s|$)([\s\S]*)",
    command=("kanna", plugin_category),
    info={
        "header": "kanna chan sticker with given custom text",
        "usage": "{tr}kanna text",
        "examples": "{tr}kanna HINDUS USERBOT is One of the Popular userbot",
    },
)
async def nekobot(hindu):
    "kanna chan sticker with given custom text"
    text = hindu.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(hindu)

    reply = await hindu.get_reply_message()
    if not text:
        if hindu.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(hindu, "**Kanna : **`What should i show you`", 5)
    cate = await edit_or_reply(hindu, "`Kanna is writing your text...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    hindufile = await kannagen(text)
    await hindu.client.send_file(hindu.chat_id, hindufile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(hindufile):
        os.remove(hindufile)


@hinduub.hindu_cmd(
    pattern="tweet(?:\s|$)([\s\S]*)",
    command=("tweet", plugin_category),
    info={
        "header": "The desired person tweet sticker with given custom text",
        "usage": "{tr}tweet <username> ; <text>",
        "examples": "{tr}tweet iamsrk ; HINDUS USERBOT is One of the Popular userbot",
    },
)
async def nekobot(hindu):
    "The desired person tweet sticker with given custom text"
    text = hindu.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(hindu)

    reply = await hindu.get_reply_message()
    if not text:
        if hindu.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(
                hindu,
                "what should I tweet? Give some text and format must be like `.tweet username ; your text` ",
                5,
            )
    if ";" in text:
        username, text = text.split(";")
    else:
        await edit_delete(
            hindu,
            "__what should I tweet? Give some text and format must be like__ `.tweet username ; your text`",
            5,
        )
        return
    cate = await edit_or_reply(hindu, f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    hindufile = await tweets(text, username)
    await hindu.client.send_file(hindu.chat_id, hindufile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(hindufile):
        os.remove(hindufile)
