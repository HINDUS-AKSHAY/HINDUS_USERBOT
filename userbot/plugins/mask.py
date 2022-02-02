# credits to @HINDUS_USERBOT and @HINDUS_USERBOT

import os

from telegraph import exceptions, upload_file
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import hinduub

from ..Config import Config
from ..funcs.managers import edit_or_reply
from . import awooify, baguette, convert_toimage, iphonex, lolice

plugin_category = "tools"


@hinduub.hindu_cmd(
    pattern="mask$",
    command=("mask", plugin_category),
    info={
        "header": "reply to image to get hazmat suit for that image.",
        "usage": "{tr}mask",
    },
)
async def _(hindubot):
    "Hazmat suit maker"
    reply_message = await hindubot.get_reply_message()
    if not reply_message.media or not reply_message:
        return await edit_or_reply(hindubot, "```reply to media message```")
    chat = "@hazmat_suit_bot"
    if reply_message.sender.bot:
        return await edit_or_reply(hindubot, "```Reply to actual users message.```")
    event = await hindubot.edit("```Processing```")
    async with hindubot.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=905164246)
            )
            await hindubot.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            return await event.edit(
                "```Please unblock @hazmat_suit_bot and try again```"
            )
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await hindubot.client.send_file(event.chat_id, response.message.media)
            await event.delete()


@hinduub.hindu_cmd(
    pattern="awooify$",
    command=("awooify", plugin_category),
    info={
        "header": "Check yourself by replying to image.",
        "usage": "{tr}awooify",
    },
)
async def hindubot(hindumemes):
    "replied Image will be face of other image"
    replied = await hindumemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(hindumemes, "reply to a supported media file")
    if replied.media:
        hinduevent = await edit_or_reply(hindumemes, "passing to telegraph...")
    else:
        return await edit_or_reply(hindumemes, "reply to a supported media file")
    download_location = await hindumemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await hinduevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await hinduevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await hinduevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await hinduevent.edit("ERROR: " + str(exc))
    hindu = f"https://telegra.ph{response[0]}"
    hindu = await awooify(hindu)
    await hinduevent.delete()
    await hindumemes.client.send_file(hindumemes.chat_id, hindu, reply_to=replied)


@hinduub.hindu_cmd(
    pattern="lolice$",
    command=("lolice", plugin_category),
    info={
        "header": "image masker check your self by replying to image.",
        "usage": "{tr}lolice",
    },
)
async def hindubot(hindumemes):
    "replied Image will be face of other image"
    replied = await hindumemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(hindumemes, "reply to a supported media file")
    if replied.media:
        hinduevent = await edit_or_reply(hindumemes, "passing to telegraph...")
    else:
        return await edit_or_reply(hindumemes, "reply to a supported media file")
    download_location = await hindumemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await hinduevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await hinduevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await hinduevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await hinduevent.edit("ERROR: " + str(exc))
    hindu = f"https://telegra.ph{response[0]}"
    hindu = await lolice(hindu)
    await hinduevent.delete()
    await hindumemes.client.send_file(hindumemes.chat_id, hindu, reply_to=replied)


@hinduub.hindu_cmd(
    pattern="bun$",
    command=("bun", plugin_category),
    info={
        "header": "reply to image and check yourself.",
        "usage": "{tr}bun",
    },
)
async def hindubot(hindumemes):
    "replied Image will be face of other image"
    replied = await hindumemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(hindumemes, "reply to a supported media file")
    if replied.media:
        hinduevent = await edit_or_reply(hindumemes, "passing to telegraph...")
    else:
        return await edit_or_reply(hindumemes, "reply to a supported media file")
    download_location = await hindumemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await hinduevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await hinduevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await hinduevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await hinduevent.edit("ERROR: " + str(exc))
    hindu = f"https://telegra.ph{response[0]}"
    hindu = await baguette(hindu)
    await hinduevent.delete()
    await hindumemes.client.send_file(hindumemes.chat_id, hindu, reply_to=replied)


@hinduub.hindu_cmd(
    pattern="iphx$",
    command=("iphx", plugin_category),
    info={
        "header": "replied image as iphone x wallpaper.",
        "usage": "{tr}iphx",
    },
)
async def hindubot(hindumemes):
    "replied image as iphone x wallpaper."
    replied = await hindumemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(hindumemes, "reply to a supported media file")
    if replied.media:
        hinduevent = await edit_or_reply(hindumemes, "passing to telegraph...")
    else:
        return await edit_or_reply(hindumemes, "reply to a supported media file")
    download_location = await hindumemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await hinduevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await hinduevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await hinduevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await hinduevent.edit("ERROR: " + str(exc))
    hindu = f"https://telegra.ph{response[0]}"
    hindu = await iphonex(hindu)
    await hinduevent.delete()
    await hindumemes.client.send_file(hindumemes.chat_id, hindu, reply_to=replied)
