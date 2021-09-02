from __future__ import unicode_literals
import youtube_dl
import keyboard
import sys
print("Insert: \n 1)Playlist \n 2)Single video \n q for exit")
link = input ("")

if link == "1":
    ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'noplaylist': True,
            
        }
elif link == "2":
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
elif link == "q" or "Q":
    print("Leaving")
    sys.exit(0)
print("Insert link")
link = input ("")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
