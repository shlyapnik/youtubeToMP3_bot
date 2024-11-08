from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from states.download import Download
from utils.youtube import download_audio
import os

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот для конвертации YouTube видео в MP3.\n"
        "Отправь мне ссылку на YouTube видео."
    )

@router.message(Command("cancel"))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Операция отменена.")

@router.message(F.text.startswith(("http://", "https://", "www.youtube.com", "youtu.be")))
async def process_youtube_url(message: Message):
    await message.answer("Начинаю загрузку и конвертацию...")
    try:
        file_path, title = await download_audio(message.text, message.from_user.id)
        
        # Создаем FSInputFile для отправки файла
        audio = FSInputFile(file_path)
        
        # Обрезаем название если оно слишком длинное
        if len(title) > 64:
            title = title[:61] + "..."
        
        # Отправляем аудио с заголовком
        await message.answer_audio(
            audio=audio,
            title=title,
            performer="YouTube Audio"
        )
        
        # Удаляем файл после отправки
        if os.path.exists(file_path):
            os.remove(file_path)
            
    except Exception as e:
        await message.answer(f"Произошла ошибка: {str(e)}") 