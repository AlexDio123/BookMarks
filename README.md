# BookMarks
Social media app that allows users to share images that they find on the internet.

# Installation

before running locally the project make sure to have created and activated a python virtual enviroment, you can see how to do that [here.](https://docs.python.org/3/tutorial/venv.html) once you're done with that follow this steps:

- run the command: **pip install requirements.txt**
- edit your local file etcs/hosts and add the line: 127.0.0.1 **mysite.com**
- make sure you have [redis](https://redis.io/) installed and running on your device.
- run the command: **python manage.py runserver_plus --cert-file cert.crt**

this should be enough to run the project.

# Features

- Local and social authentication for users
- JavaScript bookmarklet to share images from other websites
- Follow system for users
- activity section
- view counts and likes
- editing the user profiles
 
and more! this project was made following the django 3 by example of antonio mele, it uses ajax views with jquery, third party apis, redis, django signals and best development practices.
