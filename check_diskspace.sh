#!/bin/bash

file=$(free -mt | grep "Total" | awk '{print $4}')
dh=2527

if [[ $file -lt $dh ]]
then
	echo " Your disk space is running low"
	
else 
	echo " Ram is sufficent $file "
fi
