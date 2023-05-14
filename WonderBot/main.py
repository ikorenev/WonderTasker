import asyncio

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ParseMode
import GetDataFromURL as getTask
import Buttons_Input as kb


API_TOKEN = '5559949585:AAHFNSl8WQQgS_eDe7QCUmtfVoNFUCpRjQg'
bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)
photomotivation = open('files/3.png', 'rb')
photosmile = open('files/1.png', 'rb')
photostand = open('files/2.png', 'rb')


#Ответы бота на сообщения (Не клавиатура)
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





#async def Pars(wait_for,parser):
#    while True:
#        await asyncio.sleep(wait_for)
#        print('Parse')
#        pass

#if __name__ == '__main__':
#    loop=asyncio.get_event_loop()
#    loop.create_task(Pars(5,None))
#    executor.start_polling(dp,skip_updates=True)

#Вот эти 2 кнопки надо вырезать позже

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_main(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,'Текущие проекты: WonderWaffles', reply_markup=kb.inline_kb1)

@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_main(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,'Текущие Задачи: ТестЗадача2,ТестЗадача1, Сиквел, Сделать Игру ', reply_markup=kb.inline_kb1)

@dp.callback_query_handler(lambda c: c.data == 'button5')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_audio(callback_query.from_user.id, 'https://cs9-11v4.vkuseraudio.net/p2/d57bc18638cddf.mp3?extra=7uNOyzgAUDODxh-NfXnIeBATJuf6IiL35g2hnNhJ_Tw0XEJhVHaFFJuMBqXxhvi3eZQnIo33O327_4Vi38uUkrGGivRwNlgUvtNoSyzEQkaHjSIhy6NDR5wVBHG1CBvh-a2g-dF9apFErtsMo7Gmic41yQ&long_chunk=1', reply_markup=kb.inline_kb2)


@dp.callback_query_handler(lambda c: c.data == 'button4')
async def process_callback_main(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_photo(callback_query.from_user.id, photo=photomotivation,reply_markup=kb.inline_kb1)




@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_callback_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_photo(callback_query.from_user.id, photo=photosmile)
    await bot.send_message(callback_query.from_user.id, "Я умная вафля, и слежу за твоим прогрессом, сейчас я могу подсказать тебе твои текущие задачи,напомнить о дедлайнах и подбодрить тебя",reply_markup=kb.inline_kb1)


@dp.callback_query_handler(lambda c: c.data == 'button7')
async def process_callback_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, " ТестЗадача2 Дедлайн: 29 апреля 2023г. 7:38 ",reply_markup=kb.inline_kb1)

@dp.callback_query_handler(lambda c: c.data == 'button8')
async def process_callback_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Телеграмм для связи @Edlissss ",reply_markup=kb.inline_kb1)

@dp.callback_query_handler(lambda c: c.data == 'button9')
async def process_callback_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Выбери как часто мне напоминать о задачах? ",reply_markup=kb.inline_often)

@dp.callback_query_handler(lambda c: c.data == 'button10')
async def process_callback_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Ну давай посмотрим,что у тебя там получилось ",reply_markup=kb.inline_kb1)



#Кнопка назад

@dp.callback_query_handler(lambda c: c.data == 'buttonB')
async def process_callback_main(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Смотри как много я умею:", reply_markup=kb.inline_kb1)





#Частота оповещений

@dp.callback_query_handler(lambda c: c.data == 'often24')
async def process_callback_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Хорошо, я буду приходить к тебе с напоминанием раз в сутки ",reply_markup=kb.inline_kb1)

@dp.callback_query_handler(lambda c: c.data == 'often12')
async def process_callback_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Хорошо, я буду приходить к тебе с напоминанием раз в 12 часов ",reply_markup=kb.inline_kb1)
    

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
