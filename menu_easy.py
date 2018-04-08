#!/usr/bin/env python3

'''
python3 menu options helper
Author: GaDayas (https://github.com/GaDayas)
Version: 0.1
Date: 8 April 2018
'''
import os
import time
import colorama

time = str(time.strftime("%c"))
print("\033c")
print('=======================================================')
print("\t" + "\t" + time +  '                                 ')
print('                    EASY MENU                          ')
print('=======================================================')
print("\n")
# main menu

class gMenu:

    def mainMenu():
        print('MAIN MENU')
        print("1. Do something...anything       2. Do something else")
        print("3. Do something crazy            4. Quit")
        print("\n")
        
        selection=int(input("Enter choice: "))
        if selection==1:
	        print("\033c")
	        gMenu.anything()
        elif selection==2:
            print("\033c")
            gMenu.somethingElse()
        elif selection==3:
            print("\033c")
            gMenu.somethingCrazy()
        elif selection==4:
            confirm=input("Are you sure you want to exit?" "\n" + "Hit 'q' to quit or 'c' to continue: ")
            if confirm=='q':
                print("\033c")
                exit
        elif confirm=='c':
                print("\033c")
                gMenu.mainMenu()

        else:
                print("\n")
                print("\033c")
                print(colorama.Fore.RED + " ******* INVALID CHOICE: *********" + colorama.Fore.RESET)
                print("YOU MUST ENTER A NUMBER BETWEEN 1-4")
                print("\n")
                gMenu.mainMenu()

    # Menu option 1
    def anything():
        print("OPTION 1 FUNCTION!")
        getback=input("Enter r to return or q to quit: ")
        if getback=='r':
            print("\033c")
            gMenu.mainMenu()
        elif getback=='q':
            confirm =input("Are you sure you want to exit?" "\n" + "Hit 'q' to quit or 'c' to continue: ")
            if confirm=='q':
                print("\033c")
                exit
            elif confirm=='c':
                print("\033c")
                gMenu.mainMenu()
        else:
            print("Invalid input, exiting....")

    # Menu option 2
    def somethingElse():
        print("something else")
        getback=input("Enter r to return or q to quit: ")
        if getback=='r':
            print("\033c")
            gMenu.mainMenu()
        elif getback=='q':
            confirm =input("Are you sure you want to exit?" "\n" + "Hit 'q' to quit or 'c' to continue: ")
            if confirm=='q':
                print("\033c")
                exit
            elif confirm=='c':
                print("\033c")
                gMenu.mainMenu()
        else:
            print("Invalid input, exiting....")

    # Menu option 3
    def somethingCrazy():
        print("something crazy")
        getback=input("Enter r to return or q to quit: ")
        if getback=='r':
            print("\033c")
            gMenu.mainMenu()
        elif getback=='q':
            confirm =input("Are you sure you want to exit?" "\n" + "Hit 'q' to quit or 'c' to continue: ")
            if confirm=='q':
                print("\033c")
                exit
            elif confirm=='c':
                print("\033c")
                gMenu.mainMenu()
        else:
            print("\033c")
            print("Invalid input, Exiting....")

gMenu.mainMenu()
