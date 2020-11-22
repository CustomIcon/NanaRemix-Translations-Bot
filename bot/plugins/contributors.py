from bot import bot, admins
from pyrogram import filters
from bot.utlis.poeditor import cont_list

@bot.on_message(
    filters.command(["translators", "translators@NanaRemixTranslationsBot"], prefixes='/') &
    filters.user(admins)
)
async def translators_list(_, message):
    poedit = await cont_list()
    if poedit['response']['status'] == 'success':
        text = ''
        for m in poedit['result']['contributors']:
            text += f'__{m["name"]}__ - `{m["email"]}`\n'
        await message.reply(text)
    else:
        await message.reply('Something went wrong!')