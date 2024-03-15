'''
Kobe Bryant Signature Move Dataset
compile list of Kobe Bryant signature moves
find videos for each signature move
'''
from datetime import datetime
import pandas as pd
import os
from dotenv import load_dotenv
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from pprint import pprint

# ! fix scraper to pull and add new videos to spreadsheets
# TODO later collect data on clutch shots to add to MVP

load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_video(payer_name, signature_move):
    search_query = f'{payer_name} {signature_move} game highlights'

    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)

    request = youtube.search().list(
        part="id,snippet",
        type="video",
        q=search_query,
        videoDefinition='any',
        maxResults=1
    )

    videos_dict = []
    try:
        response = request.execute()
        if not response:
            print("No response received.")
        else:
            for item in response.get("items", []):
               video_id = item.get("id", {}).get("videoId")
               upload_date = (item.get("snippet", {}).get("publishTime"))
               video_url = f'https://www.youtube.com/watch?v={video_id}'

               if video_id and upload_date:
                    parsed_datetime = datetime.fromisoformat(upload_date).strftime("%Y-%m-%d %H:%M:%S %z")
                    video_info = {"video_id": video_id,
                                  "upload_date": parsed_datetime,
                                  "video_url": video_url}
                    videos_dict.append(video_info)
                    
    except Exception as err:
        print(f"An error ocurred: {err}")
    
    return videos_dict

def save_video(videos):
    columns = ['video_id', 'upload_date', 'video_url']
    df = pd.DataFrame(videos)
    with pd.ExcelWriter("kobe_videos_copy.xlsx", mode='a') as writer:
        df.to_excel(writer, "kobe_videos_copy.xlsx", columns=columns)


existing_videos = pd.read_excel("kobe_videos_copy.xlsx")
existing_videos_ids = set(existing_videos["video_id"])

all_videos = []
signature_moves = ["fadeaway", "3 pointer", "dunk", "layup", "post move", "crossover"]
for sig in signature_moves:
    new_videos = get_video("kobe bryant", sig)
    unique_new_videos = [video for video in new_videos if video["video_id"] not in existing_videos_ids]
    all_videos.extend(unique_new_videos)
    

save_video(all_videos)





