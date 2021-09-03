# Log Visualizer

A Django app to parse and visualize log files.

## How to start

##### Create project directory

`mkdir logvisualizer`

##### Change directory

`cd logvisualizer`

##### Clone the repository

`git clone https://github.com/shadmansakib/log-visualizer-django.git .`

##### Create a new virtual environment

`python3 -m venv venv`

> If you're on Windows and only python3 is installed on your system, you can use `python` instead of `python3`

##### activate virtualenv

- Linux/MacOS:

  `source venv/bin/activate`
- Windows:

  `venv\Scripts\activate`

##### Install dependencies

`pip install -r requirements.txt`

## Initial Setup and Run server

##### Set PostgreSQL Database configuration environment Variables:

`DB_NAME`: Database Name

`DB_USER`: Database username

`DB_PASSWORD`: Database password

`DB_HOST`: Database Host URL

`DB_PORT`: Database Port (Default is 5432)

##### Debug Mode:

By default debug mode is disabled.

Set `DEBUG=1` in environment to enable debug mode.

##### Run initial migration:

`python manage.py makemigrations`

`python manage.py migrate`

##### Create (admin) user:

`python manage.py createsuperuser`

##### Run django development server using the following command:

`python manage.py runserver`

## Parse log
A log parser management script is included in the django app.

Run the following command to parse the sample log file (`log`) included in the repository:

`python manage.py parselog log`

This command will clear all the existing logs and categories from database, then insert new logs.

`parselog` takes name of the log file (in this case `log`) as its positional argument.

There is an optional argument `-a`, `--append`, which will not clear the existing logs from the database before
inserting new ones.

To append new logs to database, run

`python manage.py parselog log -a`



