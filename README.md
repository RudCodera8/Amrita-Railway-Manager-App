# Amrita Railway Manager App
Amrita Railway Manager App is a simple CLI app for Reserving , Cancelling and checking status of your ticket. This is a project based on OOP concepts in python.

* [More about the project](#More-about-the-project)
* [Installation](#Installation)
* [Technologies used](#Technologies-used)



### More about the project
This project is based on OOP concepts of python and user can communicate with the program using the Terminal. Basically an end user can Book, cancel and view status of his tickets booked according to the train availablity set by the admin in the same App. So as soon as the admin adds train details, the user can book tickets using the train number and his/her details. A PNR number would be provided at the same instant using which the user can check the status and cancel his ticket. 

### Installation 
Just clone or download the repository on your machine. It just needs an editor to run. The app doesnt need any kind of server such as SQL, it basically works on .dat/.csv or .json (the programmer has to code accordingly, initial commit has .dat file support)

## Technologies used
1) python 2.x and 3.x
2) various inbuilt python libraries 
  a) pickle - for loading and dumping .dat files (can also csv or json )
  b) time - for just pausing the program for making it more realistic
  c) random -  for generating random PNRs
  d) os - for handling the files (here its .dat type)


