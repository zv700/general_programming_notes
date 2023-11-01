## Course overview

**HTML** - describes structure of web page
**CSS** - describes style of web page [colors, fonts, spacing, appearance]
**Git** - version control web program, track changes, work with others on seperate parts of program before merging parts into one final program

	course focus programming language #1
## Python 
- backend language for building program
**Django** - web programming framework written in Python, makes it easier to develop and design web applications, makes it easier to design web app that interacts with data

**SQL ("sequel")** - language used to interact with databases => used with Django to use models and migrations to interact with data, allows users to interact with data more easily

	course focus programming language #2
## JavaScript 
- runs in users' web browsers, enables interactivity for users in user interfaces, How do user interfaces work? How to develop UI using JavaScript + Python  

**Testing and CI/CD (Continuous Integration/Continuous Delivery)** - tools to use in software best practices to make sure devloping code is efficient
- test new pieces of code to make sure new code doesn't break existing parts of code in web applicaiton, 
- have a whole Suite of tests to ensure web app is behaving as it should

**Scalability and security on the internet** - what happens as the web application grows larger, 
- what happens when more and more users use the web app, 
- how to load balance between users, 
- what changes need to be made to database to ensure lots of users are able to connect to web app
- security implications of web application, what adversary might do if we're not careful, design web app proactively to ensure security


## HTML and CSS
**SEE DESKTOP CODE CS50 FOLDER "LESSON 0" PAGES FOR ADDITIONAL NOTES**

-how web browsers are able to display web pages

HTML is the same as HTML5 in !DOCTYPE (latest version of HTML)

- HTML page is comprised of nested HTML elements
- HTML elements describe something on the page
- can have elements inside of elements
- each HTML element is indicated by an HTML tag
- <html> tag indicates the beginning of HTML content on a give page's code
- </html> closing tag, end of HTML content
- HTML attributes: additional information about the tag
- <html lang="en">  HTML tag with the "lang" language tag to indicate the HTML page is written in English, used so web browser can recognize language of this given page
-ex. search engines use "lang" tag when it looks through pages to sort results

## DOCUMENT OBJECT MODEL (DOM)
- tree-like structure that describes how HTML elements are related to each other
- visuallizing DOM structure makes it easier to figure out which HTML element is inside of which other HTML element
- JavaScript allows you to modify DOM structure

**(*flowchart*)**
		head => title => Hello!
	   /
html
	   \
		body => Hello, world!

"html" = parent element

"head" = child element
"body" = child element

- indentation in HTML code is not necessary for browser to read code. 
- indentation is helpful visually for whoever is reading the page. 
- Readability is good


Two types of lists in HTML: ordered lists(numbered items) and unordered lists(bullet points)

	## CSS Style Attribute Specificity within a page's <style></style> section

1. inline (most specific)
2. id
3. class
4. type (least specific)
(5. external linked CSS page)

- hierarchy of style attributes 
- order doesn't matter to specificity [ex. if an class is higher in the pages code than an id, the id still takes precedence over the class ]
- 1. inline takes the most precedence/overwrites other CSS style attrivbutes
- 4. type takes least precedence/is overwritten by all others
- specificity goes in order of how precisely elements are identified
- id is unique, ONLY ONE element per id
- class can be applied to multiple elements
- type = ordered list, h1, table, div, etc. ()

type ex.

table {
	color: blue;
	} 

- all above hieracrchy items 1-4 take precedence over external linked CSS page



## CSS Selectors

a, b (multiple element selector)
a b (descendant selector)
a > b (child selector)
a + b (adjacent sibling selector)
[a=b] (attribute selector)
a:b (pseudoclass selector)
a::b (pseudoelement selector)

## Responsive Design 
- making sure the web page looks good regardless of how you're looking at it
- not just viewing a page on a computer browser
- webpage needs to look good on phone, tablet, etc.

## Responsive Design
- viewport
- Media Queries
- Flexbox
- Grids


## Viewport
- viewport = visible part of the screen that users can see
- by default, many mobile devices treat the viewport of a phone/etc. as the same width/dimensions as a desktop computer screen
- many phones will take desktop version of a web page and shrink it down to be able to fit a phone screen [not ideal]
- not all webpages are optimized for mobile devices
- ideally should design web pages to ADAPT to screen size/different device viewport dimensions

## -MAKE WEBPAGE AUTOMATICALLY ADAPT TO DEVICE VIEWPORT SIZE
-in <head> section of webpage html, add:
<meta name="viewport" content="width=device-width, initial-scale=1.0">
-above code: provides meta data to html, change the width of the viewport to be the width of the device

-many phones will load a viewport that is wider than the device by default as if it were loading on a desktop, then shrinks it down

## Media Queries
- Media types: print, screen...
- Media features: height, width, orientation(landscape, portrait, horizontal, vertical)...
- media queries control how a webpage looks like depending on what type of page it is or what kind of browser is being used to view it

## Flexbox
- when you're trying to display multiple elements on the same page at the same time that might overflow if not careful with responsive design
- overflow = arranged in a way where elements might not be on screen depending on viewport width/ **your row of elements are too wide for the screen and won't all show**
- elements might be good size to see on desktop monitor, but may shrink down to be too small to read/see on mobile device screen
- can make elements good size on mobile, but have to scroll left to right to see them [NOT ideal]
- try to get elements to wrap around when adapting to mobile screens

flexbox layout example:
- desktop: 1 2 3 4 5 6
- mobile: 1 2 3 
- mobile: 4 5 6


## Bootstrap = popular CSS and JavaScript library
- CSS library is prewritten CSS code template so you don't have to write CSS from scratch
- bootstrap = free to use for commercial/personal projects, free to modify
- to use bootstrap, add line of text: link to bootstrap stylesheet in html code head, from bootstrap site
- USE QUICKSTART FROM BOOTSTRAP SITE THEN SEARCH FOR DESIRED ELEMENTS IN SIDEBAR

## Style section tags
<style></style> section tags

[@] = media query [ex: @media (min-width: 10px) {} ]

[#] = id [ex: for id="example-id", #example-id {} ]

[.] = class [ex: for class="example-class", .example-class {} ]


## Bootstrap columns
<body>
<div class ="container">
<div class="row">
- bootstrap divides every row into a 12 unit column

-bootstrap allows you to specify how many units columns should take up depending on the size of a screen
<div class="col-lg-3 col-sm-6">
- above: the column/<div></div> takes up 3 units on large screens and 6 units on small screens

## SASS = extension to CSS

- **see inside desktop\code\Harvard CS50\Lesson 0:** variable.html, nesting.html, inheritance.html **for notes**

- SASS = extension to CSS (must have SASS installed, must convert/compile .scss files to .css to be usable in browsers)

- set SASS to automatically recompile changes to .scss file. in terminal: "sass --watch variable.scss:variable.css"-->

- IF TERMINAL BLOCKS SASS SCRIPT ".ps1 is not digitally signed. You cannot run this script on the current system." in terminal enter: "Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass" This command sets the execution policy to bypass for only the current PowerShell session after the window is closed, the next PowerShell session will open running with the default execution policy.
