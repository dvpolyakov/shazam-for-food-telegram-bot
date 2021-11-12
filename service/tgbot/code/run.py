import asyncio
import logging
import os
from datetime import datetime
from pathlib import Path
import json
import requests
from aiogram import types

from images_classes import class_name_to_class_dict
import config
from service.tgbot.code.setup_objects import (
    bot,
    dp,
    # generate_user_image_assesment_keyboard,
    # show_menu_reply
)
import service.tgbot.code.messages_text as messages_text

# from aiogram.dispatcher.filters import Text
# from aiogram.types.bot_command import BotCommand

# from service.tgbot.code.bot_states import register_handlers_braces
# from service.tgbot.code.setup_objects import db_connection


def format_classes_probas(classes_probas, classes_names):
    formatted_msg = "\n"
    for class_en_name, proba in classes_probas.items():
        formatted_msg += (
            classes_names[class_en_name] + " на " + str(proba) + "%\n"
        )
    return formatted_msg


async def reply_to_user(message, response):
    await bot.send_message(
        message.from_user.id,
        "Думаю, что это "
        + format_classes_probas(
            response["classes_probas"],
            class_name_to_class_dict[response["object_type"]],
        ),
    )


@dp.message_handler(content_types=["photo"])
async def handle_photo(message: types.Message):
    current_time_dttm = datetime.now()
    request_images_path = os.path.join(
        config.images_path, current_time_dttm.strftime(config.TIME_FORMAT)
    )
    Path(request_images_path).mkdir(parents=True, exist_ok=True)

    await message.photo[-1].download(
        os.path.join(request_images_path, "input.jpg")
    )

    await message.answer("Определяю еду на фото")
    response = requests.post(
        "http://image_handler:5000/return_message",
        data={"time": current_time_dttm.strftime(config.TIME_FORMAT)},
    )

    response = json.loads(response.text)
    await reply_to_user(message, response)
    requests.post(
        "http://image_uploader:5000/upload_images",
        data={
            "time": current_time_dttm.strftime(config.TIME_FORMAT),
            "user_id": message.from_user.id,
        },
    )
    # await bot.send_message(
    #     chat_id=message.from_user.id,
    #     text=text_captions.MESSAGE_ASK_USER_ABOUT_RESULT,
    #     reply_markup=generate_user_image_assesment_keyboard(),
    # )


@dp.message_handler(commands="start")
async def send_start_message(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        messages_text.BOT_DESCRIPTION_MESSAGE
        + messages_text.STANDARD_ANSWER
        + " "
        + messages_text.CHALLENGE_MESSAGE,
    )


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(
        messages_text.STANDARD_ANSWER + messages_text.CHALLENGE_MESSAGE
    )


async def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Регистрация хэндлеров
    # register_handlers_braces(dp)

    # Установка команд бота
    # await set_commands(bot)

    await dp.skip_updates()
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
