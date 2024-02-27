#!/usr/bin/python3
# Script Name:                  Challenge 37 Cookie Capture Capades
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      02/27/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-401d10
# Purpose:                      Objectives

# Copy the demo script for today as your template for this challenge.

# Complete the objectives listed at the bottom of the demo script.
# Make Cookie Monster proud!

import requests

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Send the cookie back to the site and receive a HTTP response
sweets = requests.get(targetsite, cookies=cookie)

# Generate a .html file to capture the contents of the HTTP response
html_content = sweets.text
with open('sweets.html', 'w') as f:
    f.write(html_content)

# Open it with Firefox
import subprocess
subprocess.Popen(['firefox', 'sweets.html'])
