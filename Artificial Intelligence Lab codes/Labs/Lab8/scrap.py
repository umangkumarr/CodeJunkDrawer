

from facebook_scraper import *
import requests
import pandas as pd
import os
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

df = {
    'User ID': [],
    'Name': [],
    'ImageURL': [],
    'DownloadedImageLocation': []
}


def getProfilePicUrl(user_id):
    api_query = urllib.request.urlopen(
        f'https://graph.facebook.com/{user_id}/picture?access_token=EAAgJejQH2wUBAIbcUtBUHZA2ofbNh2NMpCTXd6KktppNE6Cc9TfYXE9mN1DPIfcAwGJT60yXtTJq91JrfjkQKUwP2rVv2u31S8cGCDjuHA6R0safvd7ZB510YfFIYzbvMrbW1LE5NWRdTYpfkm2ks68PeThK8MJZBoMveNTRWQBgK1NleGIwCkpwpJHmxLar5BeZCUgZBk0D8RFDEe9hV')
    return api_query.read()


i = 1

posts = get_posts('groups/613870175328566', locale='en_US', page=2)

for post in posts:
    if i == 20:
        break
    i += 1
    user_id, username = str(post['user_id']), post['username'],
    imag_loc = os.path.join(os.getcwd(), 'Profile Images', user_id + '.jpg')

    pic_data = getProfilePicUrl(user_id)
    f = open(f"{user_id}.jpg", "wb")
    f.write(pic_data)  # save the pic
    f.close()

    prof_pic = f"www.facebook.com/{user_id}"

    df['User ID'].append(user_id)
    df['Name'].append(username)
    df['ImageURL'].append(prof_pic)
    df['DownloadedImageLocation'].append(imag_loc)

pd.DataFrame.from_dict(df).to_csv('data.csv', index=None)
