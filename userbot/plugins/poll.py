import random

from telethon.errors.rpcbaseerrors import ForbiddenError
from telethon.errors.rpcerrorlist import PollOptionInvalidError
from telethon.tl.types import InputMediaPoll, Poll

from userbot import hinduub

from ..funcs.managers import edit_or_reply
from . import Build_Poll, reply_id

plugin_category = "tools"


@hinduub.hindu_cmd(
    pattern="poll(?:\s|$)([\s\S]*)",
    command=("poll", plugin_category),
    info={
        "header": "To create a poll.",
        "description": "If you doesnt give any input it sends a default poll",
        "usage": ["{tr}poll", "{tr}poll question ; option 1; option2"],
        "examples": "{tr}poll Are you an early bird or a night owl ;Early bird ; Night owl",
    },
)
async def pollcreator(hindupoll):
    "To create a poll"
    reply_to_id = await reply_id(hindupoll)
    string = "".join(hindupoll.text.split(maxsplit=1)[1:])
    if not string:
        options = Build_Poll(["Yah sure 😊✌️", "Nah 😏😕", "Whatever die sur 🥱🙄"])
        try:
            await hindupoll.client.send_message(
                hindupoll.chat_id,
                file=InputMediaPoll(
                    poll=Poll(
                        id=random.getrandbits(32),
                        question="👆👆So do you guys agree with this?",
                        answers=options,
                    )
                ),
                reply_to=reply_to_id,
            )
            await hindupoll.delete()
        except PollOptionInvalidError:
            await edit_or_reply(
                hindupoll,
                "`A poll option used invalid data (the data may be too long).`",
            )
        except ForbiddenError:
            await edit_or_reply(hindupoll, "`This chat has forbidden the polls`")
        except exception as e:
            await edit_or_reply(hindupoll, str(e))
    else:
        hinduinput = string.split(";")
        if len(hinduinput) > 2 and len(hinduinput) < 12:
            options = Build_Poll(hinduinput[1:])
            try:
                await hindupoll.client.send_message(
                    hindupoll.chat_id,
                    file=InputMediaPoll(
                        poll=Poll(
                            id=random.getrandbits(32),
                            question=hinduinput[0],
                            answers=options,
                        )
                    ),
                    reply_to=reply_to_id,
                )
                await hindupoll.delete()
            except PollOptionInvalidError:
                await edit_or_reply(
                    hindupoll,
                    "`A poll option used invalid data (the data may be too long).`",
                )
            except ForbiddenError:
                await edit_or_reply(hindupoll, "`This chat has forbidden the polls`")
            except Exception as e:
                await edit_or_reply(hindupoll, str(e))
        else:
            await edit_or_reply(
                hindupoll,
                "Make sure that you used Correct syntax `.poll question ; option1 ; option2`",
            )
