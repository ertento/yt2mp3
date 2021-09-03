from __future__ import unicode_literals
import youtube_dl
import sys
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

verbose = False;
nopl = False;

def is_supported(url):
        extractors = youtube_dl.extractor.gen_extractors()
        for e in extractors:
            if e.suitable(url) and e.IE_NAME != 'generic':
                return True
        return False

class MyLogger(object):
    def debug(self, msg):
        if verbose == True:
            print(msg)
        else:
            pass

    def warning(self, msg):
        if verbose == True:
            print(msg)
        else:
            pass

    def error(self, msg):
        if verbose == True:
            print(msg)
        else:
            pass

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }],
                'logger': MyLogger(), 'progress_hooks': [my_hook],
                'noplaylist' : False,
                'quiet' : False,
                'o' : '~/Desktop/%(title)s.%(ext)s',
            }
def printWelcome():
    print(
    "+----------------------------------------------------------+"+ 
    "\n+              W   E   L   C   O   M   E   I N             +"+
    "\n+              Y   T   2   M   P   3   v0.2          2021  +"+
    "\n+----------------------------------------------------------+") 
    
while(True):
    clearConsole()
    printWelcome()
    text = " Q. Leave \n 1. Set verbosity (now "
    if verbose == True:
        text += "verbose mode"
    else:
        text += "quiet mode"
    text = text + ") \n 2. Set single video or playlist download mode (now "
    if nopl == True :
        text += "Single video download mode)"
    else:
        text += " Playlist download mode)"
    text += "\n D. to download \n H. for help\n"
    print(text)
    
    link = input ("")
    if link == "1":
        verbose = not verbose
        ydl_opts["verbose"] = verbose
        input("Verbosity changed! Press any key to continue \n")
        continue
    elif link == "2":
        nopl = not nopl
        ydl_opts["noplaylist"]= nopl 
        input("Download mode changed! Press any key to continue \n")
        continue
    elif link == "h" or link == "H" or link == "help" or link == "HELP":
        clearConsole()
        printWelcome()
        help = ("""\n
        Press 1 and then enter to switch between verbosity or quit mode 
        (verbosity mode print some additional info). Press 2 and then 
        enter to switch between single or playlist mode. Playlist mode 
        is able to download not only the video in the given link, 
        but also all the videos contained in the same playlist. 
        Press Q to leave or D to continue the download.\n""")
        print(help)
        input("Press any key to continue...")
        continue
    elif link == "d" or link == "D" or link =="download" or link == "DOWNLOAD": 
        print("\nInsert link: \n")
        link = input ("")
        if not is_supported(link):
            input("\n Invalid link! Press any key to continue\n")
        else:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            input("\n All done. Press any key to continue")

    elif link == "q" or link == "Q" or link == "quit" or link == "quit()" or link == "QUIT":
        sys.exit(0)
    else: 
        input("Invalid command! Press any key to continue")
        continue
    
   
