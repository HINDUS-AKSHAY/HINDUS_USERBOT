import random
import re
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from userbot import StartTime, hinduub, hinduversion

from ..Config import Config
from ..funcs.managers import edit_or_reply
from ..helpers.functions import check_data_base_heal_th, get_readable_time, HINDUS_USERBOTalive
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"


@HINDUS_USERBOT.HINDUS_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    hinduevent = await edit_or_reply(event, "`Aliving✨...`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or " 💫 "
    ALIVE_TEXT = (
        gvarstatus("ALIVE_TEXT") or "**धर्मो रक्षति रक्षितः ||🚩**"
    )
    LION_IMG = gvarstatus("ALIVE_PIC")
    Lion_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = Lion_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        hindusver=hindusversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if HINDUS_IMG:
        HINDUS = [x for x in HINDUS_IMG.split()]
        PIC = random.choice(HINDUS)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await hindusevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                hindusevent,
                f"Media Value Error!!\nChange the link by .setdv\n\nCan't get media from this link :- {PIC}",
            )
    else:
        await edit_or_reply(
            hindusevent,
            caption,
        )


temp = """{ALIVE_TEXT}
{EMOJI} Database : {dbhealth}
{EMOJI} Telethon Version : {telever}
{EMOJI} HINDUSsub Version : {hinduver}
{EMOJI} Python Version : {pyver}
{EMOJI} Uptime : {uptime}
{EMOJI} Master: {mention}"""


@HINDUS_USERBOT.HINDUS_cmd(
    pattern="ialive$",
    command=("ialive", plugin_category),
    info={
        "header": "To check bot's alive status via inline mode",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}ialive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    EMOJI = gvarstatus("ALIVE_EMOJI") or " ✨ "
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**HINDUSub is Up and Running**"
    HINDUS_caption = f"{ALIVE_TEXT}\n"
    HINDUS_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
    HINDUS_caption += f"**{EMOJI} HINDUSub Version :** `{HINDUSversion}`\n"
    HINDUS_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
    HINDUS_caption += f"**{EMOJI} Master:** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, Lion_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@HINDUS_USERBOT.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await hindualive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
