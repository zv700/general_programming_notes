# DOES NOT WORK WITH YOUTUBE, requires webdriver to load JavaScript, etc.


### Concept:
# user inputs any YouTube user's username
# program will return the image link to that YouTube user's profile picture

import requests
from bs4 import BeautifulSoup as bs     # bs = BeautifulSoup, when you want to use BeautifulSoup replace it with bs for brevity

# yt_user variable stores YouTube username
yt_user = input('Input YouTube @Username: ')  # prompts user to input a YT username and stores the YT username in variable: yt_user ---> in commandline placeholder text = 'Input Github Username: '


url = 'https://youtube.com/'+yt_user    
r = requests.get(url)   # sends REQUEST to url stored in variable: url
soup = bs(r.content, 'html.parser') # r.content returns html sourcecode --> ALL .html content from the webpage

profile_image = soup.find('img', {'alt' : 'Avatar'})['src'] # soup.find() --> from parsed html code, find a specific tag, class, attribute, etc.

print(profile_image)
