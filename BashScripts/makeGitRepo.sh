#! /bin/bash

# This script will only work with the HTTPS link of github. Not the SSH link.

echo "Hello! Welcome to the desktop git repo maker!

If you have not already made your GitHub repo and copied the link,
please do so and have it ready! Press CTL+C to exit if you need
time to get it ready. 

If you have already made your GitHub.com repo, copy the
link and have it ready to type in about 10 seconds."

sleep 15

echo "What would you like the Desktop repo to be called?"
read desktopName
echo "What is the HTTPS GitHub link for the repo?"
read githubLink

mkdir $desktopName
cd $desktopName
git init
echo "This is a repo called: "$desktopName > README.md
git add README.md
git commit -m "Add README and initialize git repo"
git remote add origin $githubLink
git push -u origin master
echo "Repo has been initialized at: "$githubLink
