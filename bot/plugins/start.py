from bot import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button = InlineKeyboardMarkup(
    [[InlineKeyboardButton('Join the Group', url='https://t.me/translation_nanaremix')]]
)

@bot.on_message(
    filters.command("start", prefixes='/')
)
async def alive(_, message):
    if message.chat.type == 'private':
        await message.reply(
            f'Hi {message.from_user.mention},This is the Helper for @translation_nanaremix. Join the Group and help us Translate the Userbot',
            reply_markup=button
        )
    else:
        await message.reply('sup!')