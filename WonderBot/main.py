from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
import GetDataFromURL as imp
import Buttons_Input as kb


API_TOKEN = '5559949585:AAHFNSl8WQQgS_eDe7QCUmtfVoNFUCpRjQg'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
photomotivation = open('files/3.png', 'rb')
photosmile = open('files/1.png', 'rb')
photostand = open('files/2.png', 'rb')



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ твой личный помощник, Вафля Тян.\nДавай договоримся, ты даешь мне вкусняшки, а я делаю что-то полезное для тебя", reply_markup=kb.hi_kb)
    await bot.send_photo(chat_id=message.chat.id, photo=photostand)

@dp.message_handler(text='Держи вафлю 🧇')
async def process_hi_command(message: types.Message):
    await message.reply("Смотри как много я умею:", reply_markup=kb.inline_kb1)

@dp.message_handler(text='Пока! 👋')
async def process_hi_command(message: types.Message):
    await message.reply("Ты просто не понимаешь от чего отказываешься", reply_markup=kb.hi_kb)


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, imp.weather,reply_markup=kb.inline_kb2)

@dp.callback_query_handler(lambda c: c.data == 'button5')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_audio(callback_query.from_user.id, 'https://cs9-11v4.vkuseraudio.net/p2/d57bc18638cddf.mp3?extra=7uNOyzgAUDODxh-NfXnIeBATJuf6IiL35g2hnNhJ_Tw0XEJhVHaFFJuMBqXxhvi3eZQnIo33O327_4Vi38uUkrGGivRwNlgUvtNoSyzEQkaHjSIhy6NDR5wVBHG1CBvh-a2g-dF9apFErtsMo7Gmic41yQ&long_chunk=1', reply_markup=kb.inline_kb2)


@dp.callback_query_handler(lambda c: c.data == 'button4')
async def process_callback_main(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_photo(callback_query.from_user.id, photo=photomotivation,reply_markup=kb.inline_kb6)


@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_callback_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Я умная вафля, я только учусь. Сейчас я умею показывать забавные картинки животных, показать тебе погоду в твоем городе, надеюсь в будущем научиться мотивировать тебя работать",reply_markup=kb.inline_kb4)



    
@dp.callback_query_handler(lambda c: c.data == 'buttonB')
async def process_callback_main(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Смотри как много я умею:", reply_markup=kb.inline_kb1)
    

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
