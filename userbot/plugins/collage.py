# collage plugin for HINDUS USERBOT by @HINDUS_USERBOT

# Copyright (C) 2020 Alfiananda P.A
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.import os

import os

from userbot import hinduub

from ..funcs.managers import edit_delete, edit_or_reply
from ..helpers import _hinduutils, reply_id
from . import make_gif

plugin_category = "utils"


@hinduub.hindu_cmd(
    pattern="collage(?:\s|$)([\s\S]*)",
    command=("collage", plugin_category),
    info={
        "header": "To create collage from still images extracted from video/gif.",
        "description": "Shows you the grid image of images extracted from video/gif. you can customize the Grid size by giving integer between 1 to 9 to cmd by default it is 3",
        "usage": "{tr}collage <1-9>",
    },
)
async def collage(event):
    "To create collage from still images extracted from video/gif."
    hinduinput = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    hinduid = await reply_id(event)
    event = await edit_or_reply(
        event, "```collaging this may take several minutes too..... 😁```"
    )
    if not (reply and (reply.media)):
        await event.edit("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    hindusticker = await reply.download_media(file="./temp/")
    if not hindusticker.endswith((".mp4", ".mkv", ".tgs")):
        os.remove(hindusticker)
        await event.edit("`Media format is not supported...`")
        return
    if hinduinput:
        if not hinduinput.isdigit():
            os.remove(hindusticker)
            await event.edit("`You input is invalid, check help`")
            return
        hinduinput = int(hinduinput)
        if not 0 < hinduinput < 10:
            os.remove(hindusticker)
            await event.edit(
                "`Why too big grid you cant see images, use size of grid between 1 to 9`"
            )
            return
    else:
        hinduinput = 3
    if hindusticker.endswith(".tgs"):
        hmm = await make_gif(event, hindusticker)
        if hmm.endswith(("@tgstogifbot")):
            os.remove(hindusticker)
            return await event.edit(hmm)
        collagefile = hmm
    else:
        collagefile = hindusticker
    endfile = "./temp/collage.png"
    hinducmd = f"vcsi -g {hinduinput}x{hinduinput} '{collagefile}' -o {endfile}"
    stdout, stderr = (await _hinduutils.runcmd(hinducmd))[:2]
    if not os.path.exists(endfile):
        for files in (hindusticker, collagefile):
            if files and os.path.exists(files):
                os.remove(files)
        return await edit_delete(
            event, "`media is not supported or try with smaller grid size`", 5
        )

    await event.client.send_file(
        event.chat_id,
        endfile,
        reply_to=hinduid,
    )
    await event.delete()
    for files in (hindusticker, collagefile, endfile):
        if files and os.path.exists(files):
            os.remove(files)
