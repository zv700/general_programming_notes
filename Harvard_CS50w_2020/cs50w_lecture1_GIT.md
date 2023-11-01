## GIT = version control tool

- command line tool
- allows you to keep track of changes made to code
- lets you store projects online
- saves "snapshots" of parts of code at different points in time, like savestates
- syncronizes code between different people
- one version of code: the repository
- multiple people can access the same repository at the same time
- if someone makes a change to repository, changes are PUSHED back up to the server so server will have most recent/up to date version of repository
- PULL changes from server = recieve latest version of code stored on server
- can test changes to code without losing the original code
- making changes to code may break it/make it not work so it's good to have acces to the last version of code that worked
- make changes to code on a SEPERATE BRANCH
- when satisfied with changes made within BRANCH, you can MERGE the branch with the main REPO/original code
- allows you to revert code back to old versions


## GitHub = site that stores GIT repositories


## Git commands

- "Git clone"
- Git clone command downloads GitHub repository from internet to computer/makes a clone or copy of repo locally on your computer

## Commandline/terminal

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

## Create new repository via commandline

GitHub instructions:
- echo "# Hello-CS50-Python-JavaScript" >> README.md
- git init /path/to/directory/containing/code
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/Kauntuch/Hello-CS50-Python-JavaScript.git
git push -u origin main

1. echo "" >> readme.md creates a readme file and writes the name of the repository to the readme file
2. git init starts Git in commandline/initializes the program: Git (Git will start in the current directory, cd to your desired directory)
3.  git add README.md loads the readme file in Git/gets it ready to be uploaded
4.


- git init is a one time action (only needs to be done once)
- cloning a repository is a one time action
- cloning copies the latest version of main branch of remote repo stored on GitHub 
- clone will include a full history of the remote repository

- Git SSH URLs follow template:
git@HOSTNAME:USERNAME/REPONAME.git

ex.

git@bitbucket.org:rhyolight/javascript-data-store.git

HOSTNAME: bitbucket.org
USERNAME: rhyolight
REPONAME: javascript-data-store

- git push
- you push or pull commits from one repository to another (local to remote, remote to local)
- can designate a specific repository in a project as "central" so collaborators' branches all contribute to one final project


- "ls" command lists all files in current directory (on Mac?)
**- "dir" command lists all files in current directory (on Windows)**

- "touch" command creates new file (on Mac)
**- "echo" command creates new file (on Windows) (see commandline section of notes for more details)**

## Making a commit = making a savestate of the files of a repository

- like saving progress via savestate within a game emulator/saving progress in a game at a savepoint
- like taking a snapshot of what the files within a repository currently look like

## Git add

	git add <filename>

- "git add" command tells Git to add a file for it to track the next time you commit/save progress
- have to manually add files to list of files that git will save to the repository with the next commit
- you won't necessarily want to add/save all files at once because you might still be working on some files that are not ready to be commited
- only have to add files you've finished working on for now that have been changed
- git add only adds files to the list of files to be commited, does not actually commit/save any files to the repository

## Git commit

	git commit -m "message"

- "git commit" will save added files to the repository
- -m stands for message (as in: commit changes while adding a message)
- after -m write a "commit message" or a description of changes made with this specific commit
- commit messages make it easier to track when specific changes were made, and to be able to identify later what changes need to be reverted or revise if something breaks
- commit message must be in double quotes ""
- insertions = number of lines added to files

## Git status

	git status

- "git status" tells us what is currently happening within repository
- git status will tell you which files had changes made to them, but WERE NOT added to commit list

"your branch is ahead of 'origin/master' by 1 commit. (use "git push" to publish your local commits)"

- above: your local version of the repo has changes made that have not been made to the origin (online) version of the repository
- "I have one commit ahead of the origin/master"
- commit changes need to be finalized by sending them to the online GitHub version of your repo with the "push" command

## Git push

	git push

- take all of the changes I have committed and **push/upload** them to GitHub

## Commit all changes simultaneously (NOT WORKING FOR ME, MAYBE MAC ONLY)

	git commit -am <your message here>

- -a stands for "all" (as in: commit all changes)
- commit -am = commit all changes, while also leaving a commit message
- combines "git add" and "git commit" steps

IF ABOVE DOESN'T WORK, USE THIS INSTEAD:

	git add --all

- above adds all changes to commit list of changes

then

	git commit -m <your message here>

- run commit normally
- instructor presented a way to combine "add" and "commit" steps: -am (could be operating system difference; he was on Mac and I'm on PC)
- above two steps at least will reduce the number of "add" commands that need to be run before committing

## Git pull/download latest version of repository from GitHub 

	git pull

- use if the online GitHub version of the repository you're working with is newer/more up to date than what you have stored locally (if someone else is working on same file)
- pull = download most recent changes to the repository from GitHub

## Merge conflicts

- if two different people are working on the same part of code and both try to sync changes online, conflicts can happen when different people make changes to the same lines of code: merge conflict
- running into merge conflicts, Git doesn't immediately know what to do
- running a pull request will fail, Git will ask you to fix conflicts then commit the result

- anything between LESS THAN arrows <<<< and equal signs === are YOUR changes
- anything between equal signs === and GREATER THAN >>> arrows are REMOTE changes/someone else's changes/what changes are stored on GitHub that you're trying to pull that conflict with what you have locally
- numbers and letters after remote commit/greater than signs >>> 546f4545 is the HASH of the confilcting commit 

a = 1
<<<<<<<<<<<<<<<<
b = 2
=======
b = 0 
>>>>>>>>> 5413f15

- HASH = every commit has a sequence of numbers and letters to identify it, Git automatically generates a hash for every commit

### STEPS TO RESOLVE MERGE CONFLICT
- after git gives you a merge conflict error when trying to push changes

1. commit your changes (again)
2. pull GitHub's version of repo with merge conflict
3. in code editor, remove all merge conflict added markers (<<< ===  >>>, hash) and blank lines from the text file
4. for conflicting lines of code, choose between changes you made locally or the remote changes GitHub has stored, OR combine changes between local and remote
5. commit changes
6. push changes

## Git log

	git commit

- used to keep track of all changes/commits made to repo
- will tell you commit hash (id number), who made the commit, what time the commit was made, and the accompanying commit message


## Git reset

	git reset

- for when you made a change you didn't want to make, 
- revert current state of local repo to previous version of repo

	git reset --hard <specify specific commit hash>

- revert back to a specific commit using the commit's hash
- run git log to get specific commit's hash or check GitHub for hash
- --hard = hard reset

	git reset --hard origin/master

- origin/master = current version of repo stored on GitHub
- revert local repo to current online/remote version 

## Making changes to repositories (hypothetical situations)

## Branching
- make changes to different parts of code simultaneously
- seperate code for different portions of a project into different branches, so later changes to one section do not affect previous sections
- if you're working on multipe features all on one branch, take a break from working on one to implement another, only to find bugs in the previous dormant feature, you might lose progress trying to revert changes, independant branches prevent that issue
- multiple branches can combine later to make up the main/master branch
- master branch/main branch usually has the most up to date stable version of repoository, implement bug fixes
-new features go in seperate branches, like an additional DLC campaign corresponding to the main standalone game
- HEAD determines which branch you are focusing on, like selecting an option from a list of options
- HEAD can be changed at any time, "switching where your HEAD is"
- when satisfied with main stable branch and side branch features, can merge branches into master branch later
- branching = work on multiple things at once without disrupting/contamination between main and features
- maintain a stable foundation seperate from additional new features until features are stable enought to implement in the main branch

### Git branch

	git branch

- command tells you which branch you are currently on
- tells you what branches exist in the repository
- "*" next to branch name tells you which branch is currently selected

## Create new branch/checkout branch

	git checkout -b <nameofnewbranch>

- -b means new branch
- git automatically switches to new branch after creating it
- changes made to selected branch won't affect other branches

## Git checkout to switch branches

	git checkout <nameofbranch>

- use git branch to see all available branches
- "git checkout main" to switch to the main branch if another branch is currently selected

## Git merge

	git merge <selectedbranchtomerge>

- attempts to merge specified branch with the currently selected branch
- If I have the "main" branch selected and I want to merge changes from the "style" branch, type: git merge style
- may result in merge confilcts
- merging branches into main branch will remove the non-main branch
- be careful of editing the same lines of code across different branches to prevent merge conflicts

## Forking a GitHub repository

- open source code = publicly available for anyone to look at and also for anyone to contribute to, community driven effort to improve program/code
- forking = make your own copy of someone else's repository, copies the repository into your own GitHub account
- forking is useful if you want to contribute to an open source project or if you want other people to be able to contribute to your own repository
-not safe for just anyone to be able to edit every open source project
- fork your own copy of an open source project (like bootstrap) that you can commit, push, pull to privately
- when you think you've finished making your own contribution to the open source project you put in a PULL REQUEST
- pull requests become openly available on the original version of forked repository
- people who maintain the original repository decide whether or not to accept a pull request/merge the changes you made into the main repository
- maintainers can provide feedback, ask for additional changes, and merge changes when everyone is satisfied


## GitHub pages

	<yourusername>.github.io

- above: conventional name for Github page
- allows you to make/host a website via GitHub
