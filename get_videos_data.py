import pickle
from apiclient.discovery import build
import pandas as pd

members = pd.read_csv("data/hololiver_url.csv", encoding="utf_8", delimiter=',')
YOUTUBE_API_KEY = 
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
#
# for member in members.iterrows():
#     search_response = youtube.search().list(
#         part='snippet',
#         channelId=member[1]["url"][32:],
#         publishedAfter='2020-06-01T00:00:00Z',
#         publishedBefore='2020-08-13T00:00:00Z',
#         maxResults=50,
#         order='date',
#         type='video',
#         ).execute()
#
#     with open('data/videos/20200601_20200813_50/' + str(member[1]["id"]) + '.pkl', 'wb') as web:
#         pickle.dump(search_response, web)
