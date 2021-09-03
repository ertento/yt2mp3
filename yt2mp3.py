from __future__ import unicode_literals
import youtube_dl
import sys
while(True):
    print("Insert: \n 1)for Playlist \n 2)for single video \n q for leave")
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
    else:
        print("Leaving")
        sys.exit(0)
    def is_supported(url):
        extractors = youtube_dl.extractor.gen_extractors()
        for e in extractors:
            if e.suitable(url) and e.IE_NAME != 'generic':
                return True
        return False
    print("Insert link")
    link = input ("")
    if not is_supported(link):
        print("Invalid link")
    else:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
