from pytube import YouTube
from sys import argv

# Instructions: Run ytdownl.py in commandline
    # format: ytdownl.py "https://youtube.com/desiredVideoLink"
    # if input within commandline is a Python list [], then:
        # program name will always be in position 0 -> [0, 1]    
        # Desired YouTube video's url is argument in position 1 -> [0, 1]
link = argv[1]

# Access YouTube video by passing video url through YouTube object
# Store YouTube video within yt variable
yt = YouTube(link)

# Print video info in console
print("Title: ", yt.title)

print("Video author: ", yt.author)

print("Publish date: ", yt.publish_date)

print("Views: ", yt.views)

print("Video length: ", yt.length) # video length measured in seconds

# Download highest resolution of video
yd = yt.streams.get_highest_resolution()
#yt.bypass_age_gate()

# Choose path to save video locally
yd.download('/Users/zvque/Videos/ytdownl')

