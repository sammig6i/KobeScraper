'''
Kobr Bryant Signature Move Dataset
compile list of Kobe Bryant signature moves
find videos for each signature move

Signature Shot Moves:
- Fadeaway
- 3 Pointer
- Dunk
- Layup
- Clutch Shot
- Turnaround Fadeaway
- Post Move
- Crossover
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
    self.signature_move = signature_move
    self.timestamps = timestamps # start and end time
    self.game_details = game_details # playoffs, nba finals, or regular season
    self.opponent = opponent # opposing team
    self.video_url = video_url # https://www.youtube.com/watch?v={videoID}
    self.duration = duration # duration of clip 

  def get_video(self, request):
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

      return response





