#! /bin/bash

echo "Welcome! 

Type your location below for a 3-day weather forecast of your
desired area (in lower case), or just press ENTER to have it
load the weather for the location connected to your IP-address!"

echo " "

echo "Desired location with no spaces(city,state/country): "

# Allows for user input
read location

if [[ -z "$location" ]]; then
    curl wttr.in
else
    curl wttr.in/$location
fi

