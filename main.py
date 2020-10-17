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

#####Prep done, type work now!!!
os.system('clear')
typewriter(green + 'Hi! I\'m zoom bot! I\'m an alogrithm designed for your specific needs!! I think that your name is ' + bwhite + name + green +  '! Now, I know I\'m having a good day, but are you??')
time.sleep(2)
os.system('clear')
typewriter('Let\'s talk commands. I am currently in Beta, so I\'m still learning, but I have a current list of them! Type eList in the console to see the list! When asking a question, make sure you spell EVERY word right, so I can understand what you are saying a little bit better.')
typewriter('That is enough of that, let\'s get started!')
time.sleep(2)
os.system('clear')

def aa():
  print('Ask me anything!\n')
  print()
  a = input(bcyan + '')

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
    print()
    print(red + 'eGame')
    print(green + 'Will let you play a short game')
    print()
    print(magenta + 'eL')
    print(green + 'Leave any command')
    print(red + 'Would you like to leave or demo exacute a command?')
    a = input('')

  




  if a == "eClear":
   os.system('clear')
   aa()
  elif a == "eL":
    os.system('clear')
    aa()
  elif a == "eTime":
    typewriter('What amount of time are we exacuting?\n ONLY USE NUMBERS\n')
    tim = input('Time = ')
    print('IMA IGNORE THAT AND DO 3 SECONDS')
    time.sleep(3)
    os.system('clear')
    aa()
  elif a == "eTypewriter":
    typewriter('Want to to type like me! This is the page for you! Just type now what you want said!')
    print()
    timm = input('>>> ')
    time.sleep(1)
    typewriter(timm)
    time.sleep(2)
    os.system('clear')
    aa()
  elif a == "ePrint":
    typewriter('What text would you like to be exacuted?')
    print()
    timmm = input('>>>>>')
    time.sleep(1)
    print(timmm)
    time.sleep(2)
    os.system('clear')
    aa()
  elif a == "ePython":
    os.system('clear')
    typewriter('Here are your choices for classes\n')
    print('a) Beginner')
    classe = input('')
    if classe == "a":
       os.system('clear')
       typewriter('Welcome beginners! Here are a few classes that are availible! ')
       print(red + 'print function')
       print()
       print('Variables')
       print()
       print('In print functions')
       print()
       print('')
  else:
    typewriter('Command not found')
    time.sleep(2)
    os.system('clear')
    aa()
###dfdfeifjifhdsjhfdsjkfhdsjhfdshfgsfgdhfgdshfdsfhgsd


aa()
<h1>
	dfff
</h1>
