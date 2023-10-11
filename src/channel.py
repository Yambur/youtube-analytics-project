import os
import json
from googleapiclient.discovery import build


class Channel:
    def __init__(self, channel_id: str):
        youtube = self.get_service()
        ch = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__channel_id = channel_id
        self.title = ch['items'][0]['snippet']['title']
        self.description = ch['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.subscribers = ch['items'][0]['statistics']['subscriberCount']
        self.video_count = ch['items'][0]['statistics']['videoCount']
        self.view = ch['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале в json-подобном удобном формате с отступами"""
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API."""
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename):
        """Сохраняет значения атрибутов экземпляра Channel в JSON-файл."""
        channel_data = {
            "channel_id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscribers_count": self.subscribers,
            "video_count": self.video_count,
            "total_views": self.view
        }
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(channel_data, json_file, indent=2, ensure_ascii=False)

