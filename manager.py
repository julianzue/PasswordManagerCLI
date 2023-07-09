from colorama import Fore, init
from getpass import getpass
import time
import os
import platform


init()


#colors
y = Fore.LIGHTYELLOW_EX
c = Fore.LIGHTCYAN_EX
r = Fore.LIGHTRED_EX
re = Fore.RESET


#variables
normal = c + "[*] " + re
entry = y + "[+] " + re
error = r + "[!] " + re

class Manager():
    def __init__(self):
        print("")

        print(normal + "Welcome! Please login.")
        self.login()

    
    def login(self):
        print("")

        self.user = input(entry + "User: ")
        self.password = getpass(entry + "Password: ")

        if self.user == "julian" and self.password == "password":
            print("")
            self.start()
        else:
            print(error + "Failed. Please try again!")
            self.login()


    def start(self):
        print(normal + "Hello " + c + self.user.capitalize() + re + "!")
        
        self.prompt()


    def prompt(self):
        print("")

        prompt_all = input(entry)

        prompt = prompt_all.split(" ")[0]

        if prompt == "add":
            self.add()

        elif prompt == "list":
            self.list_all()

        elif prompt == "search":
            query = prompt_all.split(" ")[1]
            self.search(query)

        elif prompt == "exit" or prompt == "q":
            print("")
            print(error + "Application closed!")
            print("")
            quit()

        elif prompt == "clear":
            if platform.system() == "Windows":
                os.system("cls")
            else:
                os.system("clear")
            print(normal + "Screen cleared!")
            self.prompt()

        else:
            print("")
            print(error + "Command unknown!")
            self.prompt()


    def add(self):
        print("")

        name = input(entry + y + "Name: " + re)
        user = input(entry + y + "User: " + re)
        password = input(entry + y + "Password: " + re)

        with open("logins/" + name.lower() + ".txt", "a") as f:
            f.write("name: " + name + "\n")
            f.write("time: " + time.strftime("%a %Y-%m-%d %H:%M") + "\n")
            f.write("user: " + user + "\n")
            f.write("pass: " + password + "\n")
            f.close()

        print(normal + "Login successfull added! to " + c + name.lower() + ".txt" + re + "!")
        
        self.prompt()

    
    def list_all(self):
        for login in os.scandir("logins/"):
            
            print("")
            
            with open("logins/" + login.name, "r") as f:
                for line in f.readlines():
                    split = line.strip("\n").split(": ")

                    if split[0] == "name":
                         print(normal + c + split[1] + re)
                    else:
                        print(normal + split[1])

        self.prompt()

    
    def search(self, query):
        for login in os.scandir("logins/"):
            
            name = login.name

            if query in name:

                print("")

                with open("logins/" + name, "r") as f:
                    for line in f.readlines():
                        split = line.strip("\n").split(": ")

                        if split[0] == "name":
                            print(normal + c + split[1] + re)
                        else:
                            print(normal + split[1])

        self.prompt()

Manager()