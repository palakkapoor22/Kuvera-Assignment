This is a basic front end of an application that takes purchase date, investment , fund house and selling date as inputs and provide with the final Investment amount on the selling date.NAV history as provided is used to calculate the amount which is stored as a text file. The file includes data only upto 30-May-2019 so a separate field of selling date has been included in the form.
This application also returns some exceptions as ValueError if the conditions do not meet.

To Run the application:
(In Ubuntu)

Requirements: 
1. Python3
2. Pip3
3. Django 2.0

To install pip3
sudo apt-get install python3-pip

To download Django use:
pip3 install Django==2.0

Getting started:

1. Download or clone the project from git repository.
2. Unzip the file.
3. Open a terminal inside the Kuvera-Assignment-master folder.
   Use: python3 manage.py runserver

This will start a server.

4. Go to local host as:
   localhost:8000

You will be able to view the front-end 
Enter the fields in the required place.

Eg. 
Date of purchase : 01-04-2015
Investment amount: 10000
Fund house: Axis Gold fund - Direct Plan - Dividend option
Date of selling : 30-05-2019

Next press submit to get the result.

Press 'enter more' to again enter new values.
Press 'exit' to exit from the application.

Note: the data doesn't contain NAV for all fund house for all the date values. So input must be given accordingly.
