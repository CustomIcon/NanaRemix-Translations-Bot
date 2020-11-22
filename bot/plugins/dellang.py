from bot import bot, admins
from pyrogram import filters
from bot.utlis.poeditor import del_language


@bot.on_message(
    filters.user(admins) &
    filters.command(['dellang', 'dellang@NanaRemixTranslationsBot'], prefixes='/')
)
async def del_lang(_, message):
    try:
        poedit = await del_language(message.text.split(None, 1)[1])
        if poedit['response']['status'] == 'success':
            await message.reply(f'{poedit["response"]["message"]}')
        else:
            await message.reply('Something went wrong!')
    except IndexError:
        await message.reply('Give me a language code to add.')