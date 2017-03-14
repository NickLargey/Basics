# Simple program to check weather from the command line

import webbrowser, sys
zipcode = input(">>> What's your zipcode: ")
webbrowser.open('http://www.weather.com/weather/today/' + zipcode)