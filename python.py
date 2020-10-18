import os, random, time, sys 
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
def python():
	  os.system('clear')
    typewriter('Here are your choices for classes\n')
    print('a) Beginner')
    print('b) Intermedate')
    classe = input('')
    if classe == "a":
       os.system('clear')
       typewriter('Welcome beginners! Here are a few classes that are availible! ')
       print(red + 'a) print function')
       print()
       print('b) Variables')
       print()
       print('c) In print functions')
       print()
       print('d) If, elif')
       py = input('Which course?').lowwer()
       py = py.lowwer()
       if py == "a"
	    typewriter(green + 'Hi! This is me! Zoom bot! Miss me! Well, I\'m going to assume, that you have no idea how to to anything with python!\nIt is one of the easiest languages to learn! It also capable of so much! From typing hello world, to creating discord bots and Nuraeul Networks! ')
	    time.sleep(2)
	    os.system('clear')
	    typewriter('So, why don\'t we get started!')
	    time.sleep(2)
	    os.system('clear')
	    
    elif classe == "b":
      typewriter('Hello fellow coders!')
      print(red + 'Imports')
  
