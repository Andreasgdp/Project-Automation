import sys
import os
from github import Github

path = "C:/Users/<your username>/Documents/Projects/"

username = "" #Insert your github username here
password = "" #Insert your github password here

def create():
    folderName = str(sys.argv[1])
    newPath = str(path) + str(folderName)
    os.mkdir(newPath)
    user = Github(username, password).get_user()
    repo = user.create_repo(sys.argv[1])
    print("Succesfully created repository {}".format(sys.argv[1]))

if __name__ == "__main__":
    create()