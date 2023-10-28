from googleapiclient.discovery import build
import os


class Video:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.video_id = video_id
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()

        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        self.comment_count: int = video_response['items'][0]['statistics']['commentCount']

    def __str__(self):
        return self.video_title



class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id











"""class Video(Channel):
    def __init__(self, video_id):
        youtube = super().get_service()
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.video_response = video_response
        self.__video_id = video_id
        self.url = f'https://youtu.be/{self.video_id}'
        try:
            self.title = video_response['items'][0]['snippet']['title']
            self.description = video_response['items'][0]['snippet']['description']
            self.like_count = video_response['items'][0]['statistics']['likeCount']
            self.view = video_response['items'][0]['statistics']['viewCount']
        except IndexError:
            self.title = None
            self.description = None
            self.like_count = None
            self.view = None

    def __str__(self):
        return f"{self.title}"

    @property
    def video_id(self):
        return self.__video_id


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        youtube = super().get_service()
        playlist_videos = youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails, snippet',
                                                       maxResults=50,
                                                       ).execute()
        self.playlist_id = [video['contentDetails']['videoId'] for video in playlist_videos['items']]"""
