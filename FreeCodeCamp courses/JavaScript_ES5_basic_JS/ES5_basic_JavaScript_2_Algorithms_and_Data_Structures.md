NUMBER is a data type in JavaScript that represents numeric data

<h2>OPERATORS, MATHEMATIC OPERATING SYMBOLS</h2>

PLUS SIGN + works the same way it does in math; an addition operator that combines two numbers it is placed between

	const myVar = 5 + 10;
[myVar has a value of 15 because 5+10=15]

	const sum = 10 + 10;
[sum has a value of 20]

SUBTRACTION SIGN - , same as in regular math, subtract right number from left

	const myVar = 12 - 6;
[myVar has a value of 6]

	const myVar = 45 - 33;
[myVar has a value of 12]

MULTIPLICATION, USE ASTERISK *

	const myVar = 13 * 13;
[myVar has a value of 169]

	const myVar = 8 * 10;
[myVar has a value of 80]

DIVISION, USE /

	const myVar = 16 / 2;
[myVar has a value of 8]

	const myVar = 66 / 33;
[myVar has a value of 2]

<h3>INCREMENT = ADD 1 TO A VARIABLE</h3>

add a value of one to a number by using INCREMENT: ++ [two adjacent plus signs]

	i = i + 1;
	
	i++;
	
[both above strings^^^ are the same, INCREMENT ++ usage is faster to type, reduces number of characters to use]	

	myVar = myVar = 1;
	
	myVar++;
	
<h3>DECREMENT --, decrease a variable by one with -- [two adjacent minus symbols]
</h3>
	i = i - 1;

	i--;
[both above are the same^^^]

	myVar = myVar - 1;
	
	myVar--;
	
<h2>FLOATS, FLOATING POINTS, DECIMALS</h2>
-you can declare a variable's value to be a FLOAT/DECIMAL
-when numbers are computed they are computed with finite precision, operations using FLOATING POINTS may vary in results

	const myDecimal = 1.5;
	
-in JavaScript you can perform caluculations using FLOATS/DECIMALS just like whole numbers

	const product = 2.0 * 2.5;
[value of product is 5.0]

	const quotient = 4.4 / 2.0;
[value of quotient is 2.2]

<h3>REMAINDER OPERATOR %</h3>
% is the REMAINDER OPERATOR, gives the remainder of two numbers instead of giving a number with a decimal for an answer

-the number to the right of the equal sign is the REMAINDER

-the REMAINDER OPERATOR does not work properly with NEGATIVE NUMBERS

-the MODULUS operator works with NEGATIVE NUMBERS

	17 % 2 = 1 (17 is Odd)
[result would be 8 with remainder of 1]

	48 % 2 = 0 (48 is Even)
[0 = no remainder]

	const remainder = 11 % 3;
[value of remainder is 2]

	5 % 2 = 1 because
	Math.floor(5 / 2) = 2 (Quotient)
	2 * 2 = 4
	5 - 4 = 1 (remainder)

-everything to the right of equals sign is evaluated first
-use assignments to modify the contents of a variable

<h2>ASSIGN VALUE AND PERFORM MATH OPERATION IN ONE STEP</h2>

	myVar = myVar = 5;
	
<h2>+= OPERATOR</h2>

	let myVar = 1;
	myVar += 5;
	console.log(myVar);
[console would display myVar's value as 6]

===================

	let a = 3;
	let b = 17;
	let c = 12;

	a = a + 12;
	b = 9 + b;
	c = c + 7; [value of c is 19]
	
	a += 12;
	b += 9;
	c += 7; [value of c is 19]
	
[^^above corresponding statements in bottom two segments are the same, reduces rudundancy of writing more than one of the same variable in the same line of code]

===================

<h3>-+ OPERATOR</h3>

	myVar = myVar - 5;
	
	myVar -= 5;
[^^above two statements are the same]

====================

	let a = 11;
	let b = 9;
	let c = 3;

// Only change code below this line

	a = a - 6; [a's value is 5]
	b = b - 15;
	c = c - 1;

	a -= 6; [a's value is 5]
	b -= 15;
	c -= 1;

[^^^corresponding statements in above are the same]

=====================

<h3>*= OPERATOR</h3>

	myVar = myVar * 5;
	
	myVar *= 5;
	
[above statements are the same]

=============================

	let a = 5;
	let b = 12;
	let c = 4.6;

// Only change code below this line

	a = a * 5; [a's value is 15]
	b = 3 * b;
	c = c * 10;
	
	a *= 5; [a's value is 15]
	b *= 3;
	c *= 10;
	
=====================================

<h3>/=OPERATOR</h3>

	myVar = my Var / 5;
	
	myVar /= 5;
	
=================================	
	
	let a = 48;
	let b = 108;
	let c = 33;

// Only change code below this line

	a = a / 12; 
	b = b / 4;
	c = c / 11; [c's value is 3]
	
	a /= 12;
	b /= 4;
	c /= 11; [c's value is 3]
	
====================================

<h3>ESCAPING LITERAL QUOTES IN STRINGS USING BACKSLASH \</h3>

-when defining strings, strings need to end with single quote['] or double quote ["]

-IF STRING INCLUDES single quote['] or double quote ["] in JavaScript you can ESCAPE a quote from considering the single or double quote is the end of the string with BACKSLASH [\] 

-ESCAPE A QUOTE BY PLACING BACKDASH IN FRONT OF THE QUOTE

THE STRING WITHOUT ESCAPE:

	"Alan said, "Peter is learning JavaScript".";

THE STRING WITH ESCAPE \:

	"Alan said, \"Peter is learning JavaScript\".";

[BACKDASHES ARE PLACED TO THE LEFT OF EACH CONTAINED QUOTATION MARK]

	const sampleStr = "Alan said, \"Peter is learning JavaScript\".";
	
Alan said, "Peter is learning JavaScript". [<-----------^^above string definition yields this statement, printed to the console]

	
	
		const myStr = "I am a \"double quoted\" string inside \"double quotes".";
		
[I am a "double quoted" string inside "double quotes".  <--yields in console]

-STRING VALUES in JavaScript can be written with single or double quotes as long as the string starts and ends with the same type of quote: ['    '] or ["    "]

	const doubleQuoteStr = "This is a string";
	const singleQuoteStr = 'This is also a string';
	
-you might want to use one over the other if you want to include a quote within a string WITHOUT having to ESCAPE a quote within the string

	const conversation = 'Finn exclaims to Jake, "Algebraic!"';
	
[above: no ESCAPE backslashes required for contained double quoted statement]

-APOSTROPHE COUNTS AS A SINGLE QUOTE AND REQUIRES BACKSLASH ESCAPE \

-BACKSLASH \ and FORWARDSLASH/ are not the same, have different functions

STRING THAT WORKS:
	
	const goodStr = 'Jake asks Finn, "Hey, let\'s go on an adventure!"';
	
STRING THAT DOESN'T WORK:

	const badStr = 'Finn responds, "Let's go!"';
	
FIXED STRING FROM ABOVE:

	const badStr = 'Finn responds, "Let/'s go!"';
	
==============================
	
	const myStr = "<a href=\"http://www.example.com\" target=\"_blank\">Link</a>";
	
	const myStr = '<a href="http://www.example.com" target="_blank">Link</a>';
	
[Both ^^^above yield same result]

=============================

<h3>ESCAPE SEQUENCES IN STRINGS</h3>

SITUATIONS WHERE YOU COULD NEED A BACKSLASH ESCAPE\ TO CONTINUE A STRING, TO PREVENT A STRING FROM ENDING EARLIER THAN INTENDED:

	\' single quote
	\" double quote
	\\ backslash
	\n newline
	\t tab
	\r carriage return
	\b word boundry
	\f form feed
	
-BACKSLASH needs to be ESCAPED to be able to display a BACKSLASH in the JavaScript editor
-when using above listed ESCAPEs, THERE SHOULD BE NO SPACES BETWEEN PREVIOUS CHARACTER TO THE LEFT AND THE FOLLOWING BACKSLASH
[example: FirstLine\n\t\SecondLine]

[\n NEWLINE indicates end of a line, starts a new line]
[\r CARRIAGE RETURN commands cursor to go to leftmost position]
[both \n and \r are functionally similar in JavaScript?]

	const myStr = "FirstLine\n\t\\SecondLine\nThirdLine";


	FirstLine
		\SecondLine
	ThirdLine
[above string yields the text arrangement immediately below the string]

-USE ESCAPES TO ARRANGE TEXT USING STRINGS

<h3>CONCATENATING STRINGS WITH PLUS OPERATOR +</h3>

-in JavaScript the PLUS OPERATOR + is used with string values it becomes the CONCATENATION OPERATOR
-CONCATENATION is COMBINING MULTIPLE STRINGS

	'My name is Alan,' + ' I concatenate.';
	
===============================================
-SPACES ARE REQUIRED WITHIN CONCATENATED STRINGS FOR THE SPACE TO BE DISPLAYED IN THE CONSOLE

WITH SPACE ADDED:

	'My name is Alan,' + ' I concatenate.';
[above yields: "My name is Alan, I concatenate."]

WITHOUT SPACE ADDED:

	'My name is Alan,' + 'I concatenate.';
[above yields: "My name is Alan,I concatenate"]
	
===========================================
	
	const ourStr = "I come first. " + "I come second.";
[above yields in console: "I come first. I come second."]

	const myStr = "This is the start. " + "This is the end.";
[yields: "This is the start. This is the end."]

<h3>CONCATENATING STRINGS WITH PLUS EQUALS OPERATOR +=</h3>

-use PLUS EQUALS OPERATOR += to concatenate a string onto an existing string
-You do this to break up one long string into several lines

ORIGINAL LONG STRING:
	
	let ourStr = "I come first. I come second."

LONG STRING BROKEN DOWN INTO CONCATENATED STRINGS ACROSS MULTIPLE LINES:

	let ourStr = "I come first. ";
	ourStr += "I come second."
[ourStr has a value of: "I come first. I come second."]


BEFORE CONCATENATION:

	let myStr = "This is the first sentence. This is the second sentence.";

AFTER CONCATENATION:

	let myStr = "This is the first sentence. ";
	myStr += "This is the second sentence.";


<h3>CONSTRUCTING STRINGS WITH VARIABLES</h3>

-may need to build strings using CONCATENATOR PERATOR +
-can insert one or more variable into a string you're building
-may be useful for combining previously established strings/values with new strings/values, adding on, building up

	const ourName = "freeCodeCamp";
	const ourStr = "Hello, our name is " + ourName + ", how are your?";
[value of ourStr in console: Hello, our name is freeCodeCamp, how are you?]

	const myName = "Jimmy James";
	const myStr = "My name is " + myName + "and I am well!";
	

<h3>APPENDING VARIABLES TO STRINGS WITH +=</h3>

-APPENDING is adding onto [in a non mathematical number + number way] 
-Think: adjective modfies/describes a noun
-APPEND strings using PLUS EQUALS OPERATOR +=

	const anAdjective = "awesome!";
	let ourStr = "Food is ";
	ourStr += anAdjective;
[in console, ourStr has a value of "Food is awesome!"]

	const someAdjective = "fun";
	let myStr = "Learning to code is ";
	myStr += someAdjective;
[myStr's new value is "Learning to code is fun"]

-variable defined with "const" cannot be overwritten, but can be added onto/APPENDED onto a variable defined with "let"
-variable defined with "let" can be changed via APPENDING, but cannot be overwritten by trying to define the same variable with "let" later on in the code
-If you want to change the value of variable defined with "let", it needs to be changed at the original point of being defined with "let" or APPENDED with +=

<h3>FIND THE LENGTH OF A STRING</h3>

-find the length of a STRING value by writing ".length" after the STRING VARIABLE or STRING LITERAL

	console.log("Alan Peter".length);
[the value "10" would be displayed in the console, SPACES COUNT TOWARDS CHARACTER COUNT]
[ping the console ---> console.log()]

	const firstName = "Ada";
	console.log(firstName.length);
	
	
	// Setup
let lastNameLength = 0;
const lastName = "Lovelace";

// Only change code below this line
lastNameLength = lastName.length;

<h3>USE BRACKET NOTATION TO FIND THE FIRST CHARACTER OF A STRING</h3>

-most modern programming languages [JavaScript included] START COUNTING FROM ZERO 0, NOT FROM 1
-style of counting is called ZERO-BASED INDEXING

	Charles
[character at index 0 of word: "Charles" is "C"]
[character at index 1 of word: "Charles" is "h"]

	const firstName = Charles;
	const firstLetter = firstName[0];
[variable: "firstLetter" would have a value of string: "C"]

	let firstLetterOfLastName = "";
	const lastName = "Lovelace";
	
	firstLetterOfLastName = lastName[0]
[value of "firstLetterOfLastName" is set to "L"]

<h3>STRING IMMUTABILITY</h3>

-in JavaScript STRING values are IMMUTABLE
-IMMUTABLE means you CANNOT ALTER/CHANGE THEIR PARTS AFTER CREATING THEM
-you CAN however REASSIGN values for STRINGS [as in: rewrite the entire string]

ATTEMPT TO ALTER PART OF A STRING:

	let myStr = "Bob";
	myStr[0] = "J";
[gives ERROR because the "B" in the STRING "Bob" cannot be changed]

REASSIGN THE WHOLE STRING:

	let myStr = "Bob";
	myStr = "Job";
[does NOT give an error because the whole string is being changed, not just one character]

		let myStr = "Jello World";
		myStr = "Hello World";
[no error above]

<h3>USE BRACKET NOTATION TO FIND THE Nth CHARACTER IN A STRING</h3>

-BRACKET NOTATION can be used to find the value of any character[n] within a STRING
-JavaScript starts counting from 0

	const firstName = "Ada";
	const secondLetterOfFirstName = firstName[1];
[secondLetterOfFirstName has a value of string: "d"]

	const lastName = "Lovelace"
	const thirdLetterOfLastName = lastName[2]
[thirdLetterOfLastName has a value of string: "v",]
[set thirdLetterOfLastName to value of third character of lastName: count 0(L),1(o),2(v)]

<h3>USE BRACKET NOTATION TO FIND THE LAST CHARACTER IN A STRING</h3>

-to find the LAST CHARACTER of a STRING, SUBTRACT one from the string's total length [total character count]
-use function: firstName[firstName.length - 1]

	const firstName = "Ada";
	const lastLetter = firstName[firstName.length - 1];
[lastLetter has a value of string: "a"]

	const lastLetterOfLastName = lastName[lastName.length - 1];
	
	
<h3>USE BRACKET NOTATION TO FIND THE Nth-TO-LAST CHARACTER IN A STRING</h3>

-find third-to-last letter of a string: firstName[firstName.length - 3];

	const firstName = "Augusta";
	const thirdToLastLetter = firstName[firstName.length - 3];
[thirdToLastLetter value is string: "s"]

	const lastName = "Lovelace";
	const secondToLastLetter = lastName[lastName.length - 2];
[secondToLastLetter's value is string: "c"]

<h3>WORD BLANKS</h3>

-use STRING CONCATENATION OPERATOR + to build new string
-fill in blanks in sentences with STRINGS [think adlibs]


It was really __, and we__ ourselves__.
	
	const = "It was really " + "hot" + ", and we " + "laughed" + " ourselves " + "silly" + ".";
	
	const wordBlanks = "The " + myAdjective + " " + myNoun + " " myVerb + " " + myAdverb + "."; // Change this line
	
	var wordBlanks = "The " + myAdjective + " " + myNoun + " " + myVerb + " " + myAdverb + "."; // Only change this line;
	
	
<h3>STORE MULTIPLE VALUES IN ONE VARIABLE USING JAVASCRIPT ARRAYS</h3>

-ARRAY variable lets you store multiple pieces of info in one place
-ARRAY declaration begins and ends with square brackets [] and seperate strings with comma and space
-STRINGS are surrounded by quotes ""
-NUMBERS are NOT surrounded by quotes

	const sandwich = ["peanut butter", "jelly", "bread"];
	
	const myArray = ["yes", 10];
	
<h3>NEST ONE ARRAY WITHIN ANOTHER ARRAY</h3>

-also called a MULTI-DIMENSIONAL ARRAY
-use square brackets within square brackets sperated by comma and space [[   ], [   ]]

	const teams = [["Bulls", 23], ["White Sox", 45]];
	
	const myArray = [["yes", 2], ["no", 5]];
	
<h3>ACCESS ARRAY DATA WITH INDEXES</h3>

-ARRAY INDEXES are also written in square brackets
-ARRAY INDEXES specify an entry in the array
-STRINGS specify a character
-ARRAYs use zero-based indexing, start counting at zero 0

	const array = [50, 60, 70];
	console.log(array[0]);
	const data = array[1];
[console.log(array[0]) prints 50]
[varable: "data" has a value of 60]
[in "array", "50" is located at index: 0, "60" is at index: 1, "70" is at index: 2]

	const myArray = [50, 60, 70];
	let myData = myArray[0];
[value of myData is 50]

-when defining a variable as an index within an array start the line with "let, const, var"

<h3>MODIFY ARRAY DATA WITH INDEXES</h3>

-STRINGS are IMMUTABLE
-ENTRIES of ARRAYS are MUTABLE, can be changed even if the array was declared with "const"
-MUTABLE = can be changed freely

	const ourArray = [50, 40, 30];
	ourArray[0] = 15;
[ourArray's value at index: 0 was changed from 50 to 15.]
[ourArray's new value is [15, 40, 30]]

-when defining an array index [like using command "ourArray[0]"] there should not be a space between "ourArray" and the following square bracket for SAKE OF CLARITY when others read your code
-JavaScript can process both [ourArray[0]] and [ourArray [0]] in the same way, but it is less confusing for programmers to read the first method

	const myArray = [18, 64, 99];
	myArray[0] = 45;
[myArray's value at index: 0 was changed from 18 to 45, myArray's value is now [45, 64, 99]]

-when modifying an index within an array, do not start the line by defining with "let, const, var"

<h3>ACCESS MULTI-DIMENSIONAL ARRAYS WITH INDEXES</h3>

-a MULTI-DIMENSIONAL ARRAY is an "ARRAY OF ARRAYS"
-use square brackets to access an array

	const arr = [
	[1, 2, 3],              <-----array 0
	[4, 5, 6],              <-----array 1
	[7, 8, 9],              <-----array 2
	[[10, 11, 12], 13, 14]  <-----array 3
	];
	
	const subarray = arr[3];
	const nestedSubarray = arr[3][0];
	const element = arr[3][0][1];
(subarray has a value of [[10, 11, 12], 13, 14])
(nestedSubarray has a value of [10, 11, 12])
(element has a value of 11)

THREE POSSIBLE BRACKETS WITHIN COMMAND "arrayName[n][n][n]""

-first bracket selects number of array [see: arrows above^^^]

-second bracket selects the SUBARRAY [which specific array within the array selected via first bracket]
(within array 3: "[[10, 11, 12], 13, 14]", the array:"[10, 11, 12]" is array index: 0)

-third bracked selects INDEX value WITHIN selected subarray
(in array 3: [[10, 11, 12], 13, 14], inside of subarray index: 0 "[10, 11, 12]", the number "11" is index: 1)

	const myArray = [
  [1, 2, 3],
  	[4, 5, 6],
  	[7, 8, 9],
  	[[10, 11, 12], 13, 14],
	];

	const myData = myArray[2][1];
(value of myArray is 8)

<h3>MANIPULATE ARRAYS WITH push()</h3>

-APPEND data to the END of an ARRAY with "push()" function

- .push() takes one or more PARAMETERS and "pushes" them onto the END of an ARRAY

-PARAMERTS can be numbers, variables, arrays, strings, nested arrays [array within an array, multi-dimensional array]

	const arr1 = [1, 2, 3];
	arr1.push(4);
[arr1.push(4) inserts number value: 4 to the end/rightmost position of the array]
(arr1's new value is [1, 2, 3, 4])

	const arr2 = ["Stimpson", "J", "cat"];
	arr2.push(["happy", "joy"]);
[arr2.push(["happy", "joy"]) inserts array: ["happy", "joy"] into the last/rightmost position of array: arr2]
(arr2's new value is ["Stimpson", "J", "cat", "happy", "joy"])

	const myArray = [["John", 23], ["cat", 2]];
	myArray.push(["dog", 3])
(myArray's new value is [["John", 23], ["cat", 2], ["dog", 3]])

<h3>MANIPULATE ARRAYS WITH .pop()</h3>

-.pop() function pops off a value from the end of an array [removes the value and can store it]
-you can run .pop() without putting a value into the parentheses () since pop() always removes the last/rightmost value
-console.log() is used to CHECK THE CURRENT VALUE OF A VARIABLE

	const threeArr = [1, 4, 6];
	const oneDown = threeArr.pop();
	console.log(oneDown);
	console.log(threeArr);
[console.log(oneDown) says value of oneDown is 6]
(console.log(threeArr) says value of threeArr is [1, 4])
[VALUE 6 was REMOVED/"popped' from array threeArr and stored/assigned to variable oneDown]
	
-two console.log() commands were used so you can: 
1. VERIFY the value 6 was "popped"/removed from array: threeArr
2. VERIFY value 6 is now assigned to oneDown/oneDown is now defined as value 6

	const myArray = [["John", 23], ["cat", 2]];
	const removedFromMyArray = myArray.pop()
[value/array: ["cat, 2"] was removed from myArray and assigned to removedFromMyArray]

<h3>CHECK THE CURRENT ASSIGNED VALUE OF A VARIABLE WITH console.log()</h3>

-useful for checking if THE COMMANDS YOU ENTERED EXECUTED CORRECTLY

	const variableOne = [5, 6, "green"];
	console.log(variableOne)
[console.log(variableOne) will say variableOne has a value of [5, 6, "green"]]

	const variableOne = [5, 6, "green"];
	variableOne.pop()
	console.log(variableOne)
[console.log(variableOne) should say the current value of variableOne after the pop() command is [5, 6]]

<h3>MANIPULATE ARRAYS WITH .shift()</h3>

- .shift() removes the FIRST/leftmost element of an array, index: 0

	const ourArray = ["Stimpson", "J", ["cat"]];
	const removedFromOurArray = ourArray.shift();
[removedFromOurArray's value is now "Stimpson"]
(ourArray's value is now ["J", ["cat"]])

	const myArray = [["John", 23], ["dog", 3]];
	const removedFromMyArray = myArray.shift();
	
	
<h3>MANIPULATE ARRAYS WITH .unshift()</h3>

- .unshift() INSERTS an element into the BEGINNING/leftmost position of an array, index:0
- .unshift() and .push() are opposites
- YOU NEED TO SPECIFY IN PARENTHESES () WHAT ELEMENT/VALUE TO INSERT VIA .unshift()

	const ourArray = ["Stimpson", "j", "cat"];
	ourArray.shift();
	ourArray.unshift("Happy");
(ourArray now has a value of ["Happy", "J", "cat"])
[.shift() removes "Stimpson"]
[.unshift inserts "Happy" in front]

	const myArray = [["John", 23], ["dog", 3]];
	myArray.shift();
	myArray.unshift(["Paul", 35]);

MANIPULATE SUMMARY
.push() insert element to rightmost/last index of array, specify what you want to insert/add within parentheses
.pop() remove element from rightmost/last index of array
.shift() remove element from leftmost/first index of array, index 0 
.unshift() insert element to leftmost/first index of array, index: 0

<h3>SHOPPING LIST</h3>
task: 5 itens in array, first index of each needs to be a string, second needs to be a number

	const myList = [["Chocolate Bar", 15], ["Bread", 1], ["Milk", 2], ["Eggs", 3], ["Lettuce", 5]];

<h3>WRITE REUSABLE JAVASCRIPT CODE WITH FUNCTIONS</h3>

-FUNCTIONS are bits of REUSABLE CODE
-divide code into FUNCTIONS to save time later

Example function:

	function functionName() {
  console.log("Hello World");
}

-define function with [function functionName() {}]
-operations within the curly bracket {} will be executed when you INVOKE/CALL the function
-You can call or INVOKE a function by using its NAME followed by PARENTHESES: functionName();
-above function writes "Hello World" in the console when INVOKED/CALLED

	function reusableFunction() {
  console.log("Hi World")
}
	reusableFunction();
[INVOKING the function causes "Hi World" to be written in the console]

<h3>PASSING VALUES TO FUNCTIONS WITH ARGUMENTS</h3>

-PARAMETERS are variables that act as placeholders for values that are to be input into a FUNCTION when the FUNCTION is CALLED

BASE TEMPLATE FOR FUNCTION:

function testFun(param1, param2) {
  console.log(param1, param2);
}

CALL THE FUNCTION WITH FILLED IN PARAMETERS:

	testFun("Hello", "World");
	
-two STRING ARGUMENTS were passed through the FUNCTION: "Hello" and "World"

"Hello" = param1
"World" = param2

-you can CALL the same FUNCTION with two different STRING values for each parameter, and each parameter will become whatever STRING values/ARGUMENTS are passed through

-NO SEMICOLON WHEN DEFINING A FUNCTION, ONLY CURLY BRACKET: function functionName(a, b) {}

<h3>RETURN A VALUE FROM A FUNCTION WITH RETURN</h3>

We can pass values into a function with arguments. You can use a return statement to send a value back out of a function.

	function plusThree(num) {
  return num + 3;
}

	const answer = plusThree(5);
	
-variable "answer" has a value of 8

-function plusThree takes an ARGUMENT for "num" and returns a value equal to "num + 3"

	function timesFive(num) {
  return num * 5;
}
	const answer = timesFive(4);

-value of answer is 20
-function timesFive would multiply 4 by 5 [4 * 5 = 20]

<h3>GLOBAL SCOPE AND FUNCTIONS</h3>

-SCOPE refers to the visibility of variables

-VARIABLES which are defined outside of a function have GLOBAL SCOPE

-GLOBAL SCOPE = being able to be seen everywhere/be visable from everywhere in your JavaScript code

-VARIABLES that are declared WITHOUT "let" or "const" automatically are created within the GLOBAL SCOPE [this can lead to UNEXPECTED CONSEQUENCES ELSWERE IN YOUR CODE or WHEN RUNNING A FUNCTION AGAIN]

-ALWAYS declare variables with "let" or "const" to avoid potential issues later

	// Declare the myGlobal variable below this line
const myGlobal = 10

function fun1() {
  // Assign 5 to oopsGlobal here
oopsGlobal = 5
}

// Only change code above this line

function fun2() {
  let output = "";
  if (typeof myGlobal != "undefined") {
    output += "myGlobal: " + myGlobal;
  }
  if (typeof oopsGlobal != "undefined") {
    output += " oopsGlobal: " + oopsGlobal;
  }
  console.log(output);
}

<h3>LOCAL SCOPE AND FUNCTIONS</h3>

-when variables are declared within a function or are function parameters they have LOCAL SCOPE

-LOCAL SCOPE = only visable within a specific function

	function myTest() {
 	 const loc = "foo";
	  console.log(loc);
	}

	myTest();
	console.log(loc);

[function: myTest(); will display the string "foo" in the console]
[function: console.log(loc); will display an error in the console because the function is being executed from a GLOBAL SCOPE whereas variable "loc" is only visable LOCALLY within function: myTest()]

[variable: "loc" is only declared within a function so IT CAN be checked with console.log(loc) inside of its contained function (myTest), but CANNOT be checked with console.log(log) OUTSIDE of the function]

<h3>GLOBAL VS. LOCAL SCOPE IN FUNCTIONS</h3>

-it is possible to have both LOCAL and GLOBAL variables with the SAME NAME

-when there are LOCAL and GLOBAL variables sharing the same name, the LOCAL VARIABLE TAKES PRECEDENCE OVER THE GLOBAL VARIABLE (local = variable within a function)

	const someVar = "Hat";    <----GLOBAL VARIABLE

	function myFun() {
	  const someVar = "Head"; <----LOCAL VARIABLE
	  return someVar;
	}
	
[running function: myFun() will return the string "Head" because the LOCAL version of myFun is defined with "Head"]

	// Setup
	const outerWear = "T-Shirt";

	function myOutfit() {
 	 // Only change code below this line
	const outerWear = "sweater"
 	 // Only change code above this line
 	 return outerWear;
	}

	myOutfit();
[running function: myOutfit(); will return the string value: "sweater", LOCAL variable value OVERWRITES the GLOBAL variable value]


<h3>RETURN STATEMENT AT THE END OF A FUNCTION</h3>

-RETURN STATEMENT = the last line of a function, should look like:
	
	return expression
	
-"expression" in the above can be a mathematic expression with variables defined in the containing function
	
	var res = function(x,y);

	return x + y
-Think of above return statement as: **"return/stop the function when the value for x is added to the value for y"**

-RETURN interrupts a function, the function stops executing when it runs into a RETURN statement
-RETURN statements are used to PREVENT INFINITE LOOPS, by stating a specific stopping point: "when this function reaches this value, it will terminate/stop" [with imaginary numbers]
-if a return statement is not used the function may be run infinitely, and will return the value "undefined" instead of a specific number or string



EXAMPLE:

=====================
	<!DOCTYPE html>   
<html>   
  
<head>   
</head>   
  
<body>  
  
<h2> Welcome to the javaTpoint.com </h2>  
<h3> Example of the JavaScript's return statement </h3>  
    <script>   
var res = fun(12, 30);  
function fun(x, y)  
{  
return x * y;  
}  
document.write(res);  
    </script>   
</body>   
  
</html>  
=======================================

[above example: use return to return the result of the product of two numbers. The resulting value is returned back to the function caller]
[The function runs the math and gets an answer, the answer is then used as the next input for the function, the function runs again and repeats with each new answer.]
[variable: res is the FUNCTION CALLER]
[FUNCTION CALLER: res is calling the function: fun() while passing two integers (usining parentheses parameters (x, y) as arguments of the function]
[RETURN can determine what operations happen to parameters of a function (x,y), in this case, return says to multiply x and y]
[the result value of "res" calling fucntion: fun() is stored as "res" 's new value]
[the RETURN STATEMENT "return x * y" says to stop the function when the two parameters: (x,y) or (12,30) are multiplied once]
[if there was no stopping point specified in the RETURN STATMENT, the function will run over and over indefinitely/infinitely and will give an answer of: undefined because there cannot be an end if it runs infinitely]
[output value after the function is run/called is 360. 12 * 30 = 360. ]


<h3>UNDERSTANDING UNDEFINED VALUE RETURNED FROM A FUNCTION</h3>


-a function can include the RETURN statement, but it does not have to.

-if a function doesn't have a RETURN statement, when you call the function, it will process the inner contained code with a returned value of UNDEFINED.

	let sum = 0;

	function addSum(num) {
  	sum = sum + num;
	}

	addSum(3);
	
[function: addSum is a function without a return statement, it will change the GLOBAL variable: sum, but the returned value of the function will be UNDEFINED]

	// Setup
let sum = 0;

function addThree() {
  sum = sum + 3;
}

// Only change code below this line
function addFive() {
  sum = sum + 5;
}

// Only change code above this line

addThree();
addFive();

[running function addFive returns a value of: undefined because no RETURN STATEMENT was specified at the end of the function]

<h3>ASSIGNMENT WITH A RETURNED VALUE</h3>

-everything to the right of the equal sign is resolved before the value is assigned to the variable

-because of above statement^^^ we can take the RETURN value of a function and ASSIGN it to a VARIABLE

	
	var answ = sum(1 + 2);
	function sum(x,y){
	
	return x + y;
	}
	
[variable: answ's new assigned value would be 3]

	let processed = 0;
	
	function processArg(num) {
	return (num + 3) / 5;
	}
	
	processed = process arg(7); // <---runs function and stores answer value as variable: processed
	console.log(processed) <---shows answer/new assigned value for processed in console
[console would show varable: processed's value is now 2]
[(7 + 3) / 5 = 2]

<h3>STAND IN LINE</h3>

-QUEUE = abstract data structure where items are kept in order, a line, standing in line, an order in which tasks/operations are completed [standing in line at the grocery store to pay for your stuff]
-NEW ITEMS are added to the BACK of the QUEUE, OLD ITEMS are taken off of the FRONT of the QUEUE


	function nextInLine(arr, item) {
  // Only change code below this line
  arr.push(item);  // <---.push adds item to the end of the array, pushes "item" to the end of "arr"
  const removed = arr.shift(); // <---.shift removes first element of an array and returns element removed
  return removed; // <---stops function when any value is removed, variable: removed is optional, can also return the removed element with "arr.shift();"
  // Only change code above this line
}

// Setup
let testArr = [1, 2, 3, 4, 5];

// Display code
console.log("Before: " + JSON.stringify(testArr)); //<--- shows array values in console BEFORE changes are made
console.log(nextInLine(testArr, 6)); //<---[WHERE THE FUNCTION IS BEING RUN FROM, WHERE THE 6 IN THE RESULTS SHOWED UP FROM AND HOW FUNCTION KNOWS TO USE testArr as "arr"] says to pass 6 through parameter: item for array: testArr
console.log("After: " + JSON.stringify(testArr)); //<---shows array values in console AFTER changes are made
[JSON.stringify changes array into viewable in the console]

["arr" and "item" are placeholder variables, they can be anything, but those two specifically were given in the question prompt]
[function returns the first item on the list and adds an item at the end of the list]

Below: same code no notes

=============================

	function nextInLine(arr, item) {
  // Only change code below this line
  
  	arr.push(item);
 	 const removed = arr.shift();
 	 return removed;
	 
  // Only change code above this line
}

// Setup
	let testArr = [1, 2, 3, 4, 5];

// Display code

	console.log("Before: " + JSON.stringify(testArr));
	console.log(nextInLine(testArr, 6));
	console.log("After: " + JSON.stringify(testArr));

=====================

RESULTS SHOWN IN CONSOLE:

// running tests
// tests completed
// console output
Before: [1,2,3,4,5]
1                  <-------returned first item
After: [2,3,4,5,6]


PROMPT CHECKLIST:

nextInLine([], 5) should return a number.
Passed:nextInLine([], 1) should return 1
Passed:nextInLine([2], 1) should return 2
Passed:nextInLine([5,6,7,8,9], 1) should return 5
Passed:After nextInLine(testArr, 10), testArr[4] should be 10

<h3>UNDERSTANDING BOOLEAN VALUES</h3>

-BOOLEAN VALUES can only be TRUE or FALSE
-"an on-off switch" true = on, false = off
-the two states: TRUE and FALSE are MUTUALLY EXCLUSIVE [one BOOLEAN cannot be TRUE AND FALSE at the same time]
-BOOLEAN VALUES are NEVER written with quotes
-"true" and "false" are STRINGS, NOT BOOLEAN VALUES
-true and false are BOOLEAN VALUES, they have special meaning in JavaScript

	function welcomeToBooleans() {
	
	return false;
	}
	console.log(welcomeToBooleans());
[when you run wecomeToBooleans via console.log, the value displayed in the console is false]

	function welcomeToBooleans() {
	
	return true;
	}
	console.log(welcomeToBooleans());
[when you run wecomeToBooleans via console.log, the value displayed in the console is true]
[you can code a button press with something similar to above^^^, button press runs function, result true can be light turns on, result false can be light turns off]

<h3>USE CONDITIONAL LOGIC WITH IF STATEMENTS</h3>

-"if" statments are used to make decisions in code [like a checklist of yes or no questions]
-"if" keyword tells JavaScript to execute code in the curly braces under CERTAIN CONDITIONS that are defined within the parentheses
-CERTAIN CONDITIONS = BOOLEANS
-BOOLEANS can only be true or false
-when condition evaluates to TRUE the program executes the statement inside the curly braces
-when condition evaluates to FALSE the program DOES NOT execute the statement inside the curly braces

PSUEDOCODE:
	
	if (condition is true) {
		statement is executed
	}
	
EXAMPLE:

	function test (myCondition) {
	  if (myCondition) {   //<---"if" = boolean, requires parentheses value of function to be true or false
    return "It was true"; //<--first "return statement" is determines action after: true
  }
	  return "It was false";  //<--second "return statement" is determines action after: false
}

test(true); //  <---returns "it was true" in console
test(false); //<---returns "it was false" in console

=======================================

	function trueOrFalse(wasThatTrue) {
  // Only change code below this line
  if (wasThatTrue) {
    return "Yes, that was true" //<---inside its own curly brace, true result
  }
  return "No, that was false" //<---not inside its own curly brace, false result

  // Only change code above this line

}

console.log(trueOrFalse(true))
[displays/returns: "Yes, that was true" in console]
console.log(trueOrFalse(false))
[displays/returns: "No, that was false" in console]

<h3>COMPARISON WITH THE EQUALITY OPERATOR</h3>

-JavaScript has many COMPARISON OPERATORS
-COMPARISON OPERATORS return a BOOLEAN true or false value

-most basic operator: EQUALITY OPERATOR "=="
-EQUALITY OPERATOR "==" compares two values and RETURNS true if they are EQUIVALENT or false if they are NOT EQUIVALENT
-EQUALITY OPERATOR "==" attempts to CONVERT both values being compared to a common data type
-using EQUALITY OPERATOR "==", strings and numbers CAN be equivalent [example: 2 == "2" // true]
-single equal sign means ASSIGNMENT "=", assigns value to a variable
-double equal sign means EQUALITY "==" checks if two values are equal/the same value

	function equalityTest(myVal) {
  	if (myVal == 10) {
    return "Equal";  //<---code is INSIDE curly braces, represents result if true
 	 }
 	 return "Not Equal"; //<---code is NOT INSIDE curly braces, represents result if false
	}  //<---outer curly brace
[first return is within its own curly braces: 
{{return "Equal";} return "Not Equal"}, code within its own curly brace executes if myVal is true]
[if myVal is equal to 10, the equality operator returns true]
[if true, then "Equal" returned in console, in context: true is only when myVal's value is 10]
[if false, then "Not Equal" returned in console, in context: false is when myVal's value is any number that is not 10]

-for JavaScript to be able to compare two DIFFFERENT data types [example: numbers and strings] it needs to convert one type to another type
-TYPE COERCION = converting data from one type to another

1 == 1 // true // <--1 and 1 are the same number
1 == 2 // false // <--1 and 2 are not the same number
1 == "1" // true // <-- first 1 is a number, second "1" is a string, both are 1
"3" == 3 // true // <--same as previous, "3" and 3 are both 3

=============

	// Setup
function testEqual(val) {
  if (val == 12)  { // Change this line
    return "Equal";
  }
  return "Not Equal";
}

console.log(testEqual(10));
[console log says "Not Equal" because 10 == 12 // false]

<h3>COMPARISON WITH THE STRICT EQUALITY OPERATOR</h3>

-STRICT EQUALITY OPERATOR "===" checks for equality of two compared values, but DOES NOT attempt to convert the two values to a common data type

-using STRICT EQUALITY OPERATOR "===", strings and numbers CANNOT be equivalent [example: 2 === "2" // false, 2 === 2 // true]
-STRICT EQUALITY OPERATOR "===" always considers data of two different data types to be false

3 === 3 // true // <-- two same data types: both numbers
3 === "3" // false // <-- two different data types: number and string 

======================

// Setup
function testStrict(val) {
  if (val === 7) { // Change this line
    return "Equal";
  }
  return "Not Equal";
}

console.log(testStrict(10));
[console returns "Not Equal" because 10 === 7 // false]


<h3>PRACTICE COMPARING DIFFERENT VALUES</h3>

- use "typeof" operator in JavaScript to determine the data type of a variable

		typeof 3
[console returns the string: "number"]

	typeof '3'
[console returns the string: "string"]

// Setup
function compareEquality(a, b) {
  if (a === b) { // Change this line
    return "Equal";
  }
  return "Not Equal";
}

console.log(compareEquality(10, "10"));
[console returns: "Not Equal"]

<h3>COMPARISON WITH THE INEQUALITY OPERATOR</h3>

-the INEQUALITY OPERATOR "!=" is the OPPOSITE of the EQUALITY OPERATOR, means not equal
-returns false if values are EQUAL
-returns true if values ARE NOT EQUAL
-attempts to CONVERT DATA TYPES, two values with two different data types CAN BE FALSE [false in context means they are equal when using inequality operator]

	1 != 2 // true
	1 != "1" // false
	1 != '1' // false
	1 != true // false
	0 != false // false
	
	
// Setup
function testNotEqual(val) {
  if (val != 99) { // Change this line
    return "Not Equal"; //  <--- if true
  }
  return "Equal"; // <--- if false
}

console.log(testNotEqual(10));
[console log returns "Not Equal" because it is TRUE that 10 and 99 are not equal]

<h3>COMPARISON WITH THE STRICT INEQUALITY OPERATOR</h3>

-STRICT INEQUALITY OPERATOR !== is same as INEQUALITY OPERATOR, but DOES NOT convert data types
-opposite of STRICT EQUALITY OPERATOR
-only returns FALSE if both values have THE SAME DATA TYPE
-every other situation returns TRUE

	3 !== 3 // false
	3 !== '3' // true
	4 !== 3 // true
	
	
// Setup
function testStrictNotEqual(val) {
  if (val !== 17) { // Change this line
    return "Not Equal";
  }
  return "Equal";
}

console.log(testStrictNotEqual(10));
[console log returns: "Not Equal"]

<h3>COMPARISON WITH THE GREATER THAN OPERATOR</h3>

-GREATER THAN OPERATOR ">" compares two values of NUMBERS
-if value left of ">" is greater then TRUE
-if value left of ">" is less then FALSE
-WILL CONVERT DATA TYPES, can accept NUMBERS and STRINGS

	5 > 3 // true
	7 > '3' // true
	2 > 3 // false
	'1' > 9 // false
	
	
	function testGreaterThan(val) {
  if (val > 100) {  // Change this line
    return "Over 100";
  }

  if (val > 10) {  // Change this line
    return "Over 10";
  }

  return "10 or Under";
}

console.log(testGreaterThan(10));
[console returns: "10 or under"]

<h3>COMPARISON WITH THE GREATER THAN OR EQUAL TO OPERATOR</h3>

GREATER THAN OR EQUAL TO ">="

-compares two numbers
-WILL CONVERT DATA TYPES WHEN COMPARING
-accepts STRINGS and NUMBERS

	6 >= 6 // true
	7 >= '3' // true
	2 >= 3 // false
	'7' >= 9 // false
	
	
function testGreaterOrEqual(val) {
  if (val >= 20) {  // Change this line
    return "20 or Over";
  }

  if (val >= 10) {  // Change this line
    return "10 or Over";
  }

  return "Less than 10";
}

console.log(testGreaterOrEqual(10));
[console returns: "10 or Over"]

<h3>COMPARISON WITH THE LESS THAN OPERATOR</h3>

LESS THAN "<"

-compares two numbers
-converts between data types
-accepts STRINGS and NUMBERS

	2 < 5 // true
	'3' < 7 // true
	5 < 5 // false
	3 < 2 // false
	'8' < 4 // false
	
function testLessThan(val) {
  if (val < 25) {  // Change this line
    return "Under 25";
  }

  if (val < 55) {  // Change this line
    return "Under 55";
  }

  return "55 or Over";
}

console.log(testLessThan(10));
[console returns: "Under 25"]


<h3>COMPARISON WITH THE LESS THAN OR EQUAL TO OPERATOR</h3>

LESS THAN OR EQUAL TO "<="

-compares two numbers
-converts between data types
-accepts STRINGS and NUMBERS

	4 <= 5 // true
	'7' <= 7 // true
	5 <= 5 // true
	3 <= 2 // false
	'8' <= 4 // false
	

function testLessOrEqual(val) {
  if (val <= 12) {  // Change this line
    return "Smaller Than or Equal to 12";
  }

  if (val<= 24) {  // Change this line
    return "Smaller Than or Equal to 24";
  }

  return "More Than 24";
}

console.log(testLessOrEqual(10));
[console returns: "Smaller Than or Equal to 12"]


<h3>COMPARISON WITH THE "LOGICAL AND" OPERATOR</h3>

LOGICAL AND "&&"

-test more than one thing at a time with booleans
-can nest multiple if statements within curly braces
-&& returns true IF AND ONLY IF the operands to the left and right of it are true

TWO WAYS OF WRITING  A STATEMENT:

#1:
if (num > 5) {
  if (num < 10) {
    return "Yes";
  }
}
return "No";
[will only return "Yes" if variable: num is greater than 5 AND less than 10]

#2 using LOGICAL AND operator:

if (num > 5 && num < 10) {
  return "Yes";
}
return "No";
[same as above, values to the left and right of && must both be true for the end result to be true, in context: return "Yes"]

======================

function testLogicalAnd(val) {
  // Only change code below this line

  if (val <= 50 && val >= 25) {
     {
      return "Yes";
    }
  }

  // Only change code above this line
  return "No";
}

console.log(testLogicalAnd(10));
[console log returns: "No"]

<h3>COMPARISON WITH THE "LOGICAL OR" OPERATOR</h3>

LOGICAL OR "||" //<----------press shift + the key below backspace and above Enter key
"composed of two pipe symbols"

-returns TRUE if either of surrounding operands is true
-TRUE if AT LEAST ONE OF operations to left and right are TRUE

TWO WAYS OF WRITING SAME THING:

#1:

if (num > 10) {
  return "No";
}
if (num < 5) {
  return "No";
}
return "Yes";
[will return Yes if num's value is between 5 and 10, 5 and 10 included]

#2 with LOGICAL OR operator:

if (num > 10 || num < 5) {
  return "No";
}
return "Yes";

========================

function testLogicalOr(val) {
  // Only change code below this line

  if (val < 10 || val > 20) {
    return "Outside";
  }
  // Only change code above this line
  return "Inside";
}

console.log(testLogicalOr(15));
[console returns: Inside]

<h3>INTRODUCING ELSE STATEMENTS</h3>

-if statement executes code within curly brace IF STATEMENT IS TRUE
-ELSE statement executes code within curly brace IF STATEMENT IS FALSE
-use as a second option or a failsafe

	if (num > 10) {
  	return "Bigger than 10";
	} else {
  	return "10 or Less";
	}
[if true: returns "Bigger than 10"]
[if false: returns "10 or Less"]

================================

function testElse(val) {
  let result = "";
  // Only change code below this line

  if (val > 5) {
    result = "Bigger than 5";
  } else  {
    result = "5 or Smaller";
  }

  // Only change code above this line
  return result;
}

console.log(testElse(4));
[console log returns: "5 or Smaller" because result was false, 4 is not greater than 5]


<h3>INTRODUCING ELSE IF STATEMENTS</h3>

else if

-use ELSE IF if you need to have multiple conditions addressed
-CHAIN IF STATMENTS TOGETHER WITH ELSE IF

	if (num > 15) {            <--"if" statement #1
	  return "Bigger than 15";
	} else if (num < 5) {      <--"if" statement #2
 	 return "Smaller than 5";
	} else {
	  return "Between 5 and 15";
	}
	
	
====================================

function testElseIf(val) {
  if (val > 10) {
    return "Greater than 10";
  } else if (val < 5) {
    return "Smaller than 5";
  } else {
  return "Between 5 and 10";
}
}

console.log(testElseIf(7));
[console returns "Between 5 and 10"]


<h3>LOGICAL ORDER IN IF ELSE STATEMENTS</h3>

-ORDER is important in IF, ELSE IF statements

-function is executed from TOP TO BOTTOM checkin for numbers from LEAST TO GREATEST, lower number comparisons should be in lines higher than larger number comparisons 

-must be in INCREASING ORDER from TOP TO BOTTOM

x>1
x>2
x>3
x>4
x>5
[above logic WORKS CORRECTLY]
[above logical thought process: "is x greater than 1? Yes? Okay, next. Is x greater than 2? Yes. Next. Is x greater than 3? No. STOP.""

x>5
x>1
[above logic DOES NOT WORK CORRECTLY]
[above logical thought process: for x=6 "Is x greater than 5? Yes. STOP." "Why check if x is greater than 1 if you already know x is greater than 5, a larger number?"]


CODE WORKS CORRECTLY:

function foo(x) {
  if (x < 1) {
    return "Less than one";
  } else if (x < 2) {
    return "Less than two";
  } else {
    return "Greater than or equal to two";
  }
}
[will check for "if (x < 1)" then "if (x < 2)" because statements are in correct order: increasing from top to bottom, smallest value up top]

CODE DOES NOT WORK CORRECTLY:

function bar(x) {
  if (x < 2) {                       <---wrong order, only checks for this
    return "Less than two";
  } else if (x < 1) {
    return "Less than one";
  } else {
    return "Greater than or equal to two";
  }
}
[will only check for "if (x < 2)" because 2 is a larger number than 1]



function orderMyLogic(val) {
  if (val < 5) {
    return "Less than 5";
  } else if (val < 10) {
    return "Less than 10";
  } else {
    return "Greater than or equal to 10";
  }
}

console.log(orderMyLogic(7));
[console log returns: "Less than 10"]

<h3>CHAINING IF ELSE STATMENTS</h3>

if/else statements can be chained together for complex logic
-first statement is IF, all subsequent if statements are ELSE IF

PSUEDOCODE:

if (condition1) {
  statement1
} else if (condition2) {
  statement2
} else if (condition3) {
  statement3
. . .
} else {
  statementN
}

====================

function testSize(num) {
  // Only change code below this line
if (num < 5) {
  return "Tiny"
} else if (num < 10) {
  return "Small"
} else if (num < 15) {
  return "Medium"
} else if (num < 20) {
  return "Large"
} else if (num >=20) {
  return "Huge"
}

  // Only change code above this line
}

console.log(testSize(7));
[console log returns "Small" because 7 < 5 // false, 7 < 10 // true]
[runs the input "testSize(7)" against each parameter from top to bottom, moves onto the next parameter if the result is false until one of the statements is true or all parameters end up being false]

<h3>GOLF CODE</h3>
  
  const names = ["Hole-in-one!", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home!"];

function golfScore(par, strokes) {
  // Only change code below this line
  if (strokes == 1) {
    return names[0];
  } else if (strokes <= par - 2) {
    return names[1];
  } else if (strokes === par - 1) {
    return names[2];
  } else if (strokes === par) {
    return names[3];
  } else if (strokes === par + 1) {
    return names[4];
  } else if (strokes === par + 2) {
    return names[5];
  } else {
    return names[6];
  }
  // Only change code above this line
}

// Change these values to test
golfScore(5, 4);
 
 
 
 <h3>SELECTING FROM MANY OPTIONS WITH SWITCH STATEMENTS</h3>
 
-use "switch" if you have many options to choose from

-switch statement tests a value with many "case" statements that define different possible outcomes

-each statement BEGINS wtih "case" and ENDS with "break"
-code stops executing when "break" occurs, "break" tells JavaScript to stop executing statments
-if no "break", JavaScript will execute next line

switch (lowercaseLetter) {
	case "a":        <--------------COLON :
		console.log("A");
		break;
	case "b":
		console.log("B");
		break;
}

-"case" values in "switch" statements are tested with STRICT EQUALITY (===)

-EACH CASE STATEMENT ENDS WITH A REGULAR COLON : : : : : : : : : : : : : : :, NOT A SEMICOLON ;

-values following "case" can be NUMBERS or STRINGS

function caseInSwitch(val) {
  let answer = "";
  // Only change code below this line
  switch (val) {
    case 1:
      answer = "alpha";
      break;
    case 2:
      answer = "beta";
      break;
    case 3:
      answer = "gamma";
      break;
    case 4:
      answer = "delta";
      break;
  }


  // Only change code above this line
  return answer;
}

caseInSwitch(1);


 <h3>ADDING A DEFAULT OPTION IN SWITCH STATEMENTS</h3>
 
-when using "switch" statements, you may not be able to specify all possible values as "case" statement

-add a "default" statement that will be executed if no matching "case" statments are found

-can be thought of as the final "else" statment in an if/else chain

-"default" case statements are ALWAYS THE LAST CASE

switch (num) {
	case value1:
		statement1;
		break;
	case value2:
		statment2;
		break;
...
	default:
		defaultStatement;
		break;

}

==============

function switchOfStuff(val) {
  let answer = "";
  // Only change code below this line
switch (val) {
  case "a":
    answer = "apple";
    break;
  case "b":
    answer = "bird";
    break;
  case "c":
    answer = "cat";
    break;
  default:
    answer = "stuff";
    break;
}
  // Only change code above this line
  return answer;
}

console.log(switchOfStuff(1));
[console returns "stuff" because val=1 does not match other possible outcomes "a, b, or c"]

 <h3>MULTIPLE IDENTICAL OPTIONS IN SWITCH STATMENTS</h3>
 
 -if no "break" statement is present in a "switch" statement's "case", multiple "case" statements can be executed until a "break" is encountered
 
-multiple inputs with the same output in a "switch" statement:

let result = "";
switch (val) {
	case 1:
	case 2:
	case 3:
		result = "1, 2, or 3";
		break;
	case 4:
		result = "4 alone"
}
[results for case 1, 2, 3 all are grouped into the same outcome]
[results for case 4 has its own outcome]

=====================

function sequentialSizes(val) {
  let answer = "";
  // Only change code below this line
    switch (val) {
      case 1:
      case 2:
      case 3:
        answer = "Low";
        break;
      case 4:
      case 5: 
      case 6:
        answer = "Mid";
        break;
      case 7:
      case 8:
      case 9:
        answer = "High";
        break; 
    }


  // Only change code above this line
  return answer;
}

console.log(sequentialSizes(1));
[console log returns: "Low", fits into grouped "case 1-3" = "Low"]

<h3>REPLACE IF ELSE CHAINS WITH SWITCH STATMENTS</h3>

-may be easier to write "switch" statements than "if/else chains" if multiple options are needed to be chosen from

REPLACE THIS:

if (val === 1) {
	answer = "a";
} else if (val === 2) {
	answer = "b";
} else {
	answer = "c";
}

WITH THIS:

switch (val) {
	case 1:
		answer = "a";
		break;
	case 2:
		answer = "b";
		break;
	default:
		answer = "c";
}
[both above accomplish same thing]


========================
BEFORE:


  if (val === "bob") {
    answer = "Marley";
  } else if (val === 42) {
    answer = "The Answer";
  } else if (val === 1) {
    answer = "There is no #1";
  } else if (val === 99) {
    answer = "Missed me by this much!";
  } else if (val === 7) {
    answer = "Ate Nine";
  }


AFTER:

function chainToSwitch(val) {
  let answer = "";
  // Only change code below this line

  switch (val) {
    case "bob":
      answer = "Marley"
      break;
    case 42: 
      answer = "The Answer";
      break;
    case 1 :
      answer = "There is no #1";
      break;
    case 99:
      answer = "Missed me by this much!";
      break;
    case 7:
      answer = "Ate Nine";
      break;
  }
  // Only change code above this line
  return answer;
}

console.log(chainToSwitch(7));
[console log returns "Ate Nine" for case 7]

<h3>RETURNING BOOLEAN VALUES FROM FUNCTIONS</h3>

use an if/else statement for comparison leading to boolean true/false:

function isEqual(a, b) {
	if (a === b) {
		return true;
	} else {
		return false;
	}
}

because "===" returns true or false, above can be simplified to:

function isEqual(a, b) {
	return a === b;
}


================
BEFORE:

function isLess(a, b) {
  // Only change code below this line
  if (a < b) {
    return true;
  } else {
    return false;
  }
  // Only change code above this line
}

isLess(10, 15);



AFTER:

function isLess(a, b) {
  // Only change code below this line
    return a <= b;
  // Only change code above this line
}

console.log(isLess(10, 15);

<h3>RETURN EARLY PATTERN FOR FUNCTIONS</h3>

-when a return statement is reached, the execution of the current function stops
-control returns to the calling location
-code written after a "return" statement IS NOT EXECUTED

function myFun() {
	console.log("Hello");
	return "World";
	console.log("byebye")
}
myFun();
[above displays "Hello" in the console and the return string "World"]
[the string "byebye" will not display in the console because the function exits at the "return" statement]

=============

// Setup
function abTest(a, b) {
  // Only change code below this line
  if (a < 0 || b < 0) {
    return; 
  }
 


  // Only change code above this line

  return Math.round(Math.pow(Math.sqrt(a) + Math.sqrt(b), 2));
}

console.log(abTest(2,2));
[returns: 8 (?)]

<h3>COUNTING CARDS</h3>

let count = 0;

function cc(card) {
  // Only change code below this line
switch (card) {
  case 1:
  case 2:
  case 3:
  case 4:
  case 5:
  case 6:
    count++;
// count++ is the same as (count += 1) or (count = count + 1), increment count by 1
    break;
// case 7 through 9 are not needed because the count does not change for those three values (count would change by 0)
  case 10:
  case 'J':
  case 'Q':
  case 'K':
  case 'A':
    count--;
// count-- is the same as (count -= 1) or (count = count - 1), decrement count by 1
    break;
  }

  var holdbet; 
    if (count > 0) {
    holdbet = "Bet"
  } else {
    if (count < 0);
    holdbet = "Hold"
  }
  return count + " " + holdbet;
   
  // Only change code above this line
}

console.log(cc(2)); console.log(cc(3)); console.log(cc(7)); console.log(cc('K')); console.log(cc('A'))
// [console return logs in order: "1 Bet", "2 Bet", "2 Bet", "1 Bet", "0 Hold"]

ALTERNATIVE WAY TO WRITE ENDING STATEMENT STARTING WITH: var holdbet

var holdbet = "Hold"
if count > 0 {
	holdbet = "Bet";
	}
	return count + " " + holdbet;

// [only need to specify one situation: (count > 0) because any other possible values would be negative numbers/not within scope of > statement/]
// [declaring variable and setting its global value are two operations that DO NO require semicolon endings ;]
// ["if" statement needs to be followed by curly brace {}, statements within curly brace need to end with semicolons ;]


<h3>BUILD JAVASCRIPT OBJECTS</h3>

-a JavaScript "object" is a way of storing data using "properties"
-declare an "object", declare its "properties"
-const object = {};
-properties are contained within curly braces {}
-SEMICOLON AFTER CURLY BRACES {};
-each property has two parts:
("firstPart": "secondPart",), category and contained data piece
-first part of a "property" can be a number or a string, and ends with a colon :
-first part of "properties" do not require parentheses "" if they are strings, but will be automatically typecast as strings regardless
-second part of a "property" either ends with a comma , or has no ending punctuation if it is the last property in a list
-second part of a "property" can be a number 123, string "stringOne", array [1, 2, "three"]
-PROPERTY NAME and PROPERTY VALUE


const cat = {
	"name": "Whiskers",
	"legs": 4,
	"tails": 1,
	"enemies"; ["Water", "Dogs"]
};

============

const anotherObject = {
	make: "Ford";
	5: "five",
	"model": "focus"
};


================
const myDog = {
  // Only change code below this line
  "name": "Jeff",
  "legs": 4,
  "tails": 1,
  "friends": ["Me", "You"]

  // Only change code above this line

<h3>ACCESSING OBJECT PROPERTIES WITH DOT NOTATION</h3>

-two ways of accessing properties of a JavaScript "object": 
[declare a variable and set its value to the piece of data in the property you are looking for]

[need to know OBJECT NAME, and FIRST PART OF A PROPERTY, to find the SECOND PART OF A PROPERTY]

-dot notation: const prop1val = myObj.prop1; // [DOT AFTER OBJECT NAME, FOLLOWED BY DATA PROPERTY CATEGORY LOCATION]

-bracket notation: const prop1val = myObj[prop1]
//using square brackets [] to access object properties is similar to accessing data within an array

const myObj = {
	prop1: "val1",
	prop2: "val2"
};

const prop1val = myObj.prop1;
const prop2val = myObj.prop2;
// [prop1 val would have a value of the string: "val1"]

==========
// Setup
const testObj = {
  "hat": "ballcap",
  "shirt": "jersey",
  "shoes": "cleats"
};

// Only change code below this line
const hatValue = testObj.hat;      // Change this line
const shirtValue = testObj.shirt;    // Change this line
console.log(hatValue)
console.log(shirtValue)
//[console returns "ballcap" and "jersey"]
//[you CANNOT console.log at the same time you are declaring a variable, "console.log(const shirtVal = testObj.shirt);" DOES NOT WORK]

<h3>ACCESSING OBJECT PROPERTIES WITH BRACKET NOTATION</h3>

-see above section for more info
-if the property of an object CONTAINS A SPACE you MUST USE bracket notation
-bracket notation can still be used if a property DOES NOT contain a space

const myObj = {
	"Space Name": "Kirk",
	"More Space": "Spock",
	"NoSpace": "USS Enterprise"
};

myObj["Space Name"];
myObj['More Space'];
myObj["NoSpace"];

//[single parentheses ' ' and double parentheses " " are interchangable, property names]
// [property names containing spaces MUST BE IN PARENTHESES/QUOTES]
// myObj["Space Name"]; = "Kirk"


===================

// Setup
const testObj = {
  "an entree": "hamburger",
  "my side": "veggies",
  "the drink": "water"
};

// Only change code below this line
const entreeValue = testObj["an entree"];   // Change this line
const drinkValue = testObj["the drink"];    // Change this line
console.log(entreeValue)
console.log(drinkValue)
//[console returns: "hamburger" and "water"]

<h3>ACCESSING OBJECT PROPERTIES WITH VARIABLES</h3>

const objectOne = {
	"Name1": "Value1",
	"Name2": "Value2"
}

-use variable value with square brackets when iterating through an object's properties or when accessing a lookup table

const dogs = {
  Fido: "Mutt",
  Hunter: "Doberman",
  Snoopie: "Beagle"
};

const myDog = "Hunter";
const myBreed = dogs[myDog];
console.log(myBreed);

//[displays "Doberman" in console]

-we DO NOT use quotes around the variable name when using it access the property because we are using the VALUE of the variable, not the NAME [see above]

=======

// Setup
const testObj = {
  12: "Namath",
  16: "Montana",
  19: "Unitas"
};

// Only change code below this line
const playerNumber = 16;  // Change this line
const player = testObj[playerNumber];   // Change this line
console.log(playerNumber)

//[console log displays: 16]

-to access a piece of data with square brackets, you need to:
1. define variable equal to the NAME of the property you want to access
2. define a SECOND variable equal to the name of the OBJECT with the FIRST DEFINED VARIABLE IN SQUARE BRACKETS 
3. const varTwo = objectOne[varOne]


<h3>UPDATING/CHANGING OBJECT PROPERTIES</h3>

-object properties can be updated any time similar to variable values

-use dot or bracket notation to update property value

const ourDog = {
"name": "Camper",
"legs": 4,
"friends": ["everything!"]
};

ourDog.name = "Happy Camper";

ourDog["name"] = "Happy Camper";

//[both above options accomplish the same thing^^^]

===========

// Setup
const myDog = {
  "name": "Coder",
  "legs": 4,
  "tails": 1,
  "friends": ["freeCodeCamp Campers"]
};

// Only change code below this line
myDog.name = "Happy Coder";
console.log(myDog)
//[console log returns: // running tests
// tests completed
// console output
{ name: 'Happy Coder',
  legs: 4,
  tails: 1,
  friends: [ 'freeCodeCamp Campers' ] }]
  
<h3>ADD NEW PROPERTIES TO A JAVASCRIPT OBJECT</h3>

-use dot notation or bracket notation in a similar way to updating/changing object properties to add properties

const ourDog = {
  "name": "Camper",
  "legs": 4,
  "tails": 1,
  "friends": ["everything!"]
};

ourDog.bark = "bow-wow";

ourDog["bark"] = "bow-wow";

//[either of above two statements will add the property: "bark" with the value "bow-wow"]

===========

const myDog = {
  "name": "Happy Coder",
  "legs": 4,
  "tails": 1,
  "friends": ["freeCodeCamp Campers"]
};

myDog["bark"] = "woof";
console.log(myDog)
//[console log displays: { name: 'Happy Coder',
  legs: 4,
  tails: 1,
  friends: [ 'freeCodeCamp Campers' ],
  bark: 'woof' }]
  
  <h3>DELETE PROPERTIES FROM A JAVASCRIPT OBJECT</h3>
  
-use command: delete

delete ourDog.bark;


const ourDog = {
  "name": "Camper",
  "legs": 4,
  "tails": 1,
  "friends": ["everything!"],
  "bark": "bow-wow"
};

delete ourDog.bark;
//[deletes property: "bark"]

{
  "name": "Camper",
  "legs": 4,
  "tails": 1,
  "friends": ["everything!"]
}

=============

// Setup
const myDog = {
  "name": "Happy Coder",
  "legs": 4,
  "tails": 1,
  "friends": ["freeCodeCamp Campers"],
  "bark": "woof"
};

// Only change code below this line
delete myDog.tails
console.log(myDog)
//[console log displays: { name: 'Happy Coder',
  legs: 4,
  friends: [ 'freeCodeCamp Campers' ],
  bark: 'woof' }]
  
<h3>USING OBJECTS FOR LOOKUPS</h3>

-Objects = key/value storage like a dictionary

-with tabular data [data displayed in columns or tables] you can use Objects to look up values INSTEAD of using "switch" statments or "if/else" chains

-using Objects for data lookup is useful when YOUR INPUT DATA IS LIMITED TO A CERTAIN RANGE

example data for a written for an online publication:

===========

const article = {
  "title": "How to create objects in JavaScript",
  "link": "https://www.freecodecamp.org/news/a-complete-guide-to-creating-objects-in-javascript-b0e2450655e8/",
  "author": "Kaashan Hussain",
  "language": "JavaScript",
  "tags": "TECHNOLOGY",
  "createdAt": "NOVEMBER 28, 2018"
};

const articleAuthor = article["author"];
const articleLink = article["link"];

const value = "title";
const valueLookup = article[value];

==============
// [ASSIGN A VARIABLE to a PROPERTY within an OBJECT to assign the piece of DATA within the PROPERTY to be the value of the VARIABLE]
// [const articleAuthor = article["author"]; <---assigns the data contained within the property: (article) to the varable (articleAuthor) . articleAuthor 's value is now: "Kaashan Hussain"]


==============

// Setup
function phoneticLookup(val) {
  let result = "";

  // Only change code below this line
  var lookup = {
    "alpha": "Adams",
    "bravo": "Boston",
    "charlie": "Chicago",
    "delta": "Denver",
    "echo": "Easy",
    "foxtrot": "Frank"
  };
return lookup[val];

  // Only change code above this line
  return result;
}

phoneticLookup("charlie");

//[let result = "" creates an empty string, exists for the statement to have a place to "return" the results, like a container to store the results in]
//[when you run the code, the first return statement will give you results, but the second return statm-ent is needed to store the results]

<h3>TESTING OBJECTS FOR PROPERTIES</h3>

-can be useful to check if a specific PROPERTY exists within an OBJECT

-use [.hasOwnProperty(propname)]

-command returns true or false

const myObj = {
	top: "hat",
	bottom: "pants"
};

myObj.hasOwnProperty("top");
myObj.hasOwnProperty("middle");
[first returns: true]
[second returns: false]

====================

function checkObj(obj, checkProp) {
  // Only change code below this line
 checkObj.hasOwnProperty(checkProp);
 if (obj.hasOwnProperty(checkProp)) {
   return obj[checkProp];
 } else {
   return "Not Found";
 }
  // Only change code above this line
}

<h3>MANIPULATING COMPLEX OBJECTS</h3>

-JavaScript object can handle flexible data, is a flexable place to store data
-JavaScript objects can handle combinations of strings, numbers, booleans, arrays, functions, objects [hence the "complex" above^^]


const ourMusic = [
  {
    "artist": "Daft Punk",
    "title": "Homework",
    "release_year": 1997,
    "formats": [ 
      "CD", 
      "Cassette", 
      "LP"
    ],
    "gold": true
  }
];

-above is an array (notice square brackets []) that contains an object (object has curly braces {})
[{ }]
-"formats" is also an array that is within the larger array
-add more info for individual records by adding to the top level array

"artist": "Daft Punk",

-"artist" is a KEY, "Daft Punk" is a VALUE, the whole line is a PROPERTY

-comma after every object in an array unless it is the last

===================

const myMusic = [
  {
    "artist": "Billy Joel",
    "title": "Piano Man",
    "release_year": 1973,
    "formats": [
      "CD",
      "8T",
      "LP"
    ],
    "gold": true
  }, {
    "artist": "Frank Ocean",
    "title": "Channel Orange",
    "release_year": 2012,
    "formats": [
      "CD",
      "Digital"
    ] 
  }
];

-above: each album is its own JavaScript object within the top-most level array

<h3>ACCESSING NESTED OBJECTS</h3>

-accessing sub-properties of objects by chaining together the dot or bracket notation

const ourStorage = {
  "desk": {
    "drawer": "stapler"
  },
  "cabinet": {
    "top drawer": { 
      "folder1": "a file",
      "folder2": "secrets"
    },
    "bottom drawer": "soda"
  }
};

ourStorage.cabinet["top drawer"].folder2;
ourStorage.desk.drawer;

// ourStorage is the topmost level OBJECT, "desk" and "cabinet" are two NESTED OBJECTS; object stored within an object, "top drawer" is a NESTED OBJECT within another nested object
// "folder1", "folder2", "bottom drawer", and "drawer" are KEYs of PROPERTIES
// "staper", "secrets", "a file", and "soda" are VALUEs of PROPERTIES
// Object -> Property(Key + Value)
// Object -> Object -> Property(Key + Value)

//[access sub properties of objects] -> topObject.nestedObject[nestedObject1].property;

or

topObject.nestedObject.property;

=============
const myStorage = {
  "car": {
    "inside": {
      "glove box": "maps",
      "passenger seat": "crumbs"
     },
    "outside": {
      "trunk": "jack"
    }
  }
};

const gloveBoxContents = myStorage.car.inside["glove box"];

//[CANNOT be a period between word and square bracket]


<h3>ACCESSING NESTED ARRAYS</h3>

-see above "accessing nested objects", similar square bracket + dot notation to access arrays


const ourPets = [
  {
    animalType: "cat",
    names: [
      "Meowzer",
      "Fluffy",
      "Kit-Cat"
    ]
  },
  {
    animalType: "dog",
    names: [
      "Spot",
      "Bowser",
      "Frankie"
    ]
  }
];

ourPets[0].names[1];
ourPets[1].names[0];

// arrayName[valuePosition].nestedArray[nestedValuePosition];

//ourPets[0].names[1]; returns: "Fluffy"
//ourPets[1].names[0]; returns: "Spot"



======================

const myPlants = [
  {
    type: "flowers",
    list: [                <---------ARRAY #1
      "rose",
      "tulip",
      "dandelion"
    ]
  },
  {
    type: "trees",
    list: [             <-----------ARRAY #2
      "fir",
      "pine",
      "birch"
    ]
  }
];

const secondTree = myPlants[1].list[1];

//INSTRUCTIONS: assign secondTree to the second value of the second array of myPlants
//the arrays START FROM "WORD COLON SQUARE BRACKET"
//arrays in example start from "list: []", see above arrows^^
// lines: (type: "flowers") and (type: "trees") are NOT PART OF THE ARRAYS

<h3>RECORD COLLECTION (challenge, word problem question)</h3>

<h4>PROMPT:</h4>
Record Collection

You are given an object literal representing a part of your musical album collection. Each album has a unique id number as its key and several other properties. Not all albums have complete information.

You start with an updateRecords function that takes an object literal, records, containing the musical album collection, an id, a prop (like artist or tracks), and a value. Complete the function using the rules below to modify the object passed to the function.

Your function must always return the entire record collection object.
If prop isn't tracks and value isn't an empty string, update or set that album's prop to value.
If prop is tracks but the album doesn't have a tracks property, create an empty array and add value to it.
If prop is tracks and value isn't an empty string, add value to the end of the album's existing tracks array.
If value is an empty string, delete the given prop property from the album.
Note: A copy of the recordCollection object is used for the tests.

====================

// Setup
const recordCollection = {
  2548: {
    albumTitle: 'Slippery When Wet',
    artist: 'Bon Jovi',
    tracks: ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    albumTitle: '1999',
    artist: 'Prince',
    tracks: ['1999', 'Little Red Corvette']
  },
  1245: {
    artist: 'Robert Palmer',
    tracks: []
  },
  5439: {
    albumTitle: 'ABBA Gold'
  }
};

// Only change code below this line
function updateRecords(records, id, prop, value) {
  
  if (prop !== "tracks" && value !== "") {
    records[id][prop] = value; 
  } else if
  
}
return records;
}

=======================
<h4>LINE BY LINE: </h4>
// if prop is not tracks
	
	if (prop !== "tracks")

// if prop is tracks

	if (prop === "tracks")

// if value is not an empty string

	if (value !== "")

// if prop isn't tracks and value isn't an empty string

	if (prop !== "tracks" && value !== "")
	
// update or set that album's prop to value.

	{records[id][prop] = value;}
	
	
// if prop isn't tracks and value isn't an empty string, update or set that album's prop to value.

	if (prop !== "tracks" && value !== "") {
	records[id][prop] = value;
	}

//if album DOES NOT have a tracks property
//records[id] = album name

	if (records[id].hasOwnProperty("tracks") === false)

//if album DOES have a tracks property

	if (records[id].hasOwnProperty("tracks") === true)

//if prop is tracks, but the album doesn't have a tracks property, create an empty array and add value to it [IF PROP IS TRACKS, VALUE CANNOT BE AN EMPTY STRING, THAT IS IMPLIED, INCLUDE: value !== ""]

	if (prop === tracks && value !== "" && records[id].hasOwnProperty("tracks") === false) {
	records[id][prop] = [value];
	}

// if prop is tracks and value isn't an empty string, add value to the end of the album's existing tracks array 
//  .push command adds a value to the end 

	if (prop === "tracks" && value !== "") {
	records[id][prop].push(value);
	}

// if value is an empty string

	if (value === "")
	
// if value is an empty string, delete the given prop property from the album

	if (value === "") {
	delete records[id][prop];
	}
	
	
=========================
<h4>COMPLETE SOLUTION: </h4>


function updateRecords(records, id, prop, value) {
  if (prop !== "tracks" && value !== "") {
    records[id][prop] = value;
  } else if (prop === "tracks" && value !== "" && records[id].hasOwnProperty("tracks") === false) {
    records[id][prop] = [value];
  } else if (prop === "tracks" && value !== "") {
    records[id][prop].push(value);
  } else if (value === "") {
    delete records[id][prop];
  }
  return records;
}

// individual "if" statements are chained with "if" then "else if"

<h3>ITERATE WITH JAVASCRIPT "WHILE" LOOPS</h3>

-run the same code multiple times with a "loop" command, there are multiple types of "loop" commands

-"while" loop runs a set of code over and over as long as the result/specified condition is TRUE
-"while" loop STOPS when the condition is no longer true/is FALSE

const ourArray = [];
let i = 0;

while (i < 5) {
  ourArray.push(i);
  i++;
}

// above while loop executes 5 times, appends the numbers 0 through 4 to ourArray

====================
Prompt: Add the numbers 5 through 0 (inclusive) in descending order to myArray using a while loop



// Setup
const myArray = [];
let i = 5;

while (i >= 0) {
  myArray.push(i);
  i--;
}

// Only change code below this line

console.log(myArray)
// displays array: [5, 4, 3, 2, 1, 0]

// while loop runs "while a condition is true" and stops when it is no longer true
// above pushes "i" value to the end of the array if value of "i" is greater than or equal to 0
// "i--" decrements "i" by 1 with each execution of the while loop. "i" value decreases by 1 with each while loop
// specify starting value for variable "i" before manipulating it with while loop
// while loop stops at 0 because "i >= 0"
// "i" is just a variable chosen in the example, does not represent imaginary number

<h3>ITERATE WITH JAVASCRIPT "FOR" LOOPS</h3>

-"for" loop runs/executes a set of code for a SPECIFIC NUMBER OF TIMES
- "for" loop is most common

- "for" loops have 3 optional expressions: a, b, c
- each expression is seperated by a semicolon and space
- is like running three individual commands in succession/one after the other

===

	for (a; b; c)

-"a" is the INITIALIZATION STATEMENT
-"b" is the CONDITION
-"c" is the FINAL EXPRESSION

-"a": the INITIALIZATION STATEMENT is executed ONLY ONE TIME before the "for" loop starts
-initialization statement is used to define and setup the loop variable

-"b": the CONDITION STATEMENT is evaluated at the beginning of every loop and will continue as long as it evaluates to TRUE
-when CONDITION STATEMENT evaluates to FALSE at the start of an iteration, the loop will STOP executing
-if CONDITION STATEMENT evaluates as FALSE from the start, the loop will never execute

-"c": the FINAL EXPRESSION is executed at the end of each loop iteration, prior to the next condition check
-FINAL EXPRESSION is usually used to increment++ or decrement-- the loop counter

	const ourArray = [];
	
	for (let i = 0, i < 5; i++) {
		ourArray.push(i)
	}

// ourArray will have a value of [0, 1, 2, 3, 4]
// "ourArray.push(i)" pushes/adds the new value of "i" variable to the array from left to right with each iteration of the "for" loop
// "a" initialization statement sets starting value of "i" variable to 0: (i = 0), so first value in array is 0
// "b": condition statement says the "for" loop will only execute if the value of "i" is less than 5: if (i < 5), new iterations of the loop only execute if (i < 5) = true
// "c": final expression says to iterate "i" value with each loop iteration/add 1 to the "i" value each time the loop executes/runs, (i++) or (i + 1)
// "i" starts at 0, each iteration adds 1 to "i", new iterations of the "for" loop only happen if "i < 5", "ourArray.push(i)" writes each new "i" value to the array with each iteration

==========

// Setup
const myArray = [];

for (let i = 1; i < 6; i++) {
  myArray.push(i);
}

// Only change code below this line
console.log(myArray)

//myArray's value is [ 1, 2, 3, 4, 5 ]

<h3>ITERATE ODD/EVEN NUMBERS WITH A FOR LOOP</h3>

//"c" increment using (variable += 2)
//"b" (variable < number)

const ourArray = [];

for (let i = 0; i < 10; i += 2) {
  ourArray.push(i);
}

// ourArray = [0, 2, 4, 6, 8]
// if "i" starts at 0 and final expression adds 2 to "i" value for each iteration, the "for" loop will count by EVEN numbers

========

// Setup
const myArray = [];

for (let i = 1; i < 10; i += 2) {
  myArray.push(i);
}

console.log(myArray)
// Only change code below this line

// myArray = [ 1, 3, 5, 7, 9 ]
// if values start at 1, then incrementing by += 2 will count up by ODD numbers
// 0 counts as an even number(?)

<h3>COUNT BACKWARDS WITH A FOR LOOP</h3>

// "b" and "c" expressions are opposite from above^^^
// "c" iterate using (variable -= 2)
// "b" (variable > number)

const ourArray = [];

for (let i = 10; i > 0; i -= 2) {
  ourArray.push(i);
}

// ourArray = [10, 8, 6, 4, 2]
// counts down from 10 to zero, subtracting 2 with each iteration
// counting down EVEN numbers

=======

// Setup
const myArray = [];

for (let i = 9; i >0; i -= 2) {
  myArray.push(i);
}

console.log(myArray)
// Only change code below this line

//myArray = [ 9, 7, 5, 3, 1 ]
//counting down ODD numbers


<h3>ITERATE THROUGH AN ARRAY WITH A FOR LOOP</h3>

-"i" variable in position "a" of the "for" loop refers to the NUMBER OF ITERATIONS

-"array.length" refers to the position of the element within an array

ex. in "arrayOne = [10, 20 , 30]", 30 is in position: 2, has a length of 2 
-arrays counting starting from 0, zero-based indexing

	const arr = [10, 9, 8, 7, 6];

	for (let i = 0; i < arr.length; i++) {
 	  console.log(arr[i]);
}

//because of zero-based indexing, the last index of the array is "length - 1"
// i < arr.length stops "for" loop when i is equal to length
// the loop will stop when i = 5, will terminate when "i < arr.length = false"


==========
Declare and initialize a variable total to 0. Use a for loop to add the value of each element of the myArr array to total.



// Setup
const myArr = [2, 3, 4, 5, 6];

let total = 0

for (let i = 0; i < myArr.length; i++) {
  total += myArr[i];
}
console.log(myArr)
console.log(total)

// Only change code below this line

//myArr = [ 2, 3, 4, 5, 6 ]
//total =20

//1rst iteration: total = 0, i = 0, i + 2 = 2, new total value = 2
//2nd iteration: total = 2, i = 1, i + 3 = 5, new total value = 5
// final iteration is i === 4, because the length of the array/position of right most index/element of the array is 4
// when "i === 5" the loop stops because 5 > the loop length: 4

<h3>NESTING FOR LOOPS</h3>

-use above array logic with "for" loops to loop through an array and its sub-arrays in a multi-dimensional array

-"for" loop setup parameters (a; b; c) determine how the function will NAVIGATE through the given data
-statements in curly braces {} that come after "for" loop setup parameters (a; b; c) are where any MATH OR MANIPULATION happen to the data pieces


const arr = [
  [1, 2], [3, 4], [5, 6]
];

for (let i = 0; i < arr.length; i++) {
  for (let j = 0; j < arr[i].length; j++) {
    console.log(arr[i][j]);
  }
}

// variable "i" refers to main array
// variable "j" refers to the sub-array
// inner loop checks for length of array: i "arr[i].length" because arr[i] is an array
// outputs each sub-element in arr one at a time

===================
Modify function multiplyAll so that it returns the product of all the numbers in the sub-arrays of arr.



function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
for (let i = 0; i < arr.length; i++) {
  for (let j = 0; j < arr[i].length; j++)
  product = product * arr[i][j]
}
  // Only change code above this line
  return product;
}

multiplyAll([[1, 2], [3, 4], [5, 6, 7]]);

// starts with product = 1, multiplies product value by each number within multiplyAll and stores number as the new value for variable: "product", multiplying each new value for product by the next number starting from left to right
// 1 * 1= 1, 1 * 2 = 2, 2 * 3 = 6, etc.
// final result: product = 5040

<h3>ITERATE WITH JAVASCRIPT "DO...WHILE" LOOPS</h3>

- "do...while" loop will ALWAYS DO ONE PASS through the code inside of the loop, then will continue running the WHILE loop until the condition evaluates to false
- WHILE loop runs if true, terminates if false
- WHILE loop checks if condition is true/false before running and does not run if CONDITION IS FALSE FROM THE START
- DO...WHILE loop RUNS THE BRACKETED CODE ONCE BEFORE checking if condition is true/false

===============

const ourArray = [];
let i = 0;

while (i > 5) {
  ourArray.push(i);
  i++;
} 

// no "do" keyword is present
// i = 0, so i > 5, the expression evaluates to false (0 is less than 5), so the loop does not run
// result: i = 0, [] <----- the array stays empty, code does not run, so no values are pushed into array

==============
const ourArray = [];
let i = 0;

do {
  ourArray.push(i);
  i++;
} while (i < 5);

// above pushes "i" value into the empty array and increments/adds 1 to the "i" value before evaluating true/false for "i"
// result: i = 1, [0]

===============

// Setup
const myArray = [];
let i = 10;

// Only change code below this line
 do {
  myArray.push(i);
  i++;
} while (i < 5);

// result: i = 11, [10]

<h3>REPLACE LOOPS USING RECURSION</h3>

-recursion is a way of simplifying "while if" loops
-recursion loop has less steps than "while if"
-recursion loop and "while if" loops accomplish the same thing/code executes the same

=============
"the iterative approach"

"while if" logic:
1. you have a pile of objects to search through and a list/file of objects you've already checked
2. actively engage in searching WHILE the pile of objects isn't empty
3. reach into pile and grab an object

Ending A: if you reach in the pile and find a key, STOP, you're done
Ending B: if you reach in the pile and find a box, add the box to the file of objects you've checked and RETURN TO STEP 3

pseudocode:

function look_for_key(main_box) {
    let pile = main_box.make_a_pile_to_look_through();
    while (pile is not empty) {
        box = pile.grab_a_box();
        for (item in box) {
            if (item.is_a_box()) {
                pile.append(item)
            } else if (item.is_a_key()) {
                console.log("found the key!")
            }
        }
    }}

==============
"recursive approach"

recursion loop logic:
1. check every object in the pile

Ending A: if you find a key in the pile, STOP you're done
Ending B: if you find a box in the pile, RETURN TO STEP 1


pseudocode:

function look_for_key(box) {
  for (item in box) {
    if (item.is_a_box()) {
      look_for_key(item);
    } else if (item.is_a_key()) {
      console.log("found the key!")
    } 
  }
}

=================
// NO PERFORMANCE BENEFIT TO USING RECURSION LOOP INSTEAD OF "WHILE IF" LOOP, iterative approach/"while if" can be faster than recursion and vice versa
// Recursion loop might be easier to read because less steps in code
// matter of personal preference, both do accomplish same goal
// a lot of algorithms use recursion


-beware of INFINITE LOOPS when using recursion loops
-infinite loops are when a function keeps calling itself/running over and over without an ending/solution

// WARNING: This function contains an infinite loop!
function countdown(i) {  console.log(i)  countdown(i - 1)}

countdown(5);    // This is the initial call to the function.

//above function will keep counting down forever
// above steps: print "i" -> call countdown with "i" -> print "i" -> call countdoun with "i" -> etc.
// code/script needs to be manually killed, "Ctrl-C"? or turn off js “?turn_off_js=true” at the end of url depending on program

-recursive function/recursion loop ALWAYS HAS TO SAY WHEN TO STOP REPEATING ITSELF
-specify a stopping condition

-TWO PARTS to a recursive function:
1. recursive case
2. base case

-BASE CASE is when the function stops calling itself


function countdown(i) {
    console.log(i)  if (i <= 1) {  // base case
        return;
    } else {     // recursive case
        countdown(i - 1);
    }
}

countdown(5);    // This is the initial call to the function.

// above function will stop looping back/calling itself "if (i <= 1)"
// above function starts from 5 "countdown(5)" ["i" value is set to 5], counts down -1 per loop, stops counting when i value reaches 1

recursion loop with base case logic:
1. print "i"/countdown
2. countdown i - 1, call countdown unless i <= 1
3. if i <= 1 STOP


CALL STACK is a queue of tasks to complete/function steps to run
-like a stack of books, add one book to the stack at a time
-when you're ready to take a book off the stack, you take off the topmost book
-when a program calls a function, that function goes to the top of the call stack

factorial function:
factorial(5) = 5!
5! = 5 * 4 * 3 * 2 * 1

fact(x)

function fact(x) {
    if (x == 1) {
        return 1;
    } else {
        return x * fact(x-1);
    }
}

// each call to function "fact" has its own "x"
// one instance of function "fact" cannot access another function's "x"

============
Write a recursive function, sum(arr, n), that returns the sum of the first n elements of an array arr.


function sum(arr, n) {
  // Only change code below this line
if (n <= 0) {
  return 0; //<--- I wrote 
"return n;" and still passed question
} else
  return sum(arr, n - 1) + arr[n - 1];
  // Only change code above this line
}

// "if" statement checks to see if fucntion: "sum" is evaluating the base case
// the sum of elements from 0 to 0 is inclusive
// otherwise it recurses by evaluating a simpler function call: "sum(arr, n - 1)"
// when that returns, it adds a single array element: "arr[n - 1]" to it and returns that sum: "sum(arr, n - 1) + arr[n - 1];"

<h3>PROFILE LOOKUP (word problem, challenge question)</h3>

lookUpProfile


function lookUpProfile(name, prop) {
  for (let x = 0; x < contacts.length; x++) {
    if (contacts[x].firstName === name) {
      if (contacts[x].hasOwnProperty(prop)) {
        return contacts[x][prop];
      } else {
        return "No such property";
      }
    }
  }
  return "No such contact";
}

// variable "x" is the position within the array, 0 is starting point from left to right
// if value of x is less than the contacts total length, you add 1 to x's value 
// total length of contacts [contacts.length] would be the position of the last piece of info in the array/the right most data piece
// when running function: lookUpProfile(name, prop); you insert first name for "name" and the desired property for prop
// example: lookUpProfile(Sherlock, number) yields: 0487345643
// if you input a value for "name" or "prop" that is not present within the array/database, the function will yield: "No such property"
// lookUpProfile(Sherlock, dislikes) yields: "No such property" because there is no dislikes property for the Sherlock contact
// lookUpProfile(Jimmy, number) yields: "No such property" because there is no contact info within the array for "Jimmy"
// "if (contacts[x].firstName === name)" <--- says if the value for "firstName" matches the input value for "name" when the function is run, move to next if statement/next step
// "if (contacts[x].hasOwnProperty(prop))" <--- if the contact info for "x" contact has the requested prop value when the function is run, move to next step/return contacts [x][prop]
// if both "if" statements fail, return "No such property"
// second [return "No such property"] is there if the original "for" statement fails as a contingency plan, cannot get to the "else" statement if the original "for" statement fails

<h3>GENERATE RANDOM FRACTIONS WITH JAVASCRIPT</h3>

-random numbers are useful for creating random behavior

-JavaScript has function "Math.random()"
-"Math.random()" generates a random decimal number between 0 (inclusive) and 1 (exclusive) 
- minimum number generated = 0
- maximum number generated = .99
- CANNOT generate 1, because function excludes [1 (exclusive)]

-all function calls will be resolved BEFORE the "return" executes, like when you assign a number to a variable
-"Storing values with the Assignment Operator" = assigning a value to a variable [let a = 1;]
[var myVar;
myVar = 1;]

==========
function randomFraction() {
return Math.random();
}
console.log(randomFraction())

//console log displays: 0.1606203975376459

<h3>GENERATE RANDOM WHOLE NUMBERS WITH JAVASCRIPT</h3>

-since Math.random() can only give you a decimal between 0 and 0.99, MULTIPLY THE RESULT by the maximum whole number you want to generate

Math.random() * 20; 
// Math.random * 20 multiplies the product of the random decimal by 20
// above^^ will yield a random whole number between 0 and 19.99, but cannot yield 20 because original random number generator cannot yield 1

-"Math.floor" rounds  numbers down to the nearest whole number

Math.floor(Math.random() * 20);
// above function generates a random number between 0 (inclusive) and 20 (exclusive) [so 0 through 19.99] and then rounds that value down to the nearest whole number
// generates whole numbers from 0 (inclusive) to 19 (inclusive)

============

Use this technique to generate and return a random whole number between 0 and 9.


function randomWholeNum() {

  // Only change code below this line

  return Math.floor(Math.random() * 10);
}
console.log(randomWholeNum())

// console log displays: 2
// remember random number generator does NOT include maximum value so if you want numbers 0 through 9, you multiply the random number by 10 and round with Math.floor

<h3>GENERATE RANDOM WHOLE NUMBERS WITHIN A RANGE</h3>

-generate random numbers between the specified minimum and maximum values

Math.floor(Math.random() * (max - min + 1)) + min

// generates whole number between max and min values
// add the min value after rounding number down because Math.random can generate 0 and Math.floor will round numbers between 0 and 0.99 down to 0
// includes min and max values [if min = 1 and max = 10, both 1 and 10 can be generated]

Math.floor(Math.random() * (10 - 1 + 1)) + 1

// if random number is 0.2:
PEMDAS
1 + 1 = 2
10 - 2 = 8
0.2 * 8 = 1.6
Math.floor(1.6) = 1
1 + 1 = 2


==============
Create a function called randomRange that takes a range myMin and myMax and returns a random whole number that's greater than or equal to myMin, and is less than or equal to myMax, inclusive.



function randomRange(myMin, myMax) {
  // Only change code below this line
 return Math.floor(Math.random() * (myMax - myMin + 1)) + myMin


  // Only change code above this line
}


<h3>USE THE parseInt FUNCTION</h3>

-"parstInt" function parses a string and returns an integer [the string must include a number]

const a = parseInt("007");

-above function converts string "007" into the integer: 7
-if the first character in the string can't be converted into a number, the parseInt function returns "NaN" [Not A Number]

===============
Use parseInt() in the convertToInteger function so it converts the input string str into an integer, and returns it.

function convertToInteger(str) {
return parseInt(str);
}

convertToInteger("56");

// returns : 56


<h3>USE THE parseInt FUNCTION WITH A RADIX</h3>

-parseInt() takes a second argument for the radix
-radix specifies the base of the number in the string
-radix can be an integer between 2 and 36

parse(string, radix);


const a = parseInt("11", 2);

// the radix variable: 2  say that the number value in the string: "11" is in the BINARY SYSTEM or base 2
// converts string "11" to the integer: 3

=========
Use parseInt() in the convertToInteger function so it converts a binary number to an integer and returns it.

function convertToInteger(str) {
return parseInt(str, 2);
}

convertToInteger("10011");

<h3>USE THE CONDITIONAL (TERNARY) OPERATOR</h3>

-conditional operator = ternary operator [same meaning]
-conditional operator can be used as a one line "if-else" expression

a ? b : c
 
- "a" is the condition
- "b" is the code to run when the condition returns TRUE
- "c" is the code to run when the condition returns FALSE

TWO WAYS OF WRITING SAME STATEMENT:

====
1. if/else version:

====

	function findGreater(a, b){
	if(a > b) {
		return "a is greater";
	}
	else {
		return "b is greater or equal";
	 }
	}
	
==============

2. conditional operator version:

===

	function findGreater(a, b) {
		return a > b ? "a is greater" : "b is greater or equal";
	}
	
	
=====================

Use the conditional operator in the checkEqual function to check if two numbers are equal or not. The function should return either the string Equal or the string Not Equal.


function checkEqual(a, b) {
  return a === b ? "Equal" : "Not Equal";
}

checkEqual(1, 2);

// === three equal signs is strictly equal, checks if two compared values are exactly the same, 10 === 10 [yes], "10" === 10 [no]
// == two equal signs is a comparison operator, compares two values and converts different type values to the same type [ex. if comparing a string to a number, == will change both to numbers if the string has a numerical value, will show NaN if string does not include numbers]
// "10" == 11 converts "10" to 10 before comparing
// = one equal sign sets a value to a variable, a = 10 [okay], a = a [error], 10 = 10 [error]

<h3>USE MULTIPLE CONDITIONAL (TERNARY) OPERATORS</h3>

-can chain multiple conditional/ternary operators

TWO WAYS OF WRITING SAME STATEMENT:

1. with if, else if, else

===============

function findGreaterOrEqual(a, b) {
	if (a === b) {
		return "a and b are equal";
	}
	else if (a > b) {
		return "a is greater";
	}
	else {
		return "b is greater";
	}
}

================

2. chain of conditional/ternary operators

=========

function findGreaterOrEqual(a, b) {
	return (a === b) ? "a and b are equal"
	: (a > b) ? "a is greater"
	: "b is greater";
}

// best practice for readibility to seperate multiple conditional/ternary operations to their own line [each line starts with a colon : and only the last statement ends with a semicolon ;]

=========================

In the checkSign function, use multiple conditional operators - following the recommended format used in findGreaterOrEqual - to check if a number is positive, negative or zero. The function should return positive, negative or zero.


function checkSign(num) {
  return (num > 0) ? "positive"
  : (num < 0) ? "negative"
  : "zero"
}

checkSign(10);

<h3>USE RECURSION TO CREATE A COUNTDOWN</h3>

".push" adds an element to the end (rightmost position) of an array
[1, 2, 3] <---- next addition enters from right
[1, 2, 3, 4]

".unshift" adds an element to the start (left most position) of an array
next enters from left ---> [1, 2, 3]
[4, 1, 2, 3]

<h4>LOGIC: COUNTING UP VS COUNTING DOWN</h4>

using a function to COUNT UP:
START FROM "1" and PUSH NEW NUMBERS TO RIGHT SIDE
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]

using a function to COUNT DOWN
START FROM "1" and UNSHIFT NEW NUMBERS TO THE LEFT SIDE
[1]
[2, 1]
[3, 2, 1]
[4, 3, 2, 1]

=========================

1. COUNT UP FUNCTION

==========

function countup(n) {
	if (n < 1) {
		return [];  //<--- returns empty array  
	} else {
		const countArray = countup(n - 1);
		countArray.push(n);
		return countArray;
	}
}
console.log(countup(5)); //<-- sets end point

// the function does not RETURN ANY VALUE until the count is complete
// return only happens when the array is established to store the values
// because the array is ONLY ESTABLISHED WHEN n < 1, NO NUMBERS ARE ADDED TO THE ARRAY UNTIL THE ARRAY ITSELF IS ESTABLISHED (i.e. n = 0)
// because the function uses .push, it adds the values in from left to right STARTING FROM THE LAST COMPLETED FUNCTION
[countup(1) was the last completed loop of the function so it is the first value to be added to after the array itself is established]

ORDER OF FUNCTION RECURSION LOOP COMPLETION:

countup(5) {
    const countArray = countup(4) {
        const countArray = countup(3) {
            const countArray = countup(2) {
                const countArray = countup(1) {
                    const countArray = countup(0) {
                        return [];
                    countArray.push(1);
                    return countArray; //[1]
                countArray.push(2);
                return countArray; //[1, 2] <---adds to right side
            countArray.push(3);
            return countArray; // [1, 2, 3]
        countArray.push(4);
        return countArray; // [1, 2, 3, 4]
    countArray.push(5);
    return countArray; // [1, 2, 3, 4, 5]
}

===============
We have defined a function called countdown with one parameter (n). The function should use recursion to return an array containing the integers n through 1 based on the n parameter. If the function is called with a number less than 1, the function should return an empty array. For example, calling this function with n = 5 should return the array [5, 4, 3, 2, 1]. Your function must use recursion by calling itself and must not use loops of any kind.
[THEY WANT YOU TO DO THE OPPOSITE OF THE ABOVE FUNCTION]

// Only change code below this line
function countdown(n){
  if (n < 1) {
    return [];
  } else {
    const countArray = countdown(n - 1);
    countArray.unshift(n);
    return countArray;
  }
}
console.log(countdown(5))
// Only change code above this line


// SAME FUNCTION AS ABOVE BUT ADDS VALUES TO START/LEFT INSTEAD OF END/RIGHT:

LOGIC ORDER:

countup(5) {
    const countArray = countup(4) {
        const countArray = countup(3) {
            const countArray = countup(2) {
                const countArray = countup(1) { <--adds last completed value first
                    const countArray = countup(0) {
                        return [];
                    countArray.unshift(1);
                    return countArray; //[1]
                countArray.push(2);
                return countArray; //[2, 1] //<-- adds to left side
            countArray.push(3);
            return countArray; // [3, 2, 1]
        countArray.push(4);
        return countArray; // [4, 3, 2, 1]
    countArray.push(5);
    return countArray; // [5, 4, 3, 2, 1]
}


<h3>USE RECURSION TO CREATE A RANGE OF NUMBERS (challenge question)</h3>

We have defined a function named rangeOfNumbers with two parameters. The function should return an array of integers which begins with a number represented by the startNum parameter and ends with a number represented by the endNum parameter. The starting number will always be less than or equal to the ending number. Your function must use recursion by calling itself and not use loops of any kind. It should also work for cases where both startNum and endNum are the same.




function rangeOfNumbers(startNum, endNum) {
  if (startNum > endNum ){
  return [];
  } else {
    const array = rangeOfNumbers(startNum, endNum - 1);
      array.push(endNum); 
      return array;
    }
  }
console.log(rangeOfNumbers(1, 5))

// make sure values being pushed to array, not function 
// if the function has two inputs, then every subsequent mention of the function needs to have two inputs [rangeOfNumbers(a, b)]
// startNum stays the same, countdown happens with the endNum of the range
// all math using the function must complete itself before the array is returned
// array must be established withing the "if" condition before number values from the function can be written to the array/array can be returned


