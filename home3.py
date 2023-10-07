from aiogram import Bot, Dispatcher, types, executor
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

start_keyboards = [
    types.KeyboardButton("Backend"),
    types.KeyboardButton("Frontend"),
    types.KeyboardButton("UX/UI"),
    types.KeyboardButton("Android"),
    types.KeyboardButton("iOS")
]

start_button = types.ReplyKeyboardMarkup().add(*start_keyboards)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здраствуйте, {message.from_user.full_name}", reply_markup=start_button)
    print(message)

@dp.message_handler(text="Backend")
async def backend(message:types.Message):
    await message.answer("""Backend — это внутренняя часть сайта и сервера и т.д
Стоимость 10000 сом в месяц
Обучение: 5 месяц""")

@dp.message_handler(text='Frontend')
async def frontend(message:types.Message):
    await message.answer("""Стань Frontend-разработчиком с нуля за 5 месяцев и получи доступ к стажировке + помощь в трудоустройстве!

Длительность: 5 месяцев""")

@dp.message_handler(text='UX/UI')
async def uxui(message:types.Message):
    await message.answer("""Стань UX/UI-дизайнером с нуля за 3 месяца и получи доступ к стажировке + помощь в трудоустройстве!

Длительность: 3 месяца""")

@dp.message_handler(text='Android')
async def android(message:types.Message):
    await message.answer("""Стань Android-разработчиком с нуля за 7 месяцев и получи доступ к стажировке + помощь в трудоустройстве!

Длительность: 7 месяцев""")

@dp.message_handler(text='iOS')
async def ios(message:types.Message):
    await message.answer("""Стань iOS-разработчиком с нуля за 7 месяцев и получи доступ к стажировке + помощь в трудоустройстве!

Длительность: 7 месяцев""")

executor.start_polling(dp)