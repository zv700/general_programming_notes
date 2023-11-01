# Singe-Page Applications

- using JavaScript can create an entire page that is one page
- use JavaScript to manipulate the DOM -> make changes to just that one page

## Advantages of single page web app:
- if you have multiple pages with a similar layout, instead of loading an entirely new page, ONLY load the parts of the page that are different/change -> good for applications that change frequently


## example: a single page application that displays 3 different pages using only one page (changes to one page via JavaScript)

- *see Lecture 6 folder -> code\CS50\Lecture 6\singlepage.html (something like that)*

9:41:51

- fetch requests additional information from a web server, use fetched data to fill in info on a page

### Load content dynamically:
- if single page application has multiple pages, but user might not realistically need to view every single page, can have page only fetch (from own web server) the needed content

9:41:24

- can be inefficient to load all data at once in html and showing/hiding when needed
- might be loading more info than the user will ever use/need [might only need to view page 1, but not page 2 or 3]

Load content for single page app dynamically

-fetch from own server only the parts of the page that need to change, use that fetched data to replace only the needed parts
- JavaScript for client side
- Django for web server

9:46:45

### Disadvantage to single page url: -> avoid by use JavaScript history api to change url
- url does not reflect specific page you are on within site structure [example.com/1 if you are on section 1, example.com/2 if you are on section 2]

JavaScript history api:
- push changes to JavaScript history api = update url, saves data to users' browser history so they can go back to page

### Advantages of single page app:
- if page has a lot of elements changing at the same time [like a social media page where posts, likes, etc. change in real time] it's more efficient to change out only sections of page rather than loading entire page every time new content is added -> dynamic loading of content

## JavaScript Window properties
- Window = what the user sees in their web browser

window.innerwidth = how wide is the window? [x-axis]
- useful to know how many pixels wide the user's screen is

window.innerheight = height/tallness of window [y-axis]

# JavaScript Window vs. Document objects

Document = entire web page including sections of web page that are offscreen ["can be part of the document that is above or below the window"]

Window = only the section of the web page that is CURRENTLY visible to the user, need to scroll through to other parts of the document/webpage

9:52:15

	window.scrollY 
-> "How many pixels down have you scrolled? [on the y-axis]"

- at the top of the page, "window.scrollY" = 0, "you haven't scrolled down"

		document.body.offsetHeight 
		
-> is the entire height of the page in pixels [total length of the y-axis of the webpage]

	window.innerHeight
-> is the height of the visible window of the webpage [length of the y-axis of the webpage that the user can currently see]

	window.innerWidth
-> is the width of the visible window of the webpage [length of the x-axis of the webpage that the user can currently see], [may be the same as the total width of the webpage because a lot of webpages are designed to only scroll down with default zoom-in parameters]

### Calculations and things to consider with the window and document:

**"Has the user scrolled down all the way to the bottom of the page or not?"**
- no event listener that listens for this specific situation, but you can apply logic to figure this out

if: 
1. document.body.offsetHeight = total height of the webpage in pixels, 
2. window.scrollY = amount the user has scrolled down the height or y-axis of the webpage, 
3. and window.innerHeight = the amount of the height of the page that is visible to the user [amount of y-axis length that the user can see]

Then:
**If the window.scrollY[amount they scrolled] + window.innerHeight[amount they can see] = document.body.offsetHeight, then the user has scrolled all the way to the bottom of the page.**

- Go to scroll.html in visual studio code for continued notes
9:54:04

- changing color when reaching bottom of page might not be useful for a lot of things, but there similar functions
- example: websites that have infinite scroll [page auto loads new content/the next content when you reach the bottom of the page]

#### Infinite scroll logic:
1. detect when user reaches bottom of page
2. asynchronously load JavaScript to load additional content[fetch new content]

next example: create Django project called "scroll" with an app called "posts" inside of it -> see visual studio code
9:58:11

-in code notes: how to create dynamically loading page that loads new posts when user reaches bottom of page
-[check github repo source code to troubleshoot, could not get to work only using the sections of code instructor Brian showed during demo]
10:03:42

## Add animations to HTML elements using CSS

- more responsive/more interesting
- moves around and changes properties
- change color, size, position over a set amount of time

10:04:38

**Keyframes** = specify values for when the animation starts and when the animation ends [ex. at the start: font is 10px and at the end: font is 100px -> font grows from 10px to 100px in size over the duration of the animation]

- see animate.html variants in code folder

10:10:30


10:17:50

