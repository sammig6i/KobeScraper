'''
Kobe Bryant Signature Move Dataset
compile list of Kobe Bryant signature moves
find videos for each signature move
'''
import openpyxl
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
  def __init__(self, video_id, upload_date, video_url, duration):
    self.video_id = video_id
    self.upload_date = upload_date
    self.video_url = video_url # https://www.youtube.com/watch?v={videoID}
    # self.signature_move = signature_move # to be labelled
    # self.timestamps = timestamps # start and end time, to be labelled
    # self.game_details = game_details # playoffs, nba finals, or regular season, to be labelled
    # self.opponent = opponent # opposing team, to be labelled
    # self.duration = duration # duration of clip, to be labelled

plaery_name = "Kobe Bryant"
signature_moves = ["Fadeaway", "3 Pointer", "Dunk", "Layup", "Clutch Shot", "Turnaround Fadeaway", "Post Move", "Crossover"]

def get_video(payer_name, signature_move):
    search_query = f'{payer_name} {signature_move} highlights'

    youtube = googleapiclient.discovery.build(
        api_service_name="youtube", api_version="v3", developerKey=API_KEY)

    request = youtube.search().list(
        part="id,snippet",
        type="video",
        q=search_query,
        videoDefinition='any',
        maxResults=1
    )

    try:
    response = request.execute()
    data = response["items"][0]
    video_id = data["id"]["videoId"]
    upload_date = data["snippet"]["publishTime"]
    video_url = f'https://www.youtube.com/watch?v={video_id}'

    except:
    

    video = VideoData(video_id, upload_date, video_url)
    
    return video





req = "Kobe Bryant Fadeaway"
get_video(req)




