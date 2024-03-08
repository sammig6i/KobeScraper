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

kobe_sig_moves = ["Fadeaway",
                  "3 Pointer",
                  "Dunk",
                  "Layup",
                  "Clutch Shot",
                  "Turnaround Fadeaway",
                  "Post Move",
                  "Crossover"
                  ]

class VideoData:
  def __init__(self, video_id, upload_date, signature_move, timestamps, game_details, opponent, video_url, duration):
    self.video_id = video_id
    self.upload_date = upload_date
    self.signature_move = signature_move # to be labelled
    self.timestamps = timestamps # start and end time, to be labelled
    self.game_details = game_details # playoffs, nba finals, or regular season, to be labelled
    self.opponent = opponent # opposing team, to be labelled
    self.video_url = video_url # https://www.youtube.com/watch?v={videoID}
    self.duration = duration # duration of clip, to be labelled

def get_video(request):
    api_service_name = "youtube"
    api_version = "v3"
    # Get credentials and create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)

    request = youtube.search().list(
        part="id,snippet",
        type="video",
        q=request,
        videoDefinition='any',
        maxResults=1
    )

    response = request.execute()
    # TODO: for each signature move, request videos and save to excel spreadsheet then label
    data = response["items"][0]
    video_id = data["id"]["videoId"]
    upload_date = data["snippet"]["publishTime"]
    video_url = f'https://www.youtube.com/watch?v={video_id}'
    print(video_id, upload_date, video_url)

req = "Kobe Bryant Fadeaway"
get_video(req)




