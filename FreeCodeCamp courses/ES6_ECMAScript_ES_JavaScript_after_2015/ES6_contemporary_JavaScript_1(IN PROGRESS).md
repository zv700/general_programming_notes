ECMAScript and JavaScript are interchangable/refer to the same thing

- ES5 finalized in 2009
- ES6 was established in 2015 and is still being added to/development ongoing

<h3>COMPARE SCOPES OF THE var AND let KEYWORDS</h3>

-declaring a variable with "var" will have a local scope if declared within a function OR global scope if it is declared outside of a function
-declaring a variable with "let" is similar to "var" but with more features
-variables that are declared with "let" inside of a block, statement, or expression have their scope limited to that specific block, statement, or expression

==================

var numArray = [];
var i;
for (i = 0; i < 3; i++) {
  numArray.push(i);
}
console.log(numArray);
console.log(i);

// Here the console will display the values [0, 1, 2] and 3.

var printNumTwo;
for (var i = 0; i < 3; i++) {
  if (i === 2) {
    printNumTwo = function() {
      return i;
    };
  }
}
console.log(printNumTwo());

// Here the console will display the value 3.
// behaves this way because "var" was used to assign value to "i" globally
// because of "var", "printNumTwo()" will return global value for "i", instead of "i" value set within the "for" loop
// use "let" when assigning variables to avoid this

=======================

let printNumTwo;
for (let i = 0; i < 3; i++) {
  if (i === 2) {
    printNumTwo = function() {
      return i;
    };
  }
}
console.log(printNumTwo());
console.log(i);

// Here the console will display the value 2, and an error that i is not defined.
// "i" was declared with local scope using "let"
// "i" in this example only has value within the "for" loop because it was assigned with "let", "i" outside of the "for" loop has not been assigned a value yet
// "i is not defined" for console log of "i" value because "i" value was not declared globally
// "printNumTwo" gives correct values because it is being used within the local scope of the "for" loop where "i" was assigned value

===================
Fix the code so that i declared in the if statement is a separate variable than i declared in the first line of the function. Be certain not to use the var keyword anywhere in your code.

This exercise is designed to illustrate the difference between how var and let keywords assign scope to the declared variable. When programming a function similar to the one used in this exercise, it is often better to use different variable names to avoid confusion.



function checkScope() {
  let i = 'function scope';
  if (true) {
   let i = 'block scope';
    console.log('Block scope i is: ', i);
  }
  console.log('Function scope i is: ', i);
  return i;
}



<h3>MUTATE AN ARRAY DECLARED WITH const</h3>

const s = [5, 6, 7];
s = [1, 2, 3];
s[2] = 45;
console.log(s);

// s = [1, 2, 3] will result in an error. 

const s = [5, 6, 7];
// s = [1, 2, 3];
s[2] = 45;
console.log(s);

// After commenting out that line, the console.log will display the value [5, 6, 45].

// individual elements within the array are mutable [can be changed, mutate]
BEFORE: const s = [8, 9 ,10];
s[0] = 800;
AFTER: s = [800, 9, 10];
// The value for THE VARIABLE ITSELF cannot be changed later in code if value is assigned with const
BEFORE: const s = 100;
s = 1;
AFTER: error
// elements within an object assigned to a variable with const [like an array] can be mutated, but the entire value of the variable cannot be changed in later lines of code
// change individual element of an array one at a time, not all at once

==============
An array is declared as const s = [5, 7, 2]. Change the array to [2, 5, 7] using various element assignments.


const s = [5, 7, 2];
function editInPlace() {
  // Only change code below this line
s[0] = 2;
s[1] = 5;
s[2] = 7;
  // Using s = [2, 5, 7] would be invalid

  // Only change code above this line
}
editInPlace();

<h3>PREVENT OBJECT MUTATION</h3>

- protect data from mutation with JavaScript function: "Object.freeze"
- attempts to change data/frozen object will be rejected, error thrown in console if the script is running in strict mode

============

let obj = {
  name:"FreeCodeCamp",
  review:"Awesome"
};
Object.freeze(obj);
obj.review = "bad";
obj.newProp = "Test";
console.log(obj); 

//The obj.review and obj.newProp assignments will result in errors, because our editor runs in strict mode by default, and the console will display the value { name: "FreeCodeCamp", review: "Awesome" }.
// above: "obj.review = bad;" attempts to change the line 'review: "Awesome" '
// "obj.newProp = Test;" attempts to add the object: "Test" to the list
// both fail because "obj" has been frozen with "Object.freeze(obj);"

========

In this challenge you are going to use Object.freeze to prevent mathematical constants from changing. You need to freeze the MATH_CONSTANTS object so that no one is able to alter the value of PI, add, or delete properties.


function freezeObj() {
  const MATH_CONSTANTS = {
    PI: 3.14
  };
  // Only change code below this line
Object.freeze(MATH_CONSTANTS);

  // Only change code above this line
  try {
    MATH_CONSTANTS.PI = 99;
  } catch(ex) {
    console.log(ex);
  }
  return MATH_CONSTANTS.PI;
}
const PI = freezeObj();


<h3>USE ARROW FUNCTIONS TO WRITE CONCISE ANONYMOUS FUNCTIONS</h3>

- use arrow function syntax => to simplify smaller functions into ONE LINE STATEMENTS
- when there is no function body, and only a return value, arrow function syntax allows you to omit the keyword: return [arrow function syntax will automatically "return" even if "return" is not written] 
- in JavaScript, don't always have to name functions
- like when when passing a function as an argument to another function
- can use INLINE FUNCTIONS
- inline functions do not have to have names because these functions are not resued outside of its original placement
- named functions can be used multiple times in code after a named function is established

SYNTACTIC SUGAR - computer science terminology for syntax within a programming language that is designed to make things easier to read or express, simplify code 
"sweeter for human use"

-arrow function syntax is a form of syntactic sugar

BEFORE:

const myFunc = function() {
	const myVar = "value";
	return myVar;
}

AFTER:

const myFunc = () => {
	const myVar = "value";
	return myVar;
}

//above omits function name, keeps parentheses generic slot for input, replaces with arrow function syntax => to make the function anonymous/nameless/generic function that is not reused elsewhere

AFTER (simplified further):

const myFunc = () => "value";

// above will automatically return the string "value" by default because of arrow function syntax
// "return" keyword and curly brackets {} that surround code can be omitted when using arrow function syntax in simple functions that do not have function body, will return a value by default


============

Rewrite the function assigned to the variable magic which returns a new Date() to use arrow function syntax. Also, make sure nothing is defined using the keyword var.

BEFORE:

var magic = function() {
  return new Date();
};

AFTER:

	const magic = () => new Date();
	
<h3>WRITE ARROW FUNCTIONS WITH PARAMETERS</h3>

- you can pass arguments through arrow functions like you can with regular functions

const doubler = (item) => item * 2;

doubler(4);

// doubler(4); would return the value: 8

if an arrow function only has ONE parameter, the parentheses surrounding the parameter can be omitted

	const doubler = item => item * 2;

is the same as

	const doubler = (item) => item * 2;

- it's possible to pass more than one argument through an arrow function
- seperate multiple arguments/inputs in parentheses with commas

const multiplier = (item, multi) => item * multi;

multiplier(4, 2);

// multiplier(4, 2); would return the value: 8

===============

Rewrite the myConcat function which appends contents of arr2 to arr1 so that the function uses arrow function syntax.

BEFORE:

var myConcat = function(arr1, arr2) {
  return arr1.concat(arr2);
};

console.log(myConcat([1, 2], [3, 4, 5]));

AFTER:

const myConcat = (arr1, arr2) => arr1.concat(arr2);

console.log(myConcat([1, 2], [3, 4, 5]));

// console log returns: [1, 2, 3, 4, 5]

	
<h3>SET DEFAULT PARAMETERS FOR YOUR FUNCTIONS</h3>

ES6 introduced DEFAULT PARAMETERS for functions
- for more flexible functions

const greeting = (name = "Anonymous") => "Hello " + name;

console.log(greeting("John"));
console.log(greeting());

//The console will display the strings Hello John and Hello Anonymous.
// first displays "Hello John" because "John" is the given parameter
// (name = "Anonymous") defines parameter for function greeting()
//if no parameter is inserted where "name" is within the parentheses(), the default for "(name)" will be "(Anonymous)"
//default looks like this: "greeting()" which automatically becomes: "greeting(Anonymous)"


-default parameter activates when the argument is not specified or it is undefined
-above, parameter: "name" defaults to "Anonymous" in "= (name = "Anonymous") =>"
-will print "Anonymous"  when a value is not provided for the parameter
-you can add default values for as many parameters as you want

================

Modify the function increment by adding default parameters so that it will add 1 to number if value is not specified.


// Only change code below this line
const increment = (number, value = 1) => number + value;
// Only change code above this line

<h3>USE THE REST PARAMETER WITH FUNCTION PARAMETERS</h3>

-ES6 introduces "rest" parameter for function parameters for flexible functions

LOOKS LIKE ELIPSIS FOLLOWED BY VARIABLE WITHIN PARENTHESES:

function howMany(...args) {
	return "code"
}

OR


functionOne(...n)


-IF YOU HAVE MULTIPLE DIFFERENT VARIABLES (a, b, c), REPLACE THEM WITH (...args)
-if you have multiple variables that follow a similar naming convention (a1, a2, a3) you can condense them as (...a)

-"rest" parameter lets you create functions that take a variable number of arguments
-arguments are stored in an array that can be accessed later from inside the function
-The rest parameter eliminates the need to use the arguments object and allows us to use array methods on the array of parameters passed to the function howMany.


function howMany(...args) {
  return "You have passed " + args.length + " arguments.";
}
console.log(howMany(0, 1, 2));
console.log(howMany("string", null, [1, 2, 3], { }));

//The console would display the strings "You have passed 3 arguments." and "You have passed 4 arguments."

===========

BEFORE:

const product = (n1, n2, n3) => {
  const args = [n1, n2, n3];
  let total = 0;
  for (let i = 0; i < args.length; i++) {
    total += args[i];
  }
  return total;
}
console.log(product(2, 4, 6)); //48


AFTER:

const product = (...n) => {
  let total = 0;
  for (let i = 0; i < n.length; i++) {
    total += n[i];
  }
  return total;
}
console.log(product(2, 4, 6)); //48

============

Modify the function sum using the rest parameter in such a way that the function sum is able to take any number of arguments and return their sum.

const sum = (...args) => {
  let total = 0;
  for (let i = 0; i < args.length; i++) {
    total += args[i];
  }
  return total;
}

<h3>USE THE SPREAD OPERATOR TO EVALUATE ARRAYS IN-PLACE</h3>

-ES6 "spread operator" allows you to expand arrays and other expressions in places where multiple parameters or elements are expected

-"spread operator" looks like: Math.max(...arr);

===============

BEFORE (ES5 code):

var arr = [6, 89, 3, 45];
var maximus = Math.max.apply(null, arr);

//above becomes: "var maximus = Math.max.apply(null, [6, 89, 3, 45]);"
//maximus = 89 [maximus has a value of 89]
//above uses "apply()" to compute the maximum value in an array
//Math.max(arr) would return NaN [not a number]
//Math.max(null, [6, 89, 3, 45]); = NaN
//Math.max() expects comma-seperated arguments NOT an array [ex. = Math.max(null, 5)]


AFTER (ES6 code):

const arr = [6, 89, 3, 45];
const maximus = Math.max(...arr);

//spread operator: "max(...arr)" accepts arrays as arguments
//maximus = 89


Math.max.apply(null, arr); 
IS THE SAME AS
Math.max(...arr);

- (...arr) returns an UNPACKED ARRAY, it SPREADS the array
- "spread operator" only works in-place, [within parentheses as an argument]

WORKS:

const spreaded = Math.min(...arr);

DOES NOT WORK:

const spreaded = ...arr;

==============

Copy all contents of arr1 into another array arr2 using the spread operator.

const arr1 = ['JAN', 'FEB', 'MAR', 'APR', 'MAY'];
let arr2;

arr2 = [...arr1];  // Change this line

console.log(arr2);


<h3>USE DESTRUCTURING ASSIGNMENT TO EXTRACT VALUES FROM OBJECTS</h3>

-"destructuring assignment" is special syntax introduced in ES6
-neatly assigns values taken directly from an object USING ALREADY ESTABLISHED PARAMETERS ("name" value goes with "name" variable)

(ES5) WITHOUT DESTRUCTURING ASSIGNMENT:

const user = { name: 'John Doe', age: 34 };

const name = user.name;
const age = user.age;

//name has a value of 'John Doe'
//age has a value of 34
//NOTE: there are spaces between brackets and strings/info


(ES6) WITH DESTRUCTURING ASSIGNMENT:

const user = { name: 'John Doe', age: 34 };

const { name, age } = user;

//name has a value of 'John Doe'
//age has a value of 34
//destructuring ass allows you to assign multiple values to variables in one statement/line from established values within an object's properties
//can extract as many or as few values from the object as you want
// (i.e. not all values from the object properties need to be assigned to a variable in one statement or at all)

const user = { name: 'John Doe', age: 34, height: short, status: tired };

const { name, age } = user;

//above also works, not all values assigned to variables

================
Replace the two assignments with an equivalent destructuring assignment. It should still assign the variables today and tomorrow the values of today and tomorrow from the HIGH_TEMPERATURES object.


BEFORE(ES5):

const HIGH_TEMPERATURES = {
  yesterday: 75,
  today: 77,
  tomorrow: 80
};

// Only change code below this line

const today = HIGH_TEMPERATURES.today;
const tomorrow = HIGH_TEMPERATURES.tomorrow;

// Only change code above this line


AFTER(ES6):

const HIGH_TEMPERATURES = {
  yesterday: 75,
  today: 77,
  tomorrow: 80
};

// Only change code below this line

const { today, tomorrow } = HIGH_TEMPERATURES;


// Only change code above this line

<h3>USE DESTRUCTURING ASSIGNMENT TO ASSIGN VARIABLES FROM OBJECTS</h3>

-can extract values from object and ASSIGN VALUES TO VARIABLES WITH DIFFERENT NAMES THAN OBJECT LABELS

const user = { name: 'John Doe', age: 34};

const { name: userName, age: userAge } = user;

//how above is read:
//"get the value of user.name and assign it to a new variable named userName"
//value of user.name is 'John Doe'
//value of user.age is 34

============
Replace the two assignments with an equivalent destructuring assignment. It should still assign the variables highToday and highTomorrow the values of today and tomorrow from the HIGH_TEMPERATURES object.


BEFORE:

const HIGH_TEMPERATURES = {
  yesterday: 75,
  today: 77,
  tomorrow: 80
};

// Only change code below this line
  
const highToday = HIGH_TEMPERATURES.today;
const highTomorrow = HIGH_TEMPERATURES.tomorrow; 

// Only change code above this line

=================

AFTER:

const HIGH_TEMPERATURES = {
  yesterday: 75,
  today: 77,
  tomorrow: 80
};

// Only change code below this line
  
const { today: highToday, tomorrow: highTomorrow } = HIGH_TEMPERATURES;

// Only change code above this line

//construct { objectCategory1 : newName1, objectCategory2: newName2 } = objectName;

<h3>USE DESTRUCTURING ASSIGNMENT TO ASSIGN VARIABLES FROM NESTED OBJECTS</h3>

-same principles as previous two lessons above to extract, assign values from objects to variables within nested objects
-MUST HAVE NAME OF NESTED OBJECT COMING BEFORE NESTED PROPERTIES

const mainObject = {
	nestedObj1: { nestedProp1: 1, nestedProp2: 2 },
	nestedObj2: {
	nestedProp1: 10, nestedProp2: 20
	}
};

const { nestedObj1: { nestedProp1: newName1 }} = mainObject;


================
const user = {
	johnDoe: {
		age: 34,
		email: 'johnDoe@freeCodeCamp.com'
	}
};

const { johnDoe: {age, email }} = user;

//above: extract values of object properties and assign them to variables WITH THE SAME NAME
//no difference between object property name and variable name (value of 'email' property goes with 'email' variable)

const { johnDoe: { age: userAge, email: userEmail }} = user;

//different variable names from corresponding properties
//'age' value goes with 'userAge' variable

============

Replace the two assignments with an equivalent destructuring assignment. It should still assign the variables lowToday and highToday the values of today.low and today.high from the LOCAL_FORECAST object.

BEFORE:

const LOCAL_FORECAST = {
  yesterday: { low: 61, high: 75 },
  today: { low: 64, high: 77 },
  tomorrow: { low: 68, high: 80 }
};

// Only change code below this line
  
const lowToday = LOCAL_FORECAST.today.low;
const highToday = LOCAL_FORECAST.today.high;

// Only change code above this line

=============

AFTER:

const LOCAL_FORECAST = {
  yesterday: { low: 61, high: 75 },
  today: { low: 64, high: 77 },
  tomorrow: { low: 68, high: 80 }
};

// Only change code below this line

const { today: { low: lowToday, high: highToday }} = LOCAL_FORECAST;

// Only change code above this line


<h3>USE DESTRUCTURING ASSIGNMENT TO ASSIGN VARIABLES FROM ARRAYS</h3>

-ES6 assign values from arrays similar to objects with destructuring assignment

-SPREAD OPERATOR unpacks all contents of an array into a comma sperated list
-with SPREAD OPERATOR you CANNOT choose which elements you want to assign to a variable
-DESTRUCTURING ASSIGNMENT to assign values from arrays DOES allow you to assign variables from spread list

const [a, b] = [1, 2, 3, 4, 5, 6];
console.log(a, b);

//value for 'a' is 1
//value for 'b' is 2
//values for a and b take the values for first and second indexes of the array

const [a, b,,, c] = [1, 2, 3, 4, 5, 6];
console.log(a, b, c);

//value for 'a' is 1
//value for 'b' is 2
//value for 'c' is 5
//USE COMMAS TO ACCESS SPECIFIC NUMBER INDEXES OF AN ARRAY
//there are four commas before 'c' which means 'c' will have the value of the 5th index


===================

Use destructuring assignment to swap the values of a and b so that a receives the value stored in b, and b receives the value stored in a.

BEFORE:

let a = 8, b = 6;
// Only change code below this line

==============

AFTER:

let a = 8, b = 6;
// Only change code below this line
[a, b] = [b, a]; 

<h3>DESTRUCTURING VIA REST ELEMENTS</h3>

-assign some values from an array and COLLECT THE REST OF THE VALUES WITHIN A SEPERATE ARRAY
-similar in function to 'Array.prototype.slice()'
-destructure using 'rest element' by assigning remaining values to '...arr'
-REST ELEMENT only works correctly as the LAST ASSIGNED VARIABLE within the list (rightmost value)
-cannot use 'rest syntax' to catch a subarray that leaves out the last element of the original array

const [a, b, ...arr] = [1, 2, 3, 4, 5, 7];
console.log(a, b);
console.log(arr);

//value of 'a' is 1
//value of 'b' is 2
//value of 'arr' is [3, 4, 5, 7]


=================

Use a destructuring assignment with the rest syntax to emulate the behavior of Array.prototype.slice(). removeFirstTwo() should return a sub-array of the original array list with the first two elements omitted.

BEFORE:

function removeFirstTwo(list) {
  // Only change code below this line
  const shorterList = list; // Change this line
  // Only change code above this line
  return shorterList;
}

const source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const sourceWithoutFirstTwo = removeFirstTwo(source);

==================

AFTER:

function removeFirstTwo(list) {
  // Only change code below this line
  const [a, b, ...shorterList] = list; // Change this line
  // Only change code above this line
  return shorterList;
}

const source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const sourceWithoutFirstTwo = removeFirstTwo(source);

//fuckin horribly worded task/question
//'shorterlist' is the name of the array THAT CONTAINS THE REST OF THE VALUES
//they want you to assign the first two elements of array 'source' to their own variables [a, b] and then assign the REST to array 'shorterlist' [...shorterlist]
//[a, b, ...shorterlist]


<h3>USE DESTRUCTURING ASSIGNMENT TO PASS AN OBJECT AS A FUNCTION'S PARAMETERS</h3>

-destructure the object within a function argument
-everything after the arrow '=>' is WHAT THE FUNCTION DOES TO THE INPUT
-change parameters before the arrow '=>'

const profileUpdate = (profileData) => {
	const { name, age, nationality, location } = profileData;
}



const profileUpdate = ({ name, age, nationality, location }) => {
}

//when profileData is passed to the above function, the values are destructured from the function parameter for use within the function
//takes established values you set prior to running function
//when profileData is passed through th function, the values are destructed for use within the function

=====================

Use destructuring assignment within the argument to the function half to send only max and min inside the function.

BEFORE:

const stats = {
  max: 56.78,
  standard_deviation: 4.34,
  median: 34.54,
  mode: 23.87,
  min: -0.75,
  average: 35.85
};

// Only change code below this line
const half = (stats) => (stats.max + stats.min) / 2.0; 
// Only change code above this line

==============

AFTER:

const stats = {
  max: 56.78,
  standard_deviation: 4.34,
  median: 34.54,
  mode: 23.87,
  min: -0.75,
  average: 35.85
};

// Only change code below this line
const half = ({ max, min }) => (max + min) / 2.0; 
// Only change code above this line

// inputs entered within parentheses and curly bracket ({ }) 



<h3>CREATE STRINGS USING TEMPLATE LITERALS</h3>

-ES6 feature: 'template literal'
-makes creating complex strings easier
-create multi-line strings 
-use string interpolation features to create strings
-add variable values to strings
-add values from object parameters to strings, strings being used as templates
-use in ES6 instead of using string concatenation

-below: multiple users can have different names and ages in a database, the string will change depending on which user's info is presented

const person = {
	name: "Zodiac Hasbro",
	age: 56
};

const greeting = `Hello, my name is ${person.name}!
I am ${person.age} years old.`;

console.log(greeting);

//console displays 'Hello, my name is Zodiac Hasbro!' AND 'I am 56 years old.'
//the string is wrapped in BACKTICKS [same key as ~ tild under the esc key] NOT SINGLE QUOTES ' '
//add variable to string by wrapping the variable with dollar sign, curly brackets ${variableName}
//can add multiple variables to string with plus signs between ${a + b}
//if a = 'Yes, ', b = 'dear.', then ${a + b} = 'Yes, dear.'

================
TASK:
Use template literal syntax with backticks to create an array of list element (li) strings. Each list element's text should be one of the array elements from the failure property on the result object and have a class attribute with the value text-warning. The makeList function should return the array of list item strings.

Use an iterator method (any kind of loop) to get the desired output (shown below).

[
  '<li class="text-warning">no-var</li>',
  '<li class="text-warning">var-on-top</li>',
  '<li class="text-warning">linebreak</li>'
]

BEFORE:

const result = {
  success: ["max-length", "no-amd", "prefer-arrow-functions"],
  failure: ["no-var", "var-on-top", "linebreak"],
  skipped: ["no-extra-semi", "no-dup-keys"]
};
function makeList(arr) {
  // Only change code below this line
  const failureItems = [];
  // Only change code above this line

  return failureItems;
}

const failuresList = makeList(result.failure);

================

AFTER:

const result = {
  success: ["max-length", "no-amd", "prefer-arrow-functions"],
  failure: ["no-var", "var-on-top", "linebreak"],
  skipped: ["no-extra-semi", "no-dup-keys"]
};
function makeList(arr) {
  // Only change code below this line
  const failureItems = [];
  for (let i = 0; i < arr.length; i++) {
    failureItems.push(`<li class="text-warning">${arr[i]}</li>`);
  }
  // Only change code above this line

  return failureItems;
}

const failuresList = makeList(result.failure);

//make a for loop
//LINE 8: creates 'failureItems' array. The array is empty from the start, but will be populated by values from the 'failure' array
//LINE 9: for loop, 'i' is index number, as long as index number is less than the total array length, in 'i' index value will be incremented by 1 (i + 1) each time the loop runs through an iteration
//LINE 10: with each loop iteration, pushes the next value from 'failure' array into the input ${} of the string template literal: `<li class="text-warning">${arr[i]}</li>


<h3>WRITE CONCISE OBJECT LITERAL DECLARATIONS USING OBJECT PROPERTY SHORTHAND</h3>

-ES6 supports OBJECT PROPERTY shorthand/shortcut/simpler ways of defining object literals (syntactic sugar)

const getMousePosition = (x, y) => ({ x: x, y: y });

//getMousePosition function returns an object containing two properties
//redundant to write x twice (x: x)
//in ES6 within this context you can write just 'x' and it will be converted to 'x: x' or something equivalent under the hood
//below: same function as above using shorthand syntax

const getMousePosition = (x, y) => ({ x, y });

====================
TASK:
Use object property shorthand with object literals to create and return an object with name, age and gender properties.

BEFORE:

const createPerson = (name, age, gender) => {
  // Only change code below this line
  return {
    name: name,
    age: age,
    gender: gender
  };
  // Only change code above this line
};

=================

AFTER:  

const createPerson = (name, age, gender) => {
  // Only change code below this line
  return {
    name,
    age,
    gender
  };
  // Only change code above this line
};

<h3>WRITE CONCISE DECLARATIVE FUNCTIONS WITH ES6</h3>

