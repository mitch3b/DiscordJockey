import time
import requests

from config import config
from musicbot.songinfo import Songinfo

webhookUrl = 'https://discordapp.com/api/webhooks/750859224925470851/78hc0723-lepDjtAovqcTlJXWcXNL2vlTOjl8QnwOC611v2kZwJ8EaBbbMpcOE07iYlO'

def post(content):
    print("Posting this to discord: " + content)

    myobj = {'content': content}

    x = requests.post(webhookUrl, data = myobj)

    if x.status_code != 204 and x.status_code != 200:
        raise Exception("Failed to post with code {} to discord. Content: {}".format(x.status_code, content))
        
async def startSongChat(trackNum, songInfo):
    post("Playing track " + str(trackNum) + "/60: " + songInfo.title);
    time.sleep(config.MAX_SONG_DURATION/2);
    post("Half way done!");
    
    if config.MAX_SONG_DURATION > 15:
      time.sleep(config.MAX_SONG_DURATION/2 - 10);
      post("Ten seconds left!");

