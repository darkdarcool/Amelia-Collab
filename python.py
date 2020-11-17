import os, random, time, sys 
score = 0
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
 print('Score = ' + str(score))
 typewriter('Here are your choices for classes\n')
 print('a) Beginner')
 print('b) Intermedate')
 classe = input('')
 if classe == "a":
    os.system('clear')
    typewriter('Welcome beginners! Here are a few classes that are availible!\n' + red)
    print('a) print function')
    print()
    print('b) Variables')
    print()
    print('c) In print functions')
    print()
    print('d) If, elif')
    print()
    py = input(bcyan + 'Which course?\n').lower()
    py = py.lower()
    if py == "a":
      os.system('clear')
      typewriter(green + 'Hi! This is me! Zoom bot! Miss me? Well, I\'m going to assume, that you have no idea how to to anything with python!\nIt is one of the easiest languages to learn! It also capable of so much! From typing hello world, to creating discord bots and Nuraeul Networks! ')
      time.sleep(2)
      os.system('clear')
      typewriter('So, why don\'t we get started!')
      time.sleep(2)
      os.system('clear')
      typewriter('The print function, the most basic thing to know about python, it\'s like the printf in c++/c, and the console.log in Java. So, here is how to do this.')
      time.sleep(2)
      os.system('clear')
      typewriter('print(\'Hello world!\')\n')
      typewriter('You can clearly see the print typed out, but there are parenthesies after to show what your are typing. The there are quots. You can use anykind of quot you want for the print function. Whatever you type in the quots will be printed out!\n')
      time.sleep(2)
      typewriter('Now I think it is only fair that you try!' + red + '\nONLY USE SINGLE QUOTS' + green + ' Type\nprint(\'Hello World\')')
      q1 = input(cyan + '\n').lower()
      q1 = q1.lower()
      if q1 == 'print(\'hello world\')' and 'print("hello world")':
        typewriter(green + 'Great!')
        typewriter('Looks like you go the right answer.')
        time.sleep(2)
        os.system('clear')
        typewriter('You completed the lesson!!\nCongrats! Now you get a badge for your efforts!')
        score + 1
        time.sleep(2)
        os.system('clear')
        python()
      else:
        print(green + 'HMMMMM, I think you typed something wrong.  I think you may need a little help.  ')
        time.sleep(5)
        os.system('clear')
        os.system('python3 help.py')
    elif py == "b":
      typewriter(green + 'Looks like you wanna learn variables huh? Well I, Zoom bot will gladly teach you ')
      time.sleep(2)
      os.system('clear')
      typewriter('')

      
	    
 elif classe == "b":
    typewriter('Hello fellow coders!')
    print()
    print(red + 'Imports')

python()
  
  
