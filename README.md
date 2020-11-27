# Amrita Railway Manager App
Amrita Railway Manager App is a simple CLI app for Reserving , Cancelling and checking status of your ticket. This is a project based on OOP concepts in python.


## Table of contents 
* [More about the project](#More-about-the-project)
* [Installation](#Installation)
* [Technologies used](#Technologies-used)
* [Running the project](#Running-the-project)
* [Advantages of the project](#Advantages-of-the-project)
* [Difficulties faced](#Difficulties-occured-during-the-project)
* [Future plans for the project](#Future-plans-for-the-project)


### More about the project
This project is based on OOP concepts of python and user can communicate with the program using a Terminal. Basically an end user can Book, cancel and view status of his tickets booked according to the train availablity set by the admin in the same App. So as soon as the admin adds train details, the user can book tickets using the train number and his/her details. A PNR number would be provided at the same instant using which the user can check the status and cancel his ticket. 

### Installation 
Just clone or download the repository on your machine. It just needs an editor to run. The app doesnt need any kind of server such as SQL, it basically works on .dat/.csv or .json (the programmer has to code accordingly, initial commit has .dat file support)

## Technologies used
1) python 2.x and 3.x
2) various inbuilt python libraries 
  a) pickle - for loading and dumping .dat files (can also csv or json )
  b) time - for just pausing the program for making it more realistic
  c) random -  for generating random PNRs
  d) os - for handling the files (here its .dat type)
  
## Running the project 
Just make sure to save all files in same folder, and if you are using VsCode type Editiors, make sure your workspace is set on that folder.

## Advantages of the project
1) Light weight, fast stable code following OOP concepts making editing and code reusablity easy.
2) For saving the files we aint using any SQL based server, its simply .dat files for now. The programmer can change to CSV or JSON files as per their convenience. 
3) Easy debugging and error free, developer friendly code. 

## Difficulties occured during the project
1) Since this was a group project we had a difficulty of python versions, the main programmer had a older version of python(2.x) and others had 3.x, so integrating had some time consumed. 
2) Steps included coding the project in OOP concepts which needed control and remeberance of a function used, so had some difficulties at that stage.

## Future Plans for the project
1) Plans to scale the project by connecting this to cloud server and using SSH make the app usablity more wider. For eg: A user can communicate with the project either using the Web app or CLI. 
