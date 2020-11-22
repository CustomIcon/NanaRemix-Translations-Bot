from bot import bot, admins
from pyrogram import filters
from bot.utlis.poeditor import add_language


@bot.on_message(
    filters.user(admins) &
    filters.command(['addlang', 'addlang@NanaRemixTranslationsBot'], prefixes='/')
)
async def add_lang(_, message):
    try:
        poedit = await add_language(message.text.split(None, 1)[1])
        if poedit['response']['status'] == 'success':
            await message.reply(f'{poedit["response"]["message"]}')
        else:
            await message.reply('Something went wrong!')
    except IndexError:
        await message.reply('Give me a language code to add.')