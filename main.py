
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5789487250:AAGoxWGHIr_s6W3itufy455qzKA3wWVfi8w'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("assalomu alaykum✋\nmen amonymus nikidaman va oliy talimda juda ham yaxshi oqiganman va men sizlarga math(matematika)📝 fizika🕹 va dasturlash(c# php web python java javascript c c++ go va ...)💻larga yordam bera olaman \nhammamizga malumki hozirda hech bir ish biron manfatsiz qilinmaydi shu un hamma ishni oz narxi bor.")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)