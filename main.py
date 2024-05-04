import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
# Информация для каждой кнопки
button_info = {
    "1": {"text": "Асылерушка, әрдайым қол ұшын созып, сауапқа молынан кеңеліп, дәл уақытында жанымыздан табылғанына РАХМЕТ❤️\nАлла саған разы болсын!🤲🏻",
          "video_id": "BAACAgIAAxkBAAICOmY2EWy878Y-pPsD38fK45FAz_pnAALeRgACj7mxSQU849tsp80iNAQ"},
    "2": {"text": "Тоооу Ераа, жылатасыың ғооой, қандай жағдай болмасын, әрдайым демеу беріп, ізгі жол көрсетіп, көмегің үшін РАХМЕТ❤️\nАлла саған разы болсын!🤲🏻",
          "video_id": "BAACAgIAAxkBAAIBy2Y1_82DHYByHBsGkd9VqUZWU-o1AAKnQAACjW2wSV_F7_5Tk-VbNAQ"},
    "3": {"text": "Мақыыыс, әрдайым біз үшін алаңдап, қамқор көрсетіп, көңіл-күйімізді көтеретініне РАХМЕТ❤️\nАлла саған разы болсын!🤲🏻",
          "video_id": "BAACAgIAAxkBAAICzGY2Mc0aDGESV_JUbkd2-VxSKeBMAALeRgACRWewSeZW-ZSDLdC4NAQ"},
    "4": {"text": "Рикоооооо, театр әлемін көрсетіп, эмоция сыйлап, әрдайым жүзіңнен шуақ шашып жүретініне РАХМЕТ❤️\nАлла саған разы болсын! 🤲🏻",
          "video_id": "BAACAgIAAxkBAAIBHmY0zOwIhibybPPq4bftWgkSN6OxAAKkSQACaxChSTmLEH7rcbKJNAQ"},
    "5": {"text": "Нұрболушкаа, аяғымызды жерге тигізбей, көңілімізге қаяу түсірмей, шынайы достықты түсіндіргеніне РАХМЕТ❤️\nАлла саған разы болсын!🤲🏻",
          "video_id": "BAACAgIAAxkBAAIBymY1_8ZvC9_tmxx_8zoWfH__cJg3AAKTQwADY7FJNtih7cqYdpE0BA"},
    "6": {"text": "Бекнұрджоонии, оой харизманың түбін түсіретін, қылықтарыңмен баурап алып, әрдайым позитив сыйлайтыныңа РАХМЕТ❤️\nАлла саған разы болсын!🤲🏻",
          "video_id": "BAACAgIAAxkBAAIBtWY09MfiqEY_V3OTTZPwWthaKk4_AAKySAACfYeoSWXxDkM17YhvNAQ"},
    "7": {"text": "Қасымушкаа, түр жинап алады өзіі, ұстамды мінезіңмен приколдарын өткізіп жібереді өзіі, бізді сыйлап, құрмет көрсететініңе РАХМЕТ❤️\nАлла саған разы болсын!🤲🏻 ",
          "video_id": "BAACAgIAAxkBAAIBKmY0zWt0gux3pXPBY1RJFGFMA2XmAAIXSgACqgypSXqLIzhClOnoNAQ"},

}

phone_number = {
    "6": "77479706702",
    "1": "77477400622",
    "2": "77082114526",
    "7": "77076032405",
    "3": "77083247865",
    "4": "77064283685",
    "5": "77774393864",
}
# phone_number = {
#     "6": "77781728073",
#     "1": "77751780599",
#     "2": "77474914763",
#     "7": "77761827619",
#     "3": "77766079387",
#     "4": "77064283685",
#     "5": "77774393864",
# }


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Сәлемушка, {html.bold(message.from_user.full_name)}❤️ Біз сендерді келе жатқан Отан "
                         f"Қорғаушылар мерекесімен құттықтаймыз! Қыздарлардың атынан  шақыртуымызды қабыл алыңдар🤭🫶🏽",
                         reply_markup=reply_keyboard())
    await message.answer_sticker("CAACAgEAAxkBAAEFKAZmNMYMdZOyWMwl8l0EdSMAASwpQd8AArsDAALLbKFFYgoSwcOUPRo0BA")


def reply_keyboard():
    # Создаем кнопку
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton(text='Қарындас, нөмеріңізді болады ма?😏', request_contact=True)
    ]])
    return keyboard


def reply_seven_keyboard():
    # Создаем кнопку
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='Асылер', callback_data="chosen:1"),
         KeyboardButton(text='Ернар', callback_data="chosen:2")],
        [KeyboardButton(text='Мақсат', callback_data="chosen:3"),
         KeyboardButton(text='Ринат', callback_data="chosen:4")],
        [KeyboardButton(text='Нұрбол', callback_data="chosen:5"),
         KeyboardButton(text='Бекнұр', callback_data="chosen:6")],
        [KeyboardButton(text='Қасымжомарт', callback_data="chosen:7")]
    ])
    return keyboard


def reply_bool_keyboard():
    # Создаем кнопку
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[
        [InlineKeyboardButton(text='Иа ✅', callback_data="check:yes")],
        [InlineKeyboardButton(text='Жоқ ❌', callback_data="check:no")],

    ])
    return keyboard


@dp.callback_query(F.data.startswith("check:"))
async def check_handler(callback: CallbackQuery):
    _, check = callback.data.split(":")
    print(callback.data)
    if check == 'yes':
        await callback.message.answer("Кереметушка🥹 Онда осы мерекеге орай сіздерді ұмытылмас сәттерге толы күнді Қыздарлармен өткізуге шақырамыз🫶🏽", reply_markup=None)
        await callback.message.answer_sticker('CAACAgUAAxkBAAEFLYxmNguJlirJEn_Jek__OmzeTMJGugACzAAD1F7mNny7ON8pE9OpNAQ')
        await callback.message.answer(
            "Күні: 07.05.2024\nУақыты: 14:00\nДресс-код: Ыңғайлы киініңіздер\nЖақсы көңіл-күй мен ұйқыларынды қандырып келіндер 🤗💐\nКЕШІКПЕЙ КЕЛЕМІЗ‼️👊🏿 ",
            reply_markup=None)
        await callback.message.answer("Мекен-жайы: https://2gis.kz/astana/geo/70000001029853986", reply_markup=None)
        await callback.message.answer(
            "Это только начало нашего дня!", reply_markup=None)
        await callback.message.answer_sticker(
            "CAACAgEAAxkBAAEFKAhmNMYR5MPxQgd1ROGi5hAbqzCWqAACtwMAAjiFqUWaw6qzljavKTQE")
    elif check == 'no':
        await callback.message.answer("Сөйттін ғооой даааа", reply_markup=None)
        await callback.message.answer_sticker(
            "CAACAgUAAxkBAAEFKqNmNTXg0k32Tp0bqlpSa5FRBqbungACEwEAAtRe5jYjPZWnnjeFOjQE")


@dp.callback_query(F.data.startswith("chosen:"))
async def cb_handler(callback: CallbackQuery):
    _, number = callback.data.split(":")
    info = button_info[number]
    await callback.message.answer_video(info["video_id"])

    # text = await callback.message.answer(text="Файл жүктеліп жатыр күте тұр")
    # await callback.message.answer_video(FSInputFile(info["video_id"]), caption=info["text"])
    # await text.edit_text("Файл сәтті жүктелді")


@dp.message()
async def handle_message(message: Message):
    if message.text == 'Ринат':
        await message.answer_video("BAACAgIAAxkBAAIBHmY0zOwIhibybPPq4bftWgkSN6OxAAKkSQACaxChSTmLEH7rcbKJNAQ")
        await message.answer("Рикоооооо, театр әлемін көрсетіп, эмоция сыйлап, әрдайым жүзіңнен шуақ шашып жүретініне РАХМЕТ❤️\nАлла саған разы болсын! 🤲🏻")
    if message.text == 'Қасымжомарт':
        await message.answer_video("BAACAgIAAxkBAAIBKmY0zWt0gux3pXPBY1RJFGFMA2XmAAIXSgACqgypSXqLIzhClOnoNAQ")
        await message.answer("Қасымушкаа, түр жинап алады өзіі, ұстамды мінезіңмен приколдарын өткізіп жібереді өзіі, бізді сыйлап, құрмет көрсететініңе РАХМЕТ❤️\n Алла саған разы болсын!🤲🏻 ")
    if message.text == 'Асылер':
        await message.answer_video("BAACAgIAAxkBAAICOmY2EWy878Y-pPsD38fK45FAz_pnAALeRgACj7mxSQU849tsp80iNAQ")
        await message.answer("Асылерушка, әрдайым қол ұшын созып, сауапқа молынан кеңеліп, дәл уақытында жанымыздан табылғанына РАХМЕТ❤️\nАлла саған разы болсын!🤲🏻")
    if message.text == 'Ернар':
        await message.answer_video("BAACAgIAAxkBAAIBy2Y1_82DHYByHBsGkd9VqUZWU-o1AAKnQAACjW2wSV_F7_5Tk-VbNAQ")
        await message.answer("Тоооу Ераа, жылатасыың ғооой, қандай жағдай болмасын, әрдайым демеу беріп, ізгі жол көрсетіп, көмегің үшін РАХМЕТ❤️\nАлла саған разы болсын!🤲🏻")
    if message.text == 'Мақсат':
        await message.answer_video("BAACAgIAAxkBAAICzGY2Mc0aDGESV_JUbkd2-VxSKeBMAALeRgACRWewSeZW-ZSDLdC4NAQ")
        await message.answer("Мақыыыс, әрдайым біз үшін алаңдап, қамқор көрсетіп, көңіл-күйімізді көтеретініне РАХМЕТ❤️\nАлла саған разы болсын!🤲🏻")
    if message.text == 'Нұрбол':
        await message.answer_video("BAACAgIAAxkBAAIBymY1_8ZvC9_tmxx_8zoWfH__cJg3AAKTQwADY7FJNtih7cqYdpE0BA")
        await message.answer("Нұрболушкаа, аяғымызды жерге тигізбей, көңілімізге қаяу түсірмей, шынайы достықты түсіндіргеніне РАХМЕТ❤️\nАлла саған разы болсын!🤲🏻")
    if message.text == 'Бекнұр':
        await message.answer_video("BAACAgIAAxkBAAIBtWY09MfiqEY_V3OTTZPwWthaKk4_AAKySAACfYeoSWXxDkM17YhvNAQ")
        await message.answer("Бекнұрджоонии, оой харизманың түбін түсіретін, қылықтарыңмен баурап алып, әрдайым позитив сыйлайтыныңа РАХМЕТ❤️\nАлла саған разы болсын!🤲🏻")


    if message.video:
        video_file_id = message.video.file_id
        print("File ID of the video:", video_file_id)
    if message.contact:
        print('------------------------------', message.contact.phone_number)

        for i in range(1, 8):
            print('-------------------------------------',message.contact.phone_number ==phone_number.get(str(i)))
            if message.contact.phone_number == phone_number.get(str(i))\
                    or message.contact.phone_number == f"+{phone_number.get(str(i))}":
                video_id = button_info.get(str(i)).get('video_id')
                print('--------------------------', video_id)
                await message.answer_video(video_id)
                text = button_info.get(str(i)).get('text')
                await message.answer(text, reply_markup=ReplyKeyboardRemove())
                await message.answer("7 май күні бос боласыз ба?", reply_markup=reply_bool_keyboard())
                await message.answer_sticker(
                    "CAACAgQAAxkBAAEFKp9mNTXDA9B2UYoQxDBX_15_yApr_AACNAADX8YBGRmx5VMuZAtJNAQ",
                    reply_markup=reply_seven_keyboard())


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
