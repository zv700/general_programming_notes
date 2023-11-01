## Commandline/terminal

### change directory

	cd
	
ex. 

	C:\Users\Kauntuch\cd Downloads

- if you are within a parent/upper directory that contains the desired directory, you don't have to write the whole path

- If I'm currently in:

	C:\Users\Kauntuch

- to change directory to the Downloads folder I only have to write:

	cd downloads
	
- because the Downloads folder is located inside the Kauntuch folder
	
	
### list all files and folders in current directory:

	dir
	
ex:

	C:\Users\Kauntuch\dir	
	
- above lists file/folder names, date and time created, number of directories/folders and files, amount of free storage space in bytes
- folders will have <dir> tag
- files will instead have file size in bytes

### record results of dir command in a text file

	dir > fileName.txt

ex.

	C:\Users\Kauntuch\dir > fileName.txt

- above writes the results of dir command in a text file called: "fileName.txt" in the same directory
- replace "fileName" with whatever name you want for the .txt file

### display the contents of a text file in commandline

	type fileName.txt

ex.

	C:\Users\Kauntuch\type fileName.txt


### add content to a text file

	echo

ex.

	echo Your text here >> fileName.txt

- above outputs the text "Your text here" into a file called: "fileName.txt"
- if the specified file name does not exist, the command will make a new file
- if the file already exists, the command will add the specified text on a new line of that specific file
- **TWO** greater than signs >> will ADD the text/string to the text file
- **ONE** greater than sign > will OVERWRITE the contents of the file with whatever string you enter


	echo Overwrite all of the text in the file > fileName.txt

## Output the contexts of one text file to another text file (copy the file)

	type fileName.txt > secondFileName.txt

- above creates a new file coalled: secondFileName.txt if it doesn't already exist, copies the content of fileName.txt into secondFileName.txt
- note: one greater than > will overwrite the contents of the specified file if it already exists

### Open a text file in Notepad from command line/open files from command line using default program

	notepad fileName.txt

- if Notepad is your default text viewer, you only have to type the text file name and hit enter to open it in notepad
- if you enter ANY file name in commandline without specifying a program to open it, Windows will try to open with the default program used to open that type of file

ex.

		C:\Users\Kautuch\Downloads\catPicture.png

- above will open catPicture.png in the default Windows Photo Gallery app
