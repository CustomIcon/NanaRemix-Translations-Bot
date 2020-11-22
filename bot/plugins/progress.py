from bot import bot, admins
from pyrogram import filters
from bot.utlis.poeditor import progress_list

@bot.on_message(
    filters.command(['progress', 'progress@NanaRemixTranslationsBot'], prefixes='/') &
    filters.user(admins)
)
async def progresses(_, message):
    poedit = await progress_list()
    if poedit['response']['status'] == 'success':
        languages = poedit['result']['languages']
        text = '╒═══「 **Languages** 」\n'
        for m in languages:
            text += f'╞══「 {m["name"]} ({m["code"]})」 \n'
            text += f'│ • __Translations:__ `{m["translations"]}`  __Progress:__ `{m["percentage"]}%`\n'
        text += f'╘══「 **Count {len(languages)}** 」'
        await message.reply(text)
    else:
        await message.reply('Something went wrong!')