#!/bin/bash

# monitoring the free fs space disk

FU=$( df -h | egrep -v "Filesystem|tmpfs" | grep "sda3" | awk '{print $5}' | tr -d % )
TO="itpiyushkumar6@gmail.com"


if [[ $FU -ge 40 ]]
then
	echo "Warning, disk space is low" | mail -s "Space low" $TO
else 
	echo "All good $FU"
fi 
