# ONLY WORKS WITH GITHUB OR LESS COMPLICATED SITES THAT DO NOT LOAD JAVASCRIPT
# does NOT work with instagram, youtube, twitch, etc. --> I tried, requires more layers of libraries, effort than just pulling a url from html 



### Concept:
# user inputs any GitHub user's username
# program will return the image link to that GitHub user's profile picture

# requires python libraries: requests and bs4
# requests and bs4 are two popular libraries used in web scraping
# requests = http library that makes http requests "simpler and more human-friendly"
# bs4 = BeautifulSoup --> Python library that parses HTML and XML documents --> named after "tag soup" = documents with non-closed tags that look like a mess of letters, characters
# install with pip
    # pip install requests
    # pip install bs4

import requests
from bs4 import BeautifulSoup as bs     # bs = BeautifulSoup, when you want to use BeautifulSoup replace it with bs for brevity

# github_user variable stores GH username
github_user = input('Input GitHub Username: ')  # prompts user to input a GH username and stores the GH username in variable: github_user ---> in commandline placeholder text = 'Input Github Username: '

# when webscraping first send a REQUEST to the url
# will recieve a RESPONSE from the webpage/url of 200. 200 = request was successful
# when you webscrape, you will recieve a response that will include ALL html code from that webpage ---> GET data

# url variable stores the url of the page you are making a REQUEST to ---> page you want to webscrape
# Make the url DYNAMIC by using concatenation --> combine GH url with variable that stores GH username --> assuming link to a site's user profile ends with the username directory https://github.com/username
url = 'https://github.com/'+github_user     # space not required when concatenating using +
r = requests.get(url)   # sends REQUEST to url stored in variable: url
soup = bs(r.content, 'html.parser') # r.content returns html sourcecode --> ALL .html content from the webpage
                                    # html.parser parses the html sourcecode into readable .html code
    # if you just do bs(r) --> will just return the response (maybe a response code like: 200)
# up to this point: all .html content from the webpage will be saved to variable: soup

# to specifically get profile picture, look for .html <image> tag in html source code
profile_image = soup.find('img', {'alt' : 'Avatar'})['src'] # soup.find() --> from parsed html code, find a specific tag, class, attribute, etc.
# on the web page, right click the image, click inspect, browser console dev tools will show info about the image element
# in GH profile picture --> stored in <img> tag, 
# {'alt' : 'Avatar'} corresponds to alt="avatar" attribute in .html tag
# you want to give soup.find() more info if possible because if you just passed <img> as an argument, there may be more than one <img> tags on the page
# if you just gave soup.find() <img> as an argument, it will return ALL images on the page

# if you print() the profile_image variable WITHOUT ['src'], you will get the wall of text from the dev tools that shows the html code, etc. --> not the actual image
# just want the image link
# ['src'] tells soup.find to GET the src attribute = source link for the image

print(profile_image)
