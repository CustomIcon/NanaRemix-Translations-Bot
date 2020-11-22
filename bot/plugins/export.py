from bot import bot, admins
from pyrogram import filters
from bot.utlis.poeditor import export_translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@bot.on_message(
    filters.command(['export', 'export@NanaRemixTranslationsBot'], prefixes='/') &
    filters.user(admins)
)
async def export_file(_, message):
    try:
        poedit = await export_translation(message.text.split(None, 1)[1])
        if poedit['response']['status'] == 'success':
            button = InlineKeyboardMarkup(
                [[InlineKeyboardButton('Download', url=f'{poedit["result"]["url"]}')]]
            )
            await message.reply('Download Language File:', reply_markup=button)
        else:
            await message.reply('Something went wrong!')
    except IndexError:
        await message.reply('Give me a language code.')