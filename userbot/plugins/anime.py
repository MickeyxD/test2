import re

from vampBot import bot
from vampBot.utils import admin_cmd, sudo_cmd, edit_or_reply
from vampBot.cmdhelp import CmdHelp
from vampBot.helpers.functions import deEmojify


@bot.on(admin_cmd(pattern="anime(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="anime(?: |$)(.*)", allow_sudo=True))
async def nope(vamp):
    vamp = vamp.pattern_match.group(1)
    if not vamp:
        if vamp.is_reply:
            (await vamp.get_reply_message()).message
        else:
            await edit_or_reply(vamp, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("animedb_bot", f"{(deEmojify(vamp))}")

    await troll[0].click(
        vamp.chat_id,
        reply_to=vamp.reply_to_msg_id,
        silent=True if vamp.is_reply else False,
        hide_via=True,
    )
    await vamp.delete()
    

CmdHelp("anime").add_command(
  "anime", "<anime name>", "Searches for the given anime and sends the details."
).add()
