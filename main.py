

import os,random
import time, sys
def typewriter(message):
	for i in message:
		sys.stdout.write(i)
		sys.stdout.flush()
		if ((i != "\n") and (i != ":")):
			time.sleep(0.08)
		else:
			time.sleep(0.2)
			
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bblack = "\033[0;90m"
bred = "\033[0;91m"
bgreen = "\033[0;92m"
byellow = "\033[0;93m"
bblue = "\033[0;94m"
bmagenta = "\033[0;95m"
bcyan = "\033[0;96m"
bwhite = "\033[0;97m"
os.system('clear')
typewriter('What is your name?\n')
name = input('       >>>  ')

### Prep done, type work now!!!
os.system('clear')
typewriter(green + 'Hi! I\'m zoom bot! I\'m an alogrithm designed for your specific needs!! I think that your name is ' + bwhite + name + green +  '! Now, I know I\'m having a good day, but are you??')
time.sleep(2)
os.system('clear')
typewriter('Let\'s talk commands. I am currently in Beta, so I\'m still learning, but I have a current list of them! Type eList in the console to see the list! When asking a question, make sure you spell EVERY word right, so I can understand what you are saying a little bit better.')
typewriter('That is enough of that, let\'s get started!')
time.sleep(2)
os.system('clear')
print('Ask me anything!\n')
a = input(green + '')
def Elist():
  if a == "eList":
    os.system('clear')
    typewriter('Here are the commands!\n')
    os.system('clear')
    print(red + 'eClear')
    print(green +'Cleans the console memory and everything currenty on it.')
    print()
    print(red + 'eTime')
    print(green + 'Will make the computer wait a select amount of time')
    print()
    print(red + 'eTypewriter')
    print(green + 'Will make the typewriter effect happen to any of the text you input')
    print()
    print(red + 'ePython')
    print(green + 'Will teach you the basics of python!')
    print()
  print(red+ 'ePrint')
  print(green + 'Will print any text that you input')
  




  if a == "eClear":
    os.system('clear') 
    del a, black, red, green, yellow, blue, magenta, cyan, white, bblack

  

	

