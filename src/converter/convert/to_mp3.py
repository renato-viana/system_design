import pika, json, tempfile, os
from bson.objectid import ObjectIdimport 
import moviepy.editor

def start(message, fs_videos, fs_mp3s, channel):
    message = json.loads(message)
    
    # empty0 temp file
    tf = tempfile.NamedTemporaryFile()
    # video contents
    out = fs_videos.get(ObjectId(message["video_fid"]))
    