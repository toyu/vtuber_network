import pickle
import numpy as np
import pandas as pd

members = pd.read_csv("data/hololiver_url.csv", encoding="utf_8")

am = np.zeros((27, 27))

for i, member in enumerate(members.iterrows()):
    with open('data/video/20200601_20200813_50/' + str(member[1]["id"]) + '.pkl', 'rb') as web:
        data = pickle.load(web)

    for video_data in data:
        for j, other_member in enumerate(members.iterrows()):
            if i == j:
                continue

            if video_data['items'][0]['snippet']['description'].find(other_member[1]["url"]) >= 0:
                am[i][j] += 1

print(am[14][13])
am = am+am.T
np.savetxt('data/am.csv', am, delimiter=',')
print(am)