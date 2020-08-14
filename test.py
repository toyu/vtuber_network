# import csv
# import pandas as pd
import pickle
import pprint
#
# df = pd.read_csv("data/hololiver_url.csv", encoding="utf_8")
#
# for data in df.iterrows():
#     print(data[1]["url"])
#     break

# print(len("https://www.youtube.com/channel/"))

with open('data/video/20200601_20200813_50/27.pkl', 'rb') as web:
    data = pickle.load(web)
    print(len(data))
    pprint.pprint(data[0]['items'][0]['snippet']['description'])
