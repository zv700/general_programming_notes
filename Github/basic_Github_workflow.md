1. cd <local directory of repo>
2. git add <filename>
3. git commit -m "your commit message here"
4. git status
5. git push
6. check GitHub to see if changes were made

1. change directory to the local directory of your repo
2. after finished working on files, each individual file you want to upload to GitHub needs to be added to the list of files to commit
3. after finished adding all individual desired files to commit list, use commit command. Include a "commit message" in double quotes"" as a note to yourself indicating what changes were made with this specific commit
4. git status - check the status of git before pushing/uploading local files up to the server
5. git push - push uploads commited files to the server
6. check GitHub for changes

## Additional options

git commit -am <your message here>

- -a stands for "all" (as in: commit all changes)
- commit -am = commit all changes, while also leaving a commit message
- combines "git add" and "git commit" steps

IF ABOVE DOESN'T WORK:

	git add --all

	git commit -m <your message here>

- above: add ALL edited files within the repository at once, then commit + leave a commit message
- so you don't have to add every individual changed file

- if you forget to add a commit message, commandline will open "vim text editor" (blue text)
- press "i" to enter insert mode
- type your message
- pres "esc" to exit insert mode
-type ":wq" then press enter to submit text/changes
