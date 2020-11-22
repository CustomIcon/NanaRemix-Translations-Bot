from bot import bot, admins
from pyrogram import filters
from bot.utlis.poeditor import view_project

@bot.on_message(
    filters.command("view", prefixes='/') &
    filters.user(admins)
)
async def alive(_, message):
    poedit = await view_project()
    if poedit['response']['status'] == 'success':
        text = f'**Project ID:** `{poedit["result"]["project"]["id"]}`\n'
        text += f'**Project Name:** `{poedit["result"]["project"]["name"]}`\n'
        text += f'**Public:** `{poedit["result"]["project"]["public"]}`\n'
        text += f'**Reference Language:** `{poedit["result"]["project"]["reference_language"]}`\n'
        text += f'**Terms:** `{poedit["result"]["project"]["terms"]}`\n'
        text += f'**Created on:** `{poedit["result"]["project"]["created"]}`\n'
        await message.delete()
        await message.reply(text)
    else:
        await message.delete()
        await message.reply('Something went wrong!')