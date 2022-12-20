from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Держи вафлю 🧇')
button_end = KeyboardButton('Пока! 👋')
button_start = KeyboardButton('/start')

hi_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,).add(button_hi).add(button_end).add(button_start)



inline_btn_1 = InlineKeyboardButton('Над какими проектами ты работаешь', callback_data='button5')
inline_btn_2 = InlineKeyboardButton('Текущие задачи', callback_data='button5')
inline_btn_3 = InlineKeyboardButton('Дедлайны', callback_data='button5')
inline_btn_4 = InlineKeyboardButton('Добавить мотивации', callback_data='button4')
inline_btn_5 = InlineKeyboardButton('Поделиться песней', callback_data='button5')
inline_btn_6 = InlineKeyboardButton('О себе', callback_data='button6')
inline_btn_b = InlineKeyboardButton('Назад', callback_data = 'buttonB')



inline_kb1 = InlineKeyboardMarkup().add(inline_btn_4).add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_2).add(inline_btn_3)
inline_kb3 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_3)
inline_kb4 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)

inline_kb6 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)

##-------------------------------------------------------------------------------------------------------

