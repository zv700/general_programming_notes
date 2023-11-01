<h3>CHECK CONSOLE LOG</h3>
-displays function result in console/shows returned values in console
-can run a function and check the console log at the same time by executing function within parentheses parameter of console.log()

	console.log(yourFunction(n))
	
<h3>NOTES WITHIN CODE</h3>

-"//" seperates code from notes, anything to the right of // on the same line is not included in executed code
-anything to the LEFT of // is part of code
-// only applies to the line it is written on and must be rewritten for each line you want to write notes
	
	
	const yes; // text to the right of slashes are notes
	
	// this line is a note
	var peanut
	// this line is also a note
	
<h3>DECLARE VARIABLES/ASSIGN VALUES TO VARIABLES</h3>

-IDEALLY use "const" or "let", they cannot/are more difficult to be accidentally overwritten later in code
-"let" is BLOCK SCOPED, it can only be changed within the specific block of code it was declared in, can be overwritten later LOCALLY within functions
-"const" is immutable, cannot be changed later, and is block scoped
-AVOID USING "var", var is the normal way of declaring variables, it can be accidentally changed later easily

	const declaredVariable;
	
	let declaredVariableTwo;
	
	var declaredVariableThree;
	
<h3>GLOBAL SCOPE VS LOCAL SCOPE</h3>

-variables set with local scope OVERWRITE/TAKE PRECIDENCE OVER variables set with global scope
-global scope is the baseline
-local scope is modifications made on top of the base foundation
	
<h3>MANIPULTING ARRAYS:</h3>
.push() insert element to rightmost/last index of array, specify what you want to insert/add within parentheses

.pop() remove element from rightmost/last index of array

.shift() remove element from leftmost/first index of array, index 0 

.unshift() insert element to leftmost/first index of array, index: 0

<h3>DECLARE A FUNCTION</h3>

	function myFunction(x, y) {
		if (x == y) {
			return "yes, true"
		}
		return "no, false"
	}

<h3>CHECK DATA TYPE OF A VARIABLE</h3>
- use "typeof" operator in JavaScript to determine the data type of a variable

		typeof 3
[console returns the string: "number"]

	typeof '3'
[console returns the string: "string"]

<h3>BOOLEANS</h3>

-Booleans can only be evaluated to be TRUE[1] or FALSE[0]
-Booleans are "if" statements in functions

	1 == true // true
	0 == false // true
	1 != true  // false
	0 != false // false

<h3>BOOLEAN OPERATORS</h3>
<h4>EQUALITY OPERATOR [converts data types]</h4>
"=="
	
	3 == 3 // true
	3 == "3" // true

<h4>STRICT EQUALITY OPERATOR [does not convert data types]</h4>
"==="

	3 === 3 // true
	3 === "3" // false
	
<h4>INEQUALITY OPERATOR [converts data types]</h4>
"!="
-checks if two values are NOT EQUAL

	1 !=  2    // true
	1 != "1"   // false
	1 != '1'   // false
	1 != true  // false
	0 != false // false
	

<h4>STRICT INEQUALITY OPERATOR [does NOT convert data types]</h4>
"!=="
-only false if both values have the same data type

	3 !== 3 // false
	3 !== '3' // true
	4 !== 3 // true
	
<h4>GREATER THAN OPERATOR [does convert between data types]</h4>

-same as in math
-if left value is greater: TRUE
-if left value is less: FALSE
-compares number values that are either NUMBERS or STRINGS

	1 > 3 // false
	'5' > 2 // true
	9 > '1' // true
	
<h4>GREATER THAN OR EQUAL TO [does convert between data types]</h4>

>=

if functionOne(num >= 5) {

}


<h4>LESS THAN [does convert between data types]</h4>

<

if functionOne(num < 5) {

}

<h4>LESS THAN OR EQUAL TO [does convert between data types]</h4>

<=

if functionOne(num <= 5) {

}


<h4>LOGICAL AND </h4>

&&
-statements left and right of && must both be true for the end result to be true

if (num > 1 && num <=5)


<h4>LOGICAL OR</h4>
