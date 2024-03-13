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



load_dotenv()
API_KEY = os.getenv('API_KEY')

class VideoData:
  def __init__(self, video_id, upload_date, video_url):
    self.video_id = video_id
    self.upload_date = upload_date
    self.video_url = video_url # https://www.youtube.com/watch?v={videoID}
    # self.signature_move = signature_move # to be labelled
    # self.timestamps = timestamps # start and end time, to be labelled
    # self.game_details = game_details # playoffs, nba finals, or regular season, to be labelled
    # self.opponent = opponent # opposing team, to be labelled
    # self.duration = duration # duration of clip, to be labelled


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
        maxResults=6
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
    df = pd.DataFrame(videos)
    df.rename_axis('ID', inplace=True)
    df.to_excel("kobe_videos.xlsx")

   
signature_moves = ["fadeaway", "3 pointer", "dunk", "layup", "clutch shot", "post move", "crossover"]
all_videos = []
for sig in signature_moves:
    videos = get_video("kobe bryant", sig)
    all_videos.extend(videos)
    

save_video(all_videos)





