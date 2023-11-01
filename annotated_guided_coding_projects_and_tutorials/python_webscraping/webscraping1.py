### Concept:
# user inputs any Instagram user's username
# program will return the image link to that Instagram user's profile picture
# pip install selenium --> selenium web driver to run JavaScript
import selenium.webdriver as webdriver

import requests
from bs4 import BeautifulSoup as bs     # bs = BeautifulSoup, when you want to use BeautifulSoup replace it with bs for brevity

# yt_user variable stores YouTube username
#twitch_user = input('Input Twitch username: ')  # prompts user to input a YT username and stores the YT username in variable: yt_user ---> in commandline placeholder text = 'Input Github Username: '


#url = 'https://twitch.tv/'+twitch_user    
#r = requests.get(url)   # sends REQUEST to url stored in variable: url
#soup = bs(r.content, 'html.parser') # r.content returns html sourcecode --> ALL .html content from the webpage

# DOES NOT WORK WITH INSTAGRAM, requires webdriver to load JavaScript, etc.

#profile_image = soup.find('src')

#print(profile_image)

instagram_user = input('Input Instagram username: ')

url = 'http://instagram.com/'+instagram_user
driver = webdriver.Firefox()
driver.get(url)

soup = bs(driver.page_source)

for x in soup.findAll('li', {'class':'photo'}):
    print(x)
