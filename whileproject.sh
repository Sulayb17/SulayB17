#!/bin/bash

echo -n "Print message?"

valid=0

while
[ $valid == 0 ]
do
	read ans
	case $ans in
	yes|YES|y|Y )	echo will print the message
			echo The message
			valid=1
			;;
	[nN][oO]    )   echo will NOT print the message
			valid=1;;
	*	    )   echo Yes Or No of somme form please ;;
	esac
done

