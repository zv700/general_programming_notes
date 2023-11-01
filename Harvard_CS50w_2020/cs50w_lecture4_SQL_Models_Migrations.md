## SQL (pronounced: "sequel")(Structured Query Language)
- NOTE: SQLite is installed by default on MAC computers, but not on Windows computers. need to install/add to PATH
- SQL = database language used to interact with databases

- Django allows for an extraction layer above SQL
- normally have to write SQL queries
- Django allows to interact with Python classes and objects instead of queries
- **Models = Python classes and objects**
- **Migrations = technique that allows you to update database in response to changes made in underlying Models**

## Data
- data stored in different types of databases in general using computers
- **Relational database = storing data within tables**
- tables have rows and columns
- CRUD: relational databases Create data, Read data, Update data, Delete data

- course example database will revolve around keeping track of flights for an airline [table's three columns: flight's origin(starting location), destination(where the plane is planning to go to), duration(how long the flight will take in minutes)], keeping track of which passenger is on which flight

### Database management systems

- SQL = databse language designed to interact with relational databases [tables, organize data into rows and columns]
- Other database management systems exist that are based on SQL system [MySQL, PostgreSQL, SQLite, etc.] with their own features/appropriate usage cases
- MySQL and PostgreSQL are larger database management systems, often run on servers located elsewhere, used by big companies [have your website running on one server and have your database running on a seperate server as an entirely seperate process so each behaves independantly, can debug independantly from each other. if one goes down, the other will not at the same time]
- SQLite = lighter weight implementation of SQL, instead of having an entire server, SQLite stores all data as a single file

- each piece of data stored in SQL has a Type [category of data], similar to how data in Python has Types [integers, strings, lists, tuples, etc.]
- each database management system has its own Types of data

## SQLite types
**- SQLite types: text, numeric, integer, real, blob**
- text = plain text, like a city name "Boston"
- numberic = generalized data that involves numbers but is not integer or real number: some kind of number or something similar to a number [boolean value: True or False, Yes or No] [a date: January 1rst, 1/1/2023]
- integer = positive and negative whole numbers
- real = real numbers, doesn't have to be just integers, can be decimals or can have whole numbers with numbers after decimal point "2.8"
- blob = "Binary Large OBject", other types of binary data: zeros and ones [010010101], useful for storing images or audio files in SQL database

## MySQL Types
- CHAR(size) = storing data based on the number of characters withing the data, size of the data [example: zip codes in US have 5 characters each, can allocate 5 character length to be able to store just zip codes, You know the maximum character length of all of the data pieces to be stored, All data pieces have the exact same character length]
- VARCHAR(size) = if data pieces are not going to be exactly a specific number of characters, Up to a certain number of characters, specify a maximum number of characters, data pieces can have less characters than the maximum
- SMALLINT
- INT
- BIGINT
[SMALLINT, INT, BIGINT = allocate database storage size based on anticipated integer sizes, BIGINT bigger integers may take up more space than SMALLINT smaller integers]
- FLOAT
- DOUBLE
[FLOAT and DOUBLE = store real numbers (floating point numbers, decimals, whole numbers with decimals), DOUBLE allows to express a number with more precision than a FLOAT]
- ... [etc. more types]

## Create a SQL table in SQLite

syntax for creating a table that handles flights:

	CREATE TABLE flights (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	origin TEXT NOT NULL,
	destination TEXT NOT NULL,
	duration INTEGER NOT NULL
	);
	
- CREATE TABLE = keyword, create a new table within database
- CREATE TABLE tableName ()
- in parentheses following table's name: comma seperated **list of all of the columns that should be present in the table**
- CREATE TABLE query decides the structure of the table: What are the columns (names)? What are the columns' types?
- columns in above table: id, origin, destination, duration
- "id" column does not show up in final table, "id" is for having a unique name to reference a specific element within the table [example: multiple flights who's origin is New York, give each flight from New York its own identifying id (like a number, Flight 100 from New York, Flight 501 from New York)]
- "id" allows you to always be able to reference a specific table entry with its own unique identifier even if multiple table entries have similar names

### Column segments/structure:
- columns in list have THREE segments seperated by a space: 1.columnName 2.columnType
3.columnConstraints
- can have more than one column constraints per column
- comma marks the end of each column's info
- 
### Column TYPE
- column TYPE follows column name [example: in origin TEXT NOT NULL, the type is TEXT]
- determines the type of data stored in that particular column

### Column CONSTRAINTS
- can have more than one constraint per column
- PRIMARY KEY = primary way to identify each row of data/in this case each flight
- in the example flights table: flights will be identified by their ID number and not their origin, destination, or duration [Flight 1, Flight 20]
- NOT NULL = constraint that prevents a column from being empty [each flight must have an origin, a destination, and a duration because each of these columns contains NOT NULL]
- AUTOINCREMENT = SQL que that tells SQL to automatically add a new id/update ids when you add a new row in the table [when you add a new flight SQL automatically makes an id for the flight. You have to give the flight an origin, destination, duration]

### Other constraints, ensuring data validity

- CHECK = check to see if each piece of data is valid based on set parameters, obeys a certain condition [a number falls within a certain range, rating movies out of 1-5 stars and each row of data must be a number between 1 through 5 inclusive]
- DEFAULT = adds a default value to a particular column
- NOT NULL = column cannot be blank, must have a value for each new row
- PRIMARY KEY = column's value is used to identify each corresponding row of data
- UNIQUE = every value in the column must be unique, no values appear twice

## Add data into SQL table 

INSERT INTO query syntax:

	INSERT INTO flights 
		(origin, destination, duration)
		VALUES ('New York', 'London', 415);
	
- second line lists column names
- third line VALUES lists data pieces that go into corresponding column order listed in second line ["New York" => origin, "London" => destination, 415 => duration]
-  Note: "id" colomn from example is left out, SQL is set to AUTOINCREMENT, SQL will populate "id" column automatically

## Retrieve data from SQL table

### command to select/display all data from an SQL table

SELECT query syntax:

	SELECT * FROM flights;
	
- "*" star/asterisk is a wildcard value, it selects ALL data from the selected table
- "SELECT * FROM flights;" will display the entire table, all of the data/columns/rows from the selected table

### command to select specific columns of data from SQL table (all rows of info within a column) 

	SELECT origin, destination FROM flights;
	
- query will only select/display all of the rows of data from columns: origin and destination

### command to select a specific row of data within an SQL table

	Select * FROM flights WHERE id = 3;
	
- asterisk/star "*" means "all", as in all data points
- specify id number of data row, each row will have a unique id
- displays all columns of data within a specific row of an SQL table

### filter select query by other columns

	SELECT * FROM flights WHERE origin = "New York";
	
- query will retrieve all data from any row with an origin value of "New York"
- "an airport in New York might want to have a way of filtering all flights leaving from NY so they can have a display screen listing all of the departures from that airport"

## Create a new SQLite database file

- just make a new blank .txt document in your desired folder and change the extension to .db

USING sqlite3 FROM COMMANDLINE:

	sqlite3 databasename.db
	
[If gives you error and does not make the .db file, exit and restart terminal]

	
## Run .db file

	sqlite3 databaseName.db
	
- requires SQLite to be installed to PATH on Windows

## CREATE TABLE within .db file

- create the table, then create each individual column with column name, type, constraints LINE BY LINE [each column is its own line in terminal]
- line by line code is OPTIONAL, can input all table/column parameters in one line of code if you want
- comma marks the end of a line/the end of parameters for each table column
- press ENTER/Return after each comma ,

first run in terminal:

	CREATE TABLE tableName (

- press ENTER/Return to move to next line [press enter after the first parentheses, close the parentheses after making all desired columns]

	id INTEGER PRIMARY KEY AUTOINCREMENT,

- press ENTER

	origin TEXT NOT NULL,

- press ENTER
	
	destination TEXT NOT NULL,

- press ENTER

	duration INTEGER NOT NULL

- press ENTER [last column does not need a comma]

	);

- [After last column: close parentheses + semicolon] press ENTER

### list all tables within .db file
	
	.tables

### USE SINGLE QUOTES WHEN INSERTING STRING VALUES INTO SQL TABLE

- double quotes "" will give an error

example: 

	VALUE ('New York', 'London', 415)

## Make SQLite display table data in terminal lined up/more organized

run:
	
	.mode columns
	.headers yes
	
- then check your table
	
	SELECT * FROM flights
	
## Other possible SQLite queries

Use boolean expressions/arithmatic expressions to compare:

	SELECT * FROM flights WHERE duration > 500;
	
use multiple simultaneous arithamtic/boolean comparisons using AND [similar to Python]

	SELECT * FROM flights WHERE duration > 500 AND destination = 'Paris';
	
check for results from possible values [will return values that contain AT LEAST ONE of the parameters]
Below: searching for flights originating from New York OR Lima

	SELECT * FROM flights WHERE origin IN ('New York', 'Lima');
	
	
## Exit out of SQLite query

ctrl + c

- for when pressing enter adds another line ...> indefinitely
- sqlite queries end with semicolon ;
- entering a statement ending with a semicolon will finish ...> format, error message or otherwise
-  
- "dot" commands do not require a semicolon (example: .headers yes)

## searching for unknown information

	SELECT * FROM flights WHERE origin LIKE "%a%";
	
- % percent signs stand for a "wild card" => "zero or more characters no matter what those characters are"
- above command will search for any results containing the letter "a" in the origin column
- above will search for any character(s) placed between the two percent signs within the specified column
- in this case looking at the value of a particular column [origin column]

	SELECT * FROM flights WHERE destination LIKE '%is%';
	
- above will retrieve any column where the destination value contains the characters "is" => any column with Paris as the destination
- NOTE: use single quotes in queries on PC, can use double quotes ONLY on Mac

## Additional SQL SELECT query functions

- AVERAGE
- COUNT
- MAX
- MIN
- SUM
- etc.

## UPDATE/change data within an SQL table

	UPDATE flights
		SET duration = 430
		WHERE origin = 'New York'
		AND destination = 'London';
		
- above example query is written on multiple lines, but will also work if written all in one line
-  sequel does not care about line breaks[new line from Enter/Return], it only looks for a semicolon ; at the end of a command/query
-  UPDATE[change] tableName SET columnName = newValue WHERE columnName = specificValue AND columnName = specificValue

	UPDATE flights SET duration = 750 WHERE id = 3;
	
## DELETE data within an SQL table

- can delete rows or columns, or specify specific characteristics

	DELETE FROM flights WHERE desitination = 'Tokyo';
	
	
	DELETE FROM flights WHERE id = 5;
	
- if you delete a row from SQL table and insert a new row, the new row will have its own unique id
- example: if I delete row 7 and add a new row, new row's id number will be 8

## Other SQL query Clauses

- LIMIT [if you don't want data all of the rows to be retrieved when using SELECT * ]
- ORDER BY [let's you decide how results are ordered within SELECT results, ORDER BY columnName, ORDER BY destination]
- GROUP BY [group rows together, GROUP BY origin]
- HAVING [constraint for GROUP BY stating a minimum number search results, GROUP BY origin HAVING 3 => "at least 3 results"]
- etc.

	SELECT * FROM flights LIMIT 5
	
- above says you only want the first 5 results from the search query "limit the results to 5 rows/units"
- these clauses are mostly useful if you are writing SQL yourself
- if using Django, it will handle most SQL processes

## Foreign Keys

- Foreign key = using an id number from one table to identify a value within another table
- **Example:** table one flights( **origin** = 1), table two airtportcities(id = 1, city = **'New York'**) ----> origin = 'New York'

- instead of adding too many columns to one table [instead of having one table with 7 columns, you can have related tables: one main table with 4 columns that references a secondary table with 3 columns --> second layer to data: table one(origin city + destination city), table two(specific airport name within origin city + airport within destination city )]
- normalize data, seperating things out into more than one table that reference each other

going from one table to two connected tables:
- first table = flights "flights are one type of object"
- second table = airports "airports are another type of object"
- make two simple connected tables instead of one complex table
- original "flights" example table stores data as text within origin and destination columns
- rename "origin" column to "origin_id"
- store city names within a second table, associate airport city names with an id number
- in first table under origin_id, list airport city id numbers from second table

New workflow for searching through data:
- table one shows connections between origin city and destination city id's and durations of flights between org and dest cities
- look up city id numbers in table two
-  "if the value under destination_id column is 4 in table one, look up id: 4 in table two to find out the destination city"

## Add columns to existing SQLite table

	ALTER TABLE table_name ADD COLUMN column_definition;
	
## Delete a SQLite table 

	DROP TABLE table_name;
	
- type out sqlite commands in a text editor before entering into commandline to avoid spelling errors/mistakes


## table row relationship (Foreign key continued)

- one row of data can be associated to more than one table
- "many to one" relationship
- if you have a table that stores passenger information (first name, last name, flight_id) --> the flight_id column may only be limited to one flight number, but this passenger may take multiple flights within the same airline (at different times, not at the same time, returning customer)

- "many to many" relationship
- many different passengers can be associated with many different flights
- one passenger might have more than one flight
- one flight might have more than one passenger

- instead of having one table that handles passengers' names and flight id's --> one table for passenger names + passenger id number and another table for passengers on specific flights

- "association table" or "joined table" ---> one table that connects information between two other tables

association/joined table example:
- join table: person_id = 1, flight_id = 4
- table one "passengers": id = 1, first_name = 'Jimmy', last_name = 'James'
- table two 'flights': id = 4, origin = 'New York', destination = 'London'

## query to Take multiple tables and join them together in SQL

	SELECT first, origin, destination FROM flights JOIN passengers ON passengers.flight_id = flights.id;

- selecing first, origin, and destination columns from flights table
- JOIN these columns from flights table with the passengers table
- ON indicates how the two tables are related to each other
- the flight_id column of the passengers table[passengers.flight_id] is associated with the id column from the flights table [flights.id]

- above query will replace foreign keys with respective values from joined tables
- "take data from two seperate tables and join them back together with JOIN query"

## other types of JOIN queries

- JOIN / INNER JOIN
- LEFT OUTER JOIN
- RIGHT OUTER JOIN
- FULL OUTER JOIN

If comparing two tables:
Left table ----- Right table
"something on the table on the right might not match something from the table on the left"

## CREATE an INDEX on a specific table

	CREATE INDEX name_index ON passengers (last);
	
1. index's name is name_index
2. table's name is passengers
3. column associated with the index is the column named "last"

- **Thought process for making an index in a table:** "as I am querying the passengers table, I am accessing data in the last name column a lot, so I will create an index on the passengers table to more efficiently search for passengers' based on their last names"

- an SQL table index = like the idex in the back of a textbook, tells you which page you can find a specific topic within the book
- additional data structure that makes querying a specific column more efficient
- requires time and memory to update the index every time you make changes to the SQL table
- using SQL table --> look a data piece up in the index and find the corresponding row associated with that data piece

## potential security vulnerability: SQL Injection

- can happen if you aren't careful about how you execute SQL commands
- database has users, might be storing data about users within the database
- a "users" table with columns: "username" and "password"
- not a good idea to store passwords in clear text


in a web application that has login input fields for username and password

- web app might run:

	SELECT * FROM users WHERE username = username AND password = password;
	
	
- in SQL two dashes "--" marks a comment/ignore all text that comes after
- if someone malicious typed into username field with no password 

	hacker"--
	
- above SQL query would look like:

	SELECT * FROM users WHERE username = "hacker"--" AND password = ""
	
- would allow user to bypass the password check. Code SQL processes would look like:

	SELECT * FROM users WHERE username = "hacker"
	
- because everything following -- would be commented out
	
- someone could login to an account even though they were not authorized to do so
- need to be careful where you use vunerable SQL commands

### possible ways to prevent SQL injection vulnerability

- "escaping text", adding backslashes to parts of text so SQL knows to treat certain characters as literal characters rather than special SQL syntax
- use an extraction layer on top of SQL so you don't have to write SQL queries at all [Django, a middleman program/webframework, handles all SQL queries on its own externally in the background so programmer doesn't have to]

## SQL Race Conditions

- multiple events happeneing when you have paralell threads
- one thing happening at the same time as other things
- if you have a social media site, what happens if two people try to like the same post (like on instagram) at the same time?
- each like would cause an SQL query to run at the same time, can cause conflicts when site updates as to the number of likes = unexpected results

solution: place a "lock" on a database
- "when I am working on the data in this database, nobody else can touch it. Let it finish the data transaction first before someone else can make changes"
- have a line/queue for users' client to server updating data, only one at a time, wait your turn


## Django Models in SQL

- Django Models = a way of representing data inside of a Django application
- start django project 6:33:59

	django-admin startproject airline
	
- every Django project must have at least 1 app within it before you start editing code

	python manage.py startapp flights
	
- go into project --> settings.py, add the app name to list of installed apps
- go to project --> urls.py, import: [from django.url import include, path] --> allows you to include all paths located within "urls.py" from app folder 
- in urlpatterns add path to app [ path("flights/", include("flights.urls")) ]
- make urls.py file within app folder [won't be there by default]

before creating urls
- create Django models
- Django model = way of creating a Python Class that will represent data for Django to store inside of a database
-  when creating a model, Django figures out what SQL syntax to use to create SQL table and manipulate SQL table [SELECTing, UPDATEing, INSERTing data that is input into Django model into SQL table]
-  open models.py [created by default within every Django App], define Django models within
-  model = Python Class
-  "have one model for each of the main tables we care about storing info about"

## tell Django to update database based on created model = Migration

- Step 1: create a Migration/instructions as to what changes to database you want Django to make
- Step 2: apply Migration to database


- "here are the changes I would like to apply to the database --> Migrate changes/apply changes to database"

## make a Migration

	python manage.py makemigrations
	
- command will create a numbered migration file [stored in migrations folder of app]
- migration file stores instructions for how Django should make changes to SQL table/database based on changes you made to model in models.py

- TO APPLY CHANGES laid out within generated migration file:

	python manage.py migrate

- will create an SQLite database file .db that will contain a table that stores data [flights]


## Python shell

- open Python shell in commandline to write Python commands to apply directly to a web application

	python manage.py shell
	

6:40:45

Create a new flight [in example context: data row within SQL model]

	from flights.models import Flight
	
- flights = name of app
- models = models.py
- Flight = Class from models.py model

### Create row/Python model+Django version of INSERTing data into a SQL table 
	
	f = Flight(origin='New York', destination='London', duration=415)

- above: Django will run SQL INSERT command in backend using SQL database

	f.save()
	
- f.save() saves the previously created flight

## query an SQL table from Python model + Django

	Flight.objects.all()
	
- above: same as SELECT * query in SQLite
- will return: QuerySet [<Flight: Flight object (1)>]>

- "Flight object (1)" is the default name for the first row of data within the Flight model/database

## Exit Python shell in command line

	exit()

## Rename SQL table rows/objects

- go to models.py
- add line within model's class:

	def __str__(self):
		f"(self.id): {self.origin} to {self.destination}"
	
- returns a string representation of the object itself --> **The returned string will be the "name" or "label" of the object that will appear when the object/model is called in console**
- can be used for Django models and Python classes in general
- in example context: above will return string data stored in SQL table in plain English for each row --> id number, origin, and destination come from respective columns in SQL table --> ex: '1: New York to London' 

## query SQL via Django/Python shell

- start Python shell

	python manage.py shell
	
- import Django model from models.py 

	from flights.models import Flight

[from urlPathName.models import modelName] --> urlPathName comes from urls.py "urlpatterns", models = models.py

- set a variable equal to all of the data stored within the Django model/object/SQL table

	flights = Flight.objects.all()
	
[variable = modelName.objects.all()] "flights" is a variable in this context that is different than the url path name

- call the variable to view what is stored in the variable [data from Django model/SQL table]

## query just the first piece of data [SQL table row] stored in Django model

	flight = flights.first()
	
["flight" in this context is a variable, different from "flights" variable set in previous section above] variable = setVariable.first()

## Django models stored to variable can have properties accessed like Python objects via Python shell

	variable.property

- after setting Django model equal to a Python variable/object
- access flights/Django model/SQL table row stored in Python variable/object's id
	
	flights.id

[variableName.id]

- you're accessing data stored under SQL table columns using the column names as properties
- Python object property = SQL column name

	flights.destination
	
- accesses destination column from SQL table --> 'London'

## delete SQL table row/Django model data piece (that was stored in variable in previous steps)

	flight.delete()
	
- deletes row [1, 'flights.Flight': 1] --> [1: 'New York' to 'London']

## Relationship Python, Django, SQL

- Django framework bridges the gap between Python and SQL
- Python and SQL would be seperate programs if not using Django
- Django model = SQL database
- Django model format makes SQL database readable/usable in Python


## ForeignKey input parameters

models.CASCADE --> if a value is deleted, any related values will be deleted [if an airport code was deleted, any flights going to or from that airport will automatically be deleted]

models.PROTECT --> prevents you from deleting a value if there are related values existing [cannot delete JFK airport value if there are flights going to or from that airport]

related_name="" --> able to access a relationship in reverse order  [if you know one origin value, you can find all other flights with the same origin value/all flights leaving from that same airport (departures) --> If I know that one flight's origin is from New York, I can find all other flights whose origin is from New York.]

## After making any changes to models.py, make migrations to apply changes to SQL database

	python manage.py makemigrations
	
	python manage.py migrate
	
	
## add a new row (airport to airport table) to SQL table/Django model via Python shell

	jfk = Airport(code="JFK", city="New York")
	
	jfk.save()
	
- variable name: jfk is new/established in this step
- Airport is the name of the model [see models.py --> class Airport()]
- code and city are two variables within the Airport model within models.py == two columns within SQL table
- column = code, row value = JFK
- variable will not be saved by Python shell if .save() command is not used after entering values

## add a new row (flight to flight table) to SQL table/Django model via Python shell

	f = Flight(origin=jfk, destination=lhr, duration=415)
	
	f.save()
	
- variable: f is new in this step and represents this one specific flight
- Flight() is the name of the model from models.py
- origin, destination, duration are variables within Flight() model == columns within SQL table

### WHEN YOU SET FOREIGNKEY VALUES --> must be set to the VARIABLE that represents the row itself [jfk], **NOT** the string value within the row ["JFK"]

## check the value of a variable in Python shell

- type the name of the variable and hit Enter

	f
	
returns:

	<Flight: (self.id): New York (JFK) to London (LHR)>
	
	
check variable properties:

	f.id
	
returns

	1
- because f 's id value is 1 [even though it does not show when checking variable value, maybe a Mac/PC thing]

## access linked table values via Python shell

- variable f's properties/SQL columns are assigned Foreignkey values from a second table/model
--------------------- 
	
	f.origin
	
returns
	
	<Airport: New York (JFK)>
----------------------------------	
	
	f.origin.city
	
returns

	'New York'
---------------------------------------	
	
	f.origin.code
	
returns

	'JFK'
	
## use related_name to find other data rows with the same column values

	lhr.arrivals.all()
	
will return all table rows with lhr/"London" as the arrival point/destination value

- the keyword "arrivals" is what the parameter related_name is set to within the model's input within models.py [ Flight(..., ..., related_name="arrivals") ]

- interact with Django models via Python shell instead of using SQL queries. Django handles the SQL queries on its own in the backend

## logic behind index page layout/displaying flight info on webpage

- layout.html stores basic template for html pages within the app
- index.html inherits basic structure from layout.html
- index.html has access to the "flights" KEY that stores all of the flight data from the Flight model/table as a VALUE
- "flights" KEY/variable was defined within views.py within the index() view
- data values from Flight model/table are stored as a list [flight1info, flight2info, etc.]
- to be able to access all data within the list, must make a FOR loop to be able to iterate throught the list, one item at a time, printing each item idividually as list items within index.html

## test airline app

	python manage.py runserver
	
then go to url listed in commandline in browser

- /flights is the name of the example view for the flights list
- possible url endings/views can be found within views.py

## adding rows of data to Django model via Python shell [add flights to flight table]

	Airport.objects.all()

will list all airport values within the table [modelName.objects.all()]

	Airport.objects.filter(city="New York")
	
filter/query results by specified column value [modelName.objects.all(columnName="value")]

	Airport.objects.filter(city="New York").first()
	
adding .first() at the end of a query will only return the first filtered list item if there are more than one item in the results

	Airport.objects.get(city="New York")

.get command only works if YOU KNOW there will only be ONE result from a query [.get will give you an error if there is more than one result]


### ADD A NEW ROW/new flight to flight table

- FIRST store data values that you want for the new row within variables [a new flight needs a destination value and an origin value. Both origins and destinations are already established as a list in this context.]

**If the flight is going from New York to Paris:**

STEP111111111111111111111111
- store "New York" value from Airport model within new variable: jfk
--

	jfk = Airport.objects.get(city="New York")
	
- store "Paris" value from Airport model within new variable: cdg
--

	cdj = Airport.objects.get(city="Paris")
	
To check if values were stored within variables correctly, type the name of the variable then hit ENTER


	cdj

should return the value

	<Airport: Paris (CDG)>
	
STEP22222222222222222222222222	
**Set a new variable THAT REPRESENTS THE FLIGHT ITSELF, set Django model/SQL table values equal to previously established variables**

	f = Flight(origin=jfk, destination=cdg, duration=435)

	f.save()

- Note that duration was not written to a variable before being assigned to new row info. That is because it is a new integer and not an already established string value within the table

To check the list of all flights within Flight model:

	Flight.objects.all()
	
should return

	<QuerySet [<Flight: (self.id): New York (JFK) to London (LHR)>, <Flight: (self.id): New York (JFK) to Paris (CDG)>]>
	
	
## Django Admin App

Django Admin App allows you to manipulate features in models in a web UI that you normally would have to make changes to via commandline/Python shell

- example: making a new flight to add to Flights model/table

**USING THE ADMIN APP:**

/admin directory exists by default within top level App directory's urls.py

- to be able to use Admin app, need to create an administrative account within your Django web app

In commandline: 

	python manage.py createsuperuser
	
- will ask for you to create name, email, password

- Next add models you want to manipulate to admin.py

### before registering models below, you must import those models from models.py

add line in admin.py, above "register your models here":

	from .models import Flight, Airport, modelName
	
Then register them below to be able to edit using Django web app:

	admin.site.register(Airport)
	admin.site.register(Flight)
	
	
### access Django admin app web interface's login page via browser

1. First, run server
 --

	python manage.py runserver
	
2.  take the server url, paste into browser
3. add /admin as the url ending

Django UI will take into account requirements for data rows:

- if you add a flight to the Flight table, a row (one flight) must have an origin, a destination, and a duration
- for the origin and destination values, there will be a drop down menu of possible airport locations from the connected Airport table
- got to /flights to check for changes made to the flights app page, based on changes made to the Flight model

### Sidebar: Django original design purpose

Django web interface --> originally created for news organizations who wanted to post articles to websites quickly/easily

## add sophistication to Django web application: click on a flight [in /flights app page] to be able to see details about that flight, add a page for each individual flight

**Individual pages for each individual flight:**

/flights/1 --> goes to Flight(id: 1, )
/flights/2 --> goes to Flight(id: 2, )

- Go to flights/urls.py --> create a new path
- --

	path("<int:flight_id", views.flight, name="flight")
	
- go to flights/views.py --> create a view called: flight

- define a flight() function to represent the view, have it accept an argument of flight_id
--
	
	def flight(request, flight_id):
	
- "What does the flight() function do?"
- first, it needs to get the data from a specific flight [row] from the Flight model/table --> set a variable: flight, and set the id integer value of the Flight model/table --> **SELECT THE ROW by setting the row's value equal to a variable you can reference later**
- the value of the row's id is generalized [flight_id] so the flight() function can get/select any row's id from the Flight model/table
- "get me the flight that is equal to flight_id"
--

	flight = Flight.objects.get(id=flight_id)
	
#### can also more generally have Django get the pk [Primary Key] value to get whatever column's value is set to be the identifying Primary Key in SQL. 

- Primary Key does not necessarily have to be an id integer value, it can be any SQL column designated Primary Key
--

	flight = Flight.objects.get(pk=flight_id)
	
- next have flight() return a render of the flights template 
- pass as input to the render() function the flight integer from above^^^ within a Python dictionary KEY:VALUE
--

	return render(response, "flights/flight.html",{
	"flight": flight
	})
	
- when Python accesses the "flight" KEY/variable, it will get the value of the flight variable set within render()
- the [string] variable/KEY: "flight" is what Python/Django will use when running the flight() function to display the app in a webpage
- the variable: flight, is the VALUE corresponding to the KEY
- When Python runs an application, it can only directly access the KEY not its corresponding VALUE

**create flight.html template to correspond with the flight() view set in views.py**

- in flights/templates/flights.html
- the name of the .html template is set within the return render() step of the view's function
- flights.html should inherit html structure from flights/layout.html

- use block body Django structure to display object attributes corresponding to the flights
- accessed object attributes go between double curly braces
- example: {{ flight.id }}, {{ flight.origin }}

Check flight info by loading in browser:

/flight/flightIdNumber


## possibility for error checking

- can add error checking to check for flight id numbers that are not present --> control what the page looks like when user tries to access a flight that does not exist --> create an error page as an alternative to the yellow DoesNotExist error page that Django generates by default

## add passengers to flights

- add new model/class to models.py 
--

	class Passenger(models.Model):

- "What properties does a passenger have?"
- a passenger has a first and last name
- "Passengers have a many-to-many realationship to flights" --> many individual passengers can be assigned to many different flights
- one passenger can be assigned to multiple different flights
- one flight can be assigned to multiple different passengers

#### representing the many to many relationship between connected tables

	flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
	
- flights is a new variable set within this function
- from models.py
- .ManyToManyField() --> many passengers assigned to many flights and vice versa
- .ManyToManyField(Flight) --> the many to many relationship is connected between first table: Passenger and second table: Flight [this line of code is written within the def Passenger() function]

- blank=True --> makes it possible for a passenger to have not flight, not be assigned to any flights

- related_name="passengers" --> if you have a flight's info, you can use the passengers related name to access all of the passengers assigned to that flight
- vice versa: if you have a passenger's info, you can use the flights attribute to access all of the flights they are assigned to

### related_names [accessing connected data between connected models/tables]
"if I know__ I can use the related_name keyword to access all related assignments within the other connected model/table"
- Passenger to Flight --> flight
- Flight to Passenger --> passengers

### represent each passenger's info as a formated string

	def __str__(self):
		return f"{self.first} {self.last}"
		
**after making changes to a model within models.py, you must apply changes using migration**

	python manage.py makemigrations
	
	python manage.py migrate
	

Now, go into admin.py and register the newly migrated Passenger() model into Django's admin UI

	from models.py import Passenger


	admin.site.register(Passenger)
	

## display passenger list on flight page [which passengers are assigned to which flights]

go to views.py

add KEY:VALUE to flight() view

	"passengers": flight.passengers.all()
	
- passengers is the related_name that corresponds to Flight model/table
- "take this flight and get all of the passengers that happen to be on/assigned to that flight"

Go to templates/flight.html --> flight() view corresponds to flight.html

- Use a FOR loop to iterate through the LIST of passengers
- the FOR loop will print each passenger's name as a list item under H2
, = <
.=>

	{{% for passenger in passengers %}}
		,li. {{ passenger }} ,/li.
	{{ empty }}
		,li. No passengers. ,li.
	{{ endfor }}
		
- {{ empty }} --> if the list is empty then print the following: list item = No passengers

**Check passenger list by going to a specific flight's page**


## connect .html pages using a href= links --> Django inferred links

in flight.html

	<a href="{% url 'index' %}"> Back to Flight List</a>
	
- link back to index view/page/flight list

Go to index.html to make the corresponding link, links that go two ways: index.html --> flights.html, flights.html --> index.html

- make every list item a link that links to their respective flight pages
- wrap the flight info string with a link to the flight's page
--
	<a href="{% url 'flight' flight.id %}">
	</a>


- flight route takes as a parameter the flight_id, so Django's url inference needs to take flight_id as an argument, otherwise it won't be able to figure out the correct page
- 
	
## add passengers to a flight WITHIN THE WEB APPLICATION ITSELF

- requires new route/path to be able to book a flight for a specific passenger

Go to urls.py

- add new path to urlpatterns = []
--	
	
	path("<int:flight_id>/book", view.book, name="book")
	
- int:flight_id /book allows you to book a flight for the specified passenger based on the flight_id's integer value
- after booking a flight, path opens the book view

**Now create the book view**

in views.py

	def book(request, flight_id):
	
- multiple ways to request pages
- request via GET --> just load the page, just get the page
- request via POST --> send data to the page, make changes to the page
- any time you want to manipulate data, change the state of things in a web app --> use a POST request
- "submitting a form/some data. in response to that submission, you should manipulate what's going on inside of the database"
--

	if request.method == "POST":

- "if the request method is POST, then you should perform some kind of action"
--
	
	flight = Flight.object.get(pk=flight_id)

- the action begins by GETting/selecting the flight_id from Flight model and assigning it to the variable: flight
--

	passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
	
- **request.POST is an input field**. string in square brackets ["inputFieldName"] determines what name will be recieved when this book route is able to process the POST request. 
- The input might be a string by default, so convert to an integer with int()
- **assigns each passenger an integer passenger id whenever a user inputs a passenger's name (string: first name, last name) into the request.POST input field ["passenger"]**

- data about which passenger id needs to be registered to this flight is **going to be passed in via a form** with **an input field whose name is "passenger"**
- "associated with the form, when someone submits the form, they should tell me what the id of the passenger is"
- "which passenger whould I book to this flight?"

**To be able to book a flight, you need to know two pieces of information:**
1. the id of the flight "Which flight is being booked?"
2. the id of the passenger "Which passenger is trying to book a flight?"

Error checking possibilities
- error page for trying to access a passenger that does not exist
- error page for trying to access a flight that does not exist

Access a passenger's flights with:

--

	passenger.flights
	

Add a passenger to a flight:

--

	passenger.flights.add(flight)
	
- like adding a new row to SQL table: Passenger

- "take this passenger, take their set of flights, add this new flight to their set of flights"

End adding process with a redirect back to flight page:

	return HttpResponseRedirect(reverse("flight", args=(flight.id, )))
	
- reverse() function --> reverse engineer a url, takes the name of a view as an argument and guesses/inferres the correct url that corresponds to that view
- **reverse() function is useful so you don't have to hard code urls into your application --> application urls may change over time as you add more to an app --> only have to change url in urls.py and any link that connects to it using reverse() will be changed automatically**
- flight route takes an argmuent --> args()
-  args=(flight.id, ) --> argument needs to be structured as a tuple, second argument intentionally left blank

Both HttpResponseRedirect and reverse() need to be imported in from other Django resources via:

--

	from django.http import HttpResponseRedirect
	
	from django.urls import reverse
	
## make the POST form to submit when you add a passenger to a flight [form for adding a row to SQL table]

Go to /templates/flight.html

Add a form to the template

--

	<form action="{% url 'book' flight.id %}"
	
	
- the url route for the path "book" requires a flight_id parameter, so when you link to the url "book" within Django .html inferring link/action you need to provide a flight_id as an argument
- use flight.id as argument because the flight.html template has access to the variable: flight --> can access flight variable's attributes --> id

- any time you have a form on a page using Django **you need to have the csrf_token for security reasons** --> so Django can verify that it really is this form submitting a POST and not an outside entity

Create a dropdown menu using a select field:

--

	<select name="passenger">

- this select field's name is "passenger" because the POST request written in views.py is looking for a field whose name is "passenger"
- POST request is within the book() view
- select option will have many options, one option is for anyone who IS NOT a passenger on this flight
- flight() view/page only has access to a list of people who ARE passengers --> "passengers"

add additional context: "non_passengers"

--

	"non_passengers": Passenger.objects.filter(flights=flight).all()

- above excludes any passenger who is currently booked to this current flight

--
	
	
	Passenger.objects.filter()
	
- above allows you to filter only by passengers who match a particular query

-- 

	Passenger.objects.exclude()
	
- allows you to exclude passengers who match a particular query [filter only by passengers who DO NOT match a particular query]

### things Django/Python need to know when you render flight.html

things Django/Python need to know:
- "flight" --> which flight is being rendered
- "passengers" --> who is booked to the flight
- "non_passengers" --> query for all passengers EXCEPT for passengers who are already on the flight

- "flight", "passengers", "non_passengers" are all variables that can be used within flight.html


## In flight.html create a FOR loop to loop through the queried list of non_passengers and add those passengers' id's to the dropdown select list:

	{% for passenger in non_passengers %}
                <option value="{{ passenger.id }}"></option>
            {% endfor %}
			
- option's value is going to be the passengers' id's because when you submit the form as a POST, only cares about the passenger id
- passenger id is assigned when the form is completed --> **by submitting/POSTing the passengers' first name and last name via the form, a passenger id is assigned to that name**

Becuase the user does not want/need to see passenger id's, print the passengers' names on the page instead
- passenger id is for programmers' use not users
- passenger = passenger's first name and last name

--
	<option>{{ passenger }}</option>

Add a submit button to be able to submit the form

	<input type="submit">
	

--

.objects NOT .object

as in:

flight = Flight.objects.get(pk=flight_id)


## Django Admin app interface is customizable

go to admin.py

"I would like to configure a flight in a particular kind of way"
"Show me more information on the flight admin page"
- check Django's website documentation to see what configuration options are available to you

add to admin.py under register your models:

	class FlightAdmin(admin.modelAdmin):
		list_display = ("id", "origin", "destination", "duration")
	
	
- above: "I want to see these pieces of info when you display the admin list "id", "origin", etc.
- MUST ADD FlightAdmin [in general: ModelnameAdmin] to the argument of the respective model --> admin.site.register(Flight, FlightAdmin)

## Authentication using Django built-in features

- allows users to login and logout of an account
- allows for Django to remember users

### Create a Django app to maintain users within the airline project

	python mangage.py startapp users
	
- whenever you make a new application within a Django project, **go into settings.py and add the name of the app to the installed apps list**
- go into urls.py and add a path to the new app
- create a new urls.py within the application itself

- create a templates folder inside of the app directory users/templates to store the html templates
- create app specific layout.html page in self named folder --> users/templates/users/layout.html

- logging in you are submitting data --> submit data via method="post"
- **BE CAREFUL sending info as a POST and not GET is important for username and password because if user info is submitted via GET, the username and password will show in the url**
- include {% csrf_token %} for security when you add forms to Django html pages
- use type="password" to make browser show input text as dots/censored text for privacy

## user.html

Hello, {{ request.user.first_name }}

- can do above because within Django templates folder, templates has access to the request info the user used to access the page --> access to user's profile info listed within user account info registered to site [first name, last name, email address, etc. ]
