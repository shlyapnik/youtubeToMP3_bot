import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path

async def download_audio(url: str, user_id: int) -> tuple[str, str]:
    try:
        # Инициализируем YouTube объект
        yt = YouTube(
            url,
            on_progress_callback=on_progress
        )
        
        print(f"Название: {yt.title}")
        
        # Получаем аудио поток
        audio = yt.streams.get_audio_only()
        if not audio:
            raise Exception("Не удалось найти аудиопоток")
            
        # Создаем директорию для загрузок
        download_path = Path("downloads") / str(user_id)
        download_path.mkdir(parents=True, exist_ok=True)
        
        # Скачиваем файл сразу в MP3
        out_file = audio.download(
            output_path=str(download_path),
            mp3=True  # Автоматическая конвертация в MP3
        )
        
        return out_file, yt.title
        
    except Exception as e:
        raise Exception(f"Ошибка при скачивании: {str(e)}")