#!/bin/bash
#sarah sahibzada
# MATH 491
#automate the process of generating a random sample of GCD data for pairs of numbers up to a certain 
#number of digits. created to remain consistent with data acquisition by stephen capps
echo "This program will generate data sets of GCD data for numbers from 1 to a user-specified length."
echo "A user-specified number of pairs will be generated per number, and written to a CSV file."
echo "YOU ONLY NEED TO ENTER VALUES ONCE! :-) I DO EVERYTHING ELSE!"
echo "Enter the maximum number of digits. I will generate datasets from 1 digit to that max number of digits."
read maxNumDigits
echo "OK, I will generate $maxNumDigits data sets, from 1 to $maxNumDigits."
echo "How many pairs per CSV file?"
read numPairs
echo "Okay, I will make $numPairs pairs per CSV file."
echo "I will output these files to a directory of your naming. What will that directory be called?"
read dirName
echo "Okay, writing files. Stand back--this might take a while...."
echo "--------------------------------------------"
OPT=2
COUNTER=0
SLASH="/"
DATA="dataFor"
DIGITS="Digits"
mkdir -p $dirName
cp testEEA.java $dirName
cd $dirName
javac testEEA.java
while [ $COUNTER -le $maxNumDigits ]; do
	echo "--------------------------"
	let COUNTER=COUNTER+1
	java testEEA <<-EOF
	$OPT 
	$numPairs 
	$COUNTER
	$DATA$COUNTER$DIGITS
	EOF
done
echo "Thanks and gig em."
	  	
