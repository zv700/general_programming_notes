## Basic communication via the internet:

**Client sends HttpRequest to Server**
- Client = user, using a web browser [Chrome, Safari, Firefox, etc.]
- Server processes the request, returns a response back to Client

### Previous code from this course: Python + Django = Server-side code
- code from previous sections of course --> Python code using Django framework --> runs from server
- the code listens for a request --> does computation to process the request --> generates a response
- the response is usually an .html template that is sent back to the client

## JavaScript = Client-side code
- JavaScript allows you to write code that runs Client-side inside of the user's web browser

**JavaScript can be useful for:**
1. if there's computation that needs to be done, but does not need a connection to the server to do so [faster: more efficient to compute client-side rather than have client reach out to server first before computing]
2. make web pages more interactive

JavaScript allows you to directly manipulate the DOM
- DOM = Document Object Model --> tree-like hierarchy that represents the web page the user is viewing
- write code that directly manipulates content of web page

HTML provides structure to web pages --> describes page structure through nested tags

## Include JavaScript inside of an HTML web page

- use JavaScript on a web page by including script tags within the web page's .html structure:

	<script></script>
	
--

- anything between script tags is interpreted as JavaScript code for the web browser to execute

### First JavaScript program:

	<script>
		alert('Hello, world!');
	</script>
	
- alert() function produces an alert that says/prints the string: 'Hello, world!' --> pop up with "This page says" then your message with an OK in bottom right to dismiss the alert
- alert() is a built-in function of JavaScript
- like in Python, JavaScript functions take arguments within parentheses()
- in JavaScript, you can use single quotes ' ' or double quotes " " to represent strings

## JavaScript: Event driven programming

- Event driven programming = thinking about things that happen on the web as "events that happen"
- Event examples: user clicks on button, user makes a selection from a drop down list user scrolls through a list, user submits a form
- Event = any way a user interacts with a web page

**use JavaScript Event Listeners or Event Handlers to have JavaScript code respond to how user interacts with web page**
- "when an event happens, run this particular block of code"
- "run this JavaScript function when a user clicks on a button"

## write a function in JavaScript

7:46:39

- write KEYWORD: function followed by the name of the function, 
- any inputs the function takes in parentheses
- any code you want to run goes into curly brackets --> the BODY of the function
- end code to be executed with semicolon ;
-- 

	function hello() {
		alert('Hello, world!');
	} 


"function called hello that when called, displays an alert that says 'Hello, world!' "

## get the function to run when something happens on the page - when the user clicks a button

place a button on the html page with the attribute: onclick

--

	<button onclick="hello()">Click Here</button>
	
- on click handler
- when a user clicks on the button, the function hello() runs
- like python, write name of function followed by parentheses: hello()
- parentheses calls/runs the function
- nothing inside of parentheses means not input is being entered into the function
- hello() funciton does not take input, so an input is not required

- hello() is a function you the programmer wrote
- alert() is a function that comes bundled in by default with JavaScript

## JavaScript variables

define a variable in JavaScript:

	let counter = 0;
	
"let there be a variable called counter"

## increment a value (value plus one, x + 1)

increase the value of a variable by one

multiple ways of writing the same thing:

	counter = counter + 1;
	
	counter = counter += 1;
	
	counter = counter++;
	
All three lines of code above add the value 1 to the value of variable: counter --> increment the variable

- counter++; method of incrementing is similar to notation in C coding language

## Comment out code in JavaScript

lines of code that start with // will be ignored in JavaScript code

	// this line of code is commented out
	
## use JavaScript to change the content of a webpage

- JavaScript allows you to change the DOT = Document Object Model = all of the elements on a webpage

use document.querySelector to look through an html page and extract an element of that page
- use JavaScript to manipulate that selected html element
- querySelector only returns one element, if there are multiple it will return the first one it finds
--

	document.querySelector('h1')

Above will have querySelector search the html page for an h1 element

--

	document.querySelector('h1').innerHTML = 'Goodbye!';
	
Above will change the text of the selected h1 element to the string 'Goodbye!'

- change the selected .html by modifying the .innerHTML property of the JavaScript element

in order to update the property of something in JavaScript you use the .notation --> .innerHTML

- a dot . represents the property of an object


## JavaScript conditions

- like Python, Javascript has "if, else, elif" logic statements

### IDEALLY USE === to check for equality

=== --> JavaScript checks for strict equality ---> value must match exactly, types of both compared values must be the same

== --> checks for equality with a little more leeway than === --> two compared values can have different types (ex. integer compared to a string)

### define a variable using const

- use const to define a variable if you know its value will never change --> "a constant"

--

	const heading = 1
	
- "I will never have a line of code that says heading = something else" , never have a line of code later in the program that tries to change the value of variable: heading
- JavaScript will give an error if you try to change the value of a variable defined with const
- helpful for preventing unintended behavior due to unintentional overwriting of a variable value later

## mod % --> divide by

"if counter % 10"

"if counter mod 10"

"if you take the value of variable: counter and divide it by 10"

"if counter % 10 === 0" 
If the remainder of variable: counter divided by 10 is 0 then
---> that means the value of variable counter is dividable by 10. It is a multiple of 10

**- use mod 10 [x % 10 === 0] to say "do this every tenth time an event happens"**

## Template literal: JavaScript's equivalent to Python fstring

fstring in Python:

	function(f"The count is now {counter}")
	
template literal in JavaScript

	alert(`The count is now ${counter}`)
	
- use backtick [same key as ~, under ESC] instead of quotes
- use dollar sign curly brackets to surround variables ${variable}


## ideally, do not intermingle JavaScript code with .html code as programs become more complex/pages become larger

- seperate JavaScript code from .html code to make things easier to manage later on

- set an event listener in script portion of page that listens for specific events rather than including javascript commands within HTML attributes throughout a page
- compare differences between counters2.html and counters3.html for example

## JavaScript functions can be treated as values in of themselves

- set a variable equal to a function
- "functional programming"
- manipulate a function like you would a variable, integer, string, etc.

## if you run into problems, run the JavaScript console -> like the terminal window in Django/Python

- displays any JavaScript errors from the browser dev console

- from browser -> right click -> inspect -> console tab

**null = nothing, object does not exist**

--
	
	document.querySelector('button').onclick = count;

- above: error trying to edit value of null

- document.querySelector will give a null error if it cannot find the specified element on a page
**- error because browser runs code from TOP TO BOTTOM --> JavaScript is run from the head of the page**
- when document.querySelector runs, the page has not yet processed that there is a button lower down in the code in the body of the .html page --> content of the DOM of the page has not yet finished loading


Possible solutions:
- [not common method] move the <script></script> tag section to a position lower than the <body></body> tags

[common method] add another event listener that listens to the ENTIRE DOCUMENT ITSELF
- variable: document is a variable you always have access to that refers to the entire webpage itself
--
			
			document.addEventListener('DOMContentLoaded', )
	
two events: 
1. what event you're looking for and 
2. what function should run when DOM finishes loading - can be name of function or write the actual function within the second argument

- 'DOMContentLoaded' means the event listener is waiting until after all content on the page is loaded before running functions

- second argument can be an anonymous function()

- anonymous function() -> a function that has no name but is being run through a function for the purpose of making the eventListener run --> object requires an argument to run, so you add in an empty argument

## have a seperate file for JavaScript [similar to having a seperate file for CSS]

- can be helpful if you have multiple people working on the same page [one working on html and another working on JavaScript]
- helpful if one of the two [html or JavaScript] is going to change more than the other, only have to make changes to one file at a time
- can use one .js JavaScript file to handle JavaScript for multiple .html pages
- JavaScript libraries = JavaScript written by other people [like Bootstrap]


### **All JavaScript code that was written in an .html <script></script> can be placed inside of a .js file [without including the script tags]**
- in html page in <script></script> tag section, include an src attribute that points to the .js file

## more page interactivity - user fills out a form, page responds

- autofocus attribute of input field makes the page focus on that element when they open the page
- id = unique identifier for you to be able to quickly reference this specificly named element on the page

## select specific elements with document.querySelector
- document.querySelector similar to selection within CSS

document.querySelector('tag')
document.querySelector('#id')
document.querySelector('.class')

- hashtag id for a specific element with that id --> id's are unique, will only be one element on a page with that id

- .class for multiple elements tagged with the same class attribute


**any time you find yourself copy pasting the same code, could use optimization**

8:32:45

## data attributes

instead of

	<button id="red">Red</button>
	
can be

	<button data-color="red">Red</button>
	
Data attributes always start with "data-"

- used if you want to store data within an element
- "what color should the text be changed to when the button is clicked on?"

document.querySelector() only selects ONE element at a time

**document.querySelectorAll() will select multiple elements**

- querySelectorALL() will return an array of all elements that match your particular query --> use to select all of the buttons on the page
- JavaScript array = a list
-

Can also directly write code within JavaScript browser console --> can use to text code "what happens when I _?"
- node.list similar in function to an array

### querySelectorAll() example: one looping event handler for three elements

use querySelectorALL() to select all buttons on page --> loop over list/array of buttons --> for each button there should be an event handler that changes color of h1 element

	querySelectorALL().forEach

- .forEach is a function that accepts as an argument another function
- "for each of the elements inside of a node.list/array/list"


button.dataset.color corresponds to data-color attribute of each button

**example script nested function layers:**
- layer 1 "run a function after the page's DOM is fully loaded" 
- layer 2 "run a query that selects all buttons on the page"
"event handler: on click, run a function"
- layer 3 "function: for each button selected/stored in the array, run a function" --> loop through the array and run the function once on each array element
- layer 4 "function: select the element with the #hello id and change its CSS style: color to the color stored within the clicked button's dataset (data-color)"

8:40:50

## JavaScript arrow notation =>

in newer versions of JavaScript:

arrows => can replace function()/anonymous functions

This:

	.forEach(function(button) {}

Is the same as:

	.forEach(button => {}
	
	
----------------------------------
old format: 

	function(anonymousFunction(input) {codeBodyToBeExecuted})

new format:

	function(input => {codeBodyToBeExecuted})
	
newformat if no input:

	function(() => {codeBodyToBeExecuted})
	
	
8:43:12

## Other JavaScript event handlers

dropdown menu <select></select>
- .onchange corresponds to select dropdown menus [like how .onclick corresponds to buttons]
- "when a user chooses something different, run this code"

### this
- "this" is a special value/KEYWORD in JavaScript
- based on context
- "this" within an event handler will ALWAYS REFER to the thing/element that recieves the event
- in example: if the querySelector is selecting a dropdown menu, then "this" keyword will refer to the dropdown menu

## Other JavaScript Events:

- onclick
- onmouseover [hovering mouse over webpage]
- onkeydown [when you press down a key on the keyboard]
- onkeyup [when you let go of a key on the keyboard after pressing it down]
- onload
- onblur
- etc.

# JavaScript ToDo list [only using JavaScript, no servers, etc.]

### Create a new element on a page using JavaScript

	const li = document.createElement('li');

above: creates a new list item [to populate the example's empty unordered list --> list item = <li></li>]

	li.innerHTML = task;
	
above: after creating variable/element: li, updates li's HTML text to the value of variable: task [in example's context: task = user input into text field]

html property: disabled can be true or false -> allows you to disable something like a button

## JavaScript intervals

interval = a function runs after a specified amount of time in miliseconds

	setInterval(count, 1000);
	
- setInterval() is a JavaScript built-in function
- first input/argument = function you want to run
- second input/argument = number of miliseconds pass before the specified function runs automatically

1 second = 1000 miliseconds

- interval can be used for countdown/countup timers on webpages

9:01:48

## Local storage

- web browser can ask user to store info locally on their computer in their browser
- on subsequent visits to the same page, JavaScript can access values stored locally
- Store or retrieve information stored within the user's browser

**stores 2 key functions to be able to manipulate locally stored values**

	localStorage.getItem(key)
	
- "get something(data) out of local storage using its key. KEY = name given to a specific value"
	
	localStorage.setItem(key, value)
	
- "adds a new value to local storage or replaces an existing value in local storage => sets a KEY equal to a particular VALUE"

9:05:29

## Check local storage values/data

In browser (chrome):

	right click, inspect(devconsole) -> application tab (up top)-> local storage


## JavaScript Objects

- JavaScript object = Python dictionary (similar)
- KEY: VALUE
- look up the KEY to see what the stored/associated VALUE is

**JS Object syntax (similar to Python dictionary):**

	let person = {
		first: 'Jenny',
		last: 'Jean'
	};
	
- can access properties of JavaScript object

person
{first: 'Jenny', last: 'Jean'}

		person.first -> 'Jenny'
		
- first is a property, 'Jenny' is the value stored in the property

		person["first"]
		"Jenny"
- can also use square brackets like Python


- accessing KEY: VALUE within JavaScript objects = useful when exchanging data -> **moving around data from one service to another**

## API = Application Programming Interfaces

- "in the context of the web: some well defined, structured way for services on the internet to communicate with each other"
- your application interacts with another service "my app connects to a weather service to retrieve/display weather info" "my app connects to Google Maps to retrieve location information"
- send a REQUEST and recieve data using .json

### JSON = JavaScript Object Notation

- transfers data using JavaScript objects -> objects with properties, KEY: VALUE 

Example JSON -> flight information:

	{
		"origin": "New York",
		"destination": "London",
		"duration": 415
	}
	
- origin, destination, duration are all JavaScript object properties[KEY] with associated values
- in JSON quotations for KEY's are not required. [ex. origin: "New York"]
- if example Flights application wanted to share info about a specific flight with another application, it could share above JSON data so other application could access data as a JavaScript object
- JSON is good because it is intuitive: both "human readable" and "machine readable"
- computer knows to access property that comes before the colon: to find out the value that comes after the colon:


9:12:00

- Python and other programming languages can interpret JSON data

JSON useful for representing structures
- can contain lists or arrays
- can contain other JavaScript objects [nested: object within an object]


		{
			"origin": {
				"city": "New York",
				"code": "JFK"
			},
			"destination": {
				"city": "London",
				"code": "LHR"
			},
			"duration": 415
		}
		
- JSON payload = JSON object
- sender and reciever must agree upon the structure of data to be able to interpret and use JSON data in a meaningful way [ex. origin = starting point, destination = end point, duration = time in minutes]

## using JavaScript to access another service using API: access data about currency exchange rates

- currency exchange rates are always changing -> you always want access to the latest currency exchange rate data
- access exchange rate data via API, receive data in JSON format -> use JSON data to write an application that uses real time data to show current currency exchange rate conversions

example JSON data for USD conversions:

		{
			"rates": {
				"EUR": 0.907,
				"JPY": 109.716,
				"GBP": 0.766,
				"AUD": 1.479
			},
			"base": "USD"
		}
- "base" KEY -> USD (US Dollar) VALUE
- "rates" KEY that shows equivalent values of other currencies
- **JSON data structure organization may vary**
- JSON data is useful as long as sender and receiver both understand what the data means based on how the data is organized
- **look for commas, colons: , and curly brackets for data structure organization if JSON data is lacking spacing, indetations/visual organization**

9:15:07
[instructor Brian accesses api via browser, may be outdated site. I tried and got a 101 error, no api access key -> don't know, didn't mention how to get one in course]

## AJS = asynchronus JavaScript

- even after a page is loaded, can still ask for additional information do use/display on webpage via web REQUESTS
- using either your own web server or a third-party web server

In example: currency.html -> webpage should request for additional data about currency exchange rates

### fetch

- fetch commands queries a web server -> your server or third party
- recieves an Http response from queried page

When accessing API -> read API documentation to understand how parameters work, structure of data recieved

- after fetch sends a REQUEST, it recieves a PROMISE
- PROMISE = something/data will be received, but it may not be recieved immediately
- .then() function -> "what should I do when the PROMISE/response comes back"

9:19:26

console.log() - command prints result to JavaScript dev console

- access 

### JavaScript: round decimal values

`${rate.toFixed(3)} EUR.`; 
//variableName.toFixed(3) -> for long decimals, limits/rounds to 3 decimal places

## JavaScript undefined variable/value
- if you try to access a variable/property that does not exist, JavaScript returns the default variable: undefined
- undefined = there is no value, does not exist

### API data/retrieved JSON data is case-sensitive [KEYs are case-sensitive]

- in web app where user inputs three letter code for a specific currency "EUR" -> name of currency is case sensitive because in retrieved JSON data euros are listed as EUR
- by default, if user inputs "eur", the web app will treat the input as invalid

JavaScript function that takes an input string and converts it to uppercase:

		inputString.toUpperCase();
		
- above: if value of inputString is in lowercase letters, converts to uppercase letters
- if inputString = "eur", then .toUpperCase converts it to "EUR"

## .catch -> in case of error, [accessed API changes or goes down]

		.catch(error => [
                        console.log('Error:', error);
						
- "What should you do if something goes wrong?"
- runs code if cannot access API 

- in above: will display in console the string "Error:" and will store the error in variable: error
- "if something goes wrong when accessing the api, catch the error and print an error message in the dev console."
- "Error messages are a 'nice to have' when things crash, you want them to crash in a predictable way"
- 
