#!/bin/bash

if [ -z "$1" ]
then
	echo "Error: Please provide a filename"
	echo 'Usage: ./git-push.sh filename "commit message"'
	exit 1
fi

if [ -z "$2" ]
then 
	echo "Error : Please prove a commit message"
	echo 'Usage: ./git push.sh "commit message"'
	exit 1
fi

git add "$1"
git commit -m "$2"
git push

