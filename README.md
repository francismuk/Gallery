# GALGALO GALLERY

## Description
This is a web application that allows users/mostly farmers to sign up, log in add problems,see problems or posts which other users can ccomment on, and delete. They can choose to update  their bio which includes their profile photo and posts they have posted they can also delete to write a pitch in and can view and comment.You also get your own page once you log in.

### By: FRANCIS MUKUHA

## Prerequisites
1. python3.6
2. Virtual environment(virtualenv)
3. Django

## Cloning and running
Clone the application using git clone(this copies the app onto your device). In your terminal:

    $ git clone https://github.com/Omtatah/FarmOverflow.git
    $ cd Gallery
    
Creating the virtual environment

    $ python3.6 -m venv --without-pip virtual
    $ source virtual/bin/env
    $ curl https://bootstrap.pypa.io/get-pip.py | python
    
Installing Flask and other Modules

    $ python3.6 install django===1.11
    $ python3.6 install django-bootstrap3
    
Run the application:

    $ python3.6 manage.py runserver
    
Testing the Application
To run the tests for the class files:

    $ python3.6 manage.py test
    
## Technologies Used
1. Python 3.6
2. Django
3. Bootstrap
4. HTML
5. Postgresql

## BDD
| Behavior           | Input                 | Outcome                            |
| -------------------|-----------------------| -----------------------------------|
| request page       | click horuku link url | view images          |
|view images according to categories or location| click on a category or location item   |    user goes to page containing similar item    |                      
|all images        | navebar home  | view all images          |
## Contact Information
For any questions, troubleshooting or contributions, find me on:
Email: mukd3v3lop3r@gmail.com

#### Known bugs
 - N/A

## License
[MIT](./License)
 Copyright (c) 2019 **Gallery**
