import asyncio
import logging
import os
from datetime import datetime
from pathlib import Path
import json
import requests
from aiogram import types

from images_classes import not_food_dict, eats_classes_dict, beverage_dict
import config
from service.tgbot.code.setup_objects import (
    bot,
    dp,
    # generate_user_image_assesment_keyboard,
    # show_menu_reply
)


# from aiogram.dispatcher.filters import Text
# from aiogram.types.bot_command import BotCommand

# from service.tgbot.code.bot_states import register_handlers_braces
# from service.tgbot.code.setup_objects import db_connection


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
    if response["object_type"] == "food":
        await bot.send_message(
            message.from_user.id,
            f"Думаю, что это {eats_classes_dict[response['class_name']]}",
        )
    elif response["object_type"] == "beverage":
        await bot.send_message(
            message.from_user.id,
            f"Думаю, что это {beverage_dict[response['class_name']]}",
        )
    else:
        await bot.send_message(
            message.from_user.id,
            f"Не похоже на еду. Думаю, что это {not_food_dict[response['class_name']]}",
        )
    requests.post(
        "http://image_uploader:5000/upload_images",
        data={"time": current_time_dttm.strftime(config.TIME_FORMAT),
              "user_id": message.from_user.id},
    )
    # await bot.send_message(
    #     message.from_user.id, text_captions.MESSAGE_BRACES_NOT_FOUND
    # )
    # else:
    #     img = open(request_images_path + "/result.jpg", "rb")
    #     await bot.send_photo(
    #         message.from_user.id,
    #         img,
    #         caption=response.text,
    #     )
    # await bot.send_message(
    #     chat_id=message.from_user.id,
    #     text=text_captions.MESSAGE_ASK_USER_ABOUT_RESULT,
    #     reply_markup=generate_user_image_assesment_keyboard(),
    # )


@dp.message_handler(commands="start")
async def send_start_message(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        "Привет! Я - шазам для еды. Я умею определять 70 видов блюд по фотографии. "
        + "\nОтправь мне фотографию блюда, "
        + "а я определю, какая еда на нам изображена\n"
        + "Также можешь переслать фотографию блюда "
        + "из канала с фотографиями еды: https://t.me/shazam_for_food_examples\n\n"
        + "Давай я попробую угадать, какое блюдо ты мне пришлешь?)",
    )


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(
        "Просто отправь мне фотографию блюда, "
        + "а я определю, какая еда на нам изображена\n"
        + "Также можешь переслать фотографию блюда "
        + "из канала с фотографиями еды: https://t.me/shazam_for_food_examples"
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
