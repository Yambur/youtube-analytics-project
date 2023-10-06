import os
import json
from googleapiclient.discovery import build
import isodate

class Channel:
    def __init__(self, channel_id: str):
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        def printj(dict_to_print: dict) -> None:
            """Выводит словарь в json-подобном удобном формате с отступами"""
            print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        printj(channel)
