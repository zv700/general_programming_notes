# from: https://www.youtube.com/watch?v=vEQ8CXFWLZU
# "3 PYTHON AUTOMATION PROJECTS FOR BEGINNERS" by Internet Made Coder

# requires pytube installed -> pip install pytube
    # pytube is a Python library that lets you manipulate content/data specifically from YouTube
# note: YouTube spelling is case sensitive -> Y T

from pytube import YouTube
from sys import argv


### To get this program to work:
# from commandline run: programName "Youtube video url"
# from commandline run: ytdownl.py "https://yourYoutubeVideoLink.com"
# argv treats the command/argument run from commandline as a python list
# argv allows you to access the url link within commandline
# input the program name followed by arguments -> link

link = argv[1]
# "link = argv[1]" says the url link will be in the [0, 1] number 1 position of list
# "access using first commandline argument" if list position: 0 will always be the name of the program

yt = YouTube(link)
# yt object contains YouTube url link "create this YouTube object from this link [and store it within variable: yt]"

print("Title: ", yt.title)

print("Video author: ", yt.author)

print("Publish date: ", yt.publish_date)

print("Views: ", yt.views)

print("Video length: ", yt.length) # video length measured in seconds

### Tested properties that do not provide useful info
    #print("Video author's channel id: ", yt.channel_id) # works, but not sure where info is used. Url ending at the YouTube channel is the person's @userName and not the channel id

    #print("Video description: ", yt.description) # returns "None" despite videos having descriptions?

    #print("Keywords: ", yt.keywords) # returns an empty python list []

    #print("Video info: ", yt.vid_info) -> video info = a large body of text and numbers not made for human reading


# have the program print info about the YouTube link to make sure the program works properly, 
    # to make sure program was able to reach the correct link or any YouTube link at all
# ".title" and ".views" are properties of YouTube videos imported/accessable through "from pytube import YouTube"
# list of available properties of YouTube() object available at pytube.io -> pytube documentation


##### Actually download the YT video
yd = yt.streams.get_highest_resolution()
# specify to download/GET request the highest resolution version of video because when you play a YT video, each quality/resolution is its own stream

yd.download('/Users/zvque/Videos/ytdownl')
# input path the folder where the video will be saved locally