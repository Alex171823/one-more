# Django HW

This is repository for Django projects made while learning in Hillel School

## Overview

This project runs locally. It has several apps with their own functional.


## Quick Start

To get apps up and running locally on your computer:
1. Set up the [Python virtual environment](https://docs.python.org/3/library/venv.html#module-venv).
2. Assuming you have Python setup, run the following commands:
   ```
   python install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser # Create a superuser
   python manage.py runserver
   ```


To run "__" app:
   
## ATTENTION
By default all apps run in `DEBUG` mode with the settings from **./DjangoBigProject/local_settings** for local development. 
If you want to enter `DEBUG=False` mode, change `DjangoBigProject.local_settings` in **./manage.py** file to `mysite.settings`
and re-run site.