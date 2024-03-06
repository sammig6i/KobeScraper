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
- Half Shimmy Fadeaway
- Post Move
- Crossover
'''
import openpyxl
import pandas as pd

class VideoData:
  def __init__(self, video_id, upload_date, signature_move, timestamps, game_details, opponent, video_url, duration):
    self.video_id = video_id
    self.upload_date = upload_date
    self.signature_move = signature_move
    self.timestamps = timestamps
    self.game_details = game_details # playoffs, nba finals, or regular season
    self.opponent = opponent
    self.video_url = video_url
    self.duration = duration



