import pickle
from apiclient.discovery import build
import pandas as pd
import pprint

members = pd.read_csv("data/hololiver_url.csv", header=True, encoding="utf_8", delimiter=',')
YOUTUBE_API_KEY = 
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# for member in members.iterrows():
#     with open('data/videos/20200601_20200813_50/' + str(member[1]["id"]) + '.pkl', 'rb') as web:
#         videos_data = pickle.load(web)
#
#     data_list = []
#     for video_data in videos_data['items']:
#         search_response = youtube.videos().list(
#             part='snippet',
#             id=video_data['id']['videoId'],
#             ).execute()
#
#         data_list.append(search_response)
#
#     with open('data/video/20200601_20200813_50/' + str(member[1]["id"]) + '.pkl', 'wb') as web:
#         pickle.dump(data_list, web)
