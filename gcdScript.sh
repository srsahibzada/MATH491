
#!/bin/bash
#sarah sahibzada
#MATH 491
#due to the time it takes to run this many times, i have written a bash script to automate the process
#will generate a user-specified number of csv files and the corresponding bezout lists
echo "This program will run the EEA generator 1000 times."
#hard code in 2 to generate CSV
echo "Hello! I am a silly bash script that will run a program for you while you go about your busy life :-)"
echo "YOU ONLY NEED TO ENTER VALUES ONCE! :-) I DO EVERYTHING ELSE!"
echo "Enter the number of digits in the random numbers to generate."
read numDigits
echo "OK, generating pairs of numbers that are $numDigits long."
echo "How many pairs do you wish to generate per CSV file?"
read numPairs
echo "OK, I will make $numPairs pairs per CSV file."
echo "Great! How many files do you want me to generate?"
read numTimesAnswer
#numTimesAnswer=1000
echo "These files need names, though. Give me a base name and I will do the rest of the work for you."
read fileName
echo "Awesome. I will generate $numTimesAnswer CSV files. Stand back--this might ake a while...."
echo "---------------------------------------------------"
OPT=2
#oproc java testEEA
COUNTER=0
while [ $COUNTER -lt $numTimesAnswer ]; do
        echo "--------------------------------"
        java testEEA <<- EOF
        $OPT
        $numPairs
        $numDigits
        $fileName$COUNTER
        EOF
        #pawn ./gcdScript <testEEA.java
        #expect "This program will generate data on the Euclidean algorithm using random numbers of a user-specified length. Do you want this as:"
        #expect "[1] A .txt file"
        #expect "[2] A .csv file"
        #send "1"
#       expect "How many pairs do you wish to generate?"
#       send "$numPairs"
#       expect "How many digits long do you want the numbers to be?"
#       send "$numDigits"
#       expect "Name the file (do not include file extension)."
#       send "$fileName"
        let COUNTER=COUNTER+1
done
#at <&${COPROC[0]}
echo "Thanks and gig em!"
