# Installation, setup & usage
###### This guide is for windows only. See https://github.com/KalleHallden/ProjectInitializationAutomation for MAC-version.

## Install
1. ```git clone https://github.com/Andreasgdp/create-easy-repositories.git```
2. ```cd create-easy-repositories```
3. ```pip install -r requirements.txt```

## Setup
### ```create.py```
1. Set the path variable in the file ```create-repositories\create.py``` (line 5) to your desired projects folder. For example: 
```Python
5   path = "C:/Users/<your username>/Documents/Projects/"
```
2. Set the username and password variables to your github username and password in ```create-repositories\create.py``` (line 7 & 8). For example: 
```PYTHON
7   username = "<your GutHub username>" #Insert your github username here
8   password = "<your GutHub password>" #Insert your github password here
```
3. Place folder ```create-repositories``` here: ```C:\Users\<your username>\Documents\```, like this: ```C:\Users\<your username>\Documents\create-repositories\```.
### ```create.bat```
1. Insert your PS username in the first line of the file ```create.bat```, like this:
```BAT
1   cd C:\Users\<your username>\Documents\create-repositories\
```
2. Change the path in the third line to match the path for your projects in the ```create.py``` file, like this (```%1``` is taking the second argument that you type after create. See Usage): 
```BAT
3   cd C:\Users\<your username>\Documents\Projects\%1
```
3. Change the fith line so that your GitHub username is in the link. like this:
```BAT
5   git remote add origin https://github.com/<your GitHub username>/%1.git
```
4. Change the last line to your code launcher command. If you use VS code it is ```code .``` and with VS code insiders it is ```code-insiders .```. If you don't have such a command, you can just delete the line.
5. Place file ```create.bat``` here: ```C:\Windows\System32```. You will need administrator permission for this.

## Usage
1. To run the script type ```create <name of your new repository>``` in your preferred terminal.

