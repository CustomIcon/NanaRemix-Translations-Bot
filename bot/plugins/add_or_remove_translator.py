from bot import bot, admins
from pyrogram import filters
from bot.utlis.poeditor import add_cont, del_cont


@bot.on_message(
    filters.user(admins) &
    filters.command(['addtranslator', 'addtranslator@NanaRemixTranslationsBot'], prefixes='/')
)
async def add_translator(_, message):
    try:
        args = message.text.split(None, 3)
        poedit = await add_cont(
            name=args[1],
            email=args[2],
            language=args[3]
        )
        await message.reply(poedit["response"]["message"])
    except IndexError:
        await message.reply('Arguments not complete, example: `addtranslator (name) (email) (language code)`')


@bot.on_message(
    filters.user(admins) &
    filters.command(['deltranslator', 'deltranslator@NanaRemixTranslationsBot'], prefixes='/')
)
async def del_translator(_, message):
    try:
        args = message.text.split(None, 3)
        poedit = await del_cont(
            name=args[1],
            email=args[2],
            language=args[3]
        )
        await message.reply(poedit["response"]["message"])
    except IndexError:
        await message.reply('Arguments not complete, example: `addtranslator (name) (email) (language code)`')