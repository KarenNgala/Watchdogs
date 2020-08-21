# Watchdogs
A web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handymen to meeting announcements or even alerts.

## Getting Started

To get a copy of the project up and running on your local machine for development and testing purposes, 
1. **clone** this repository 
   ``` 
   git clone https://github.com/KarenNgala/Watchdogs
   ```
2. Set up a Python development environment that includes; Python, **pip** & **a virtual environment** 
   ```bash
   $ python3.6 -m venv --without-pip virtual

   $ source virtual/bin/activate

   (virtual) $ curl https://bootstrap.pypa.io/get-pip.py | python
   ```

### Prerequisites

1. Install project **dependencies**
   ```sh
    (virtual) $ pip install -r requirements.txt
    ```
* See deployment for notes on how to deploy the project on a live system.

### Installing

1.  To get a development env running, use the **.env.example** file to create your own **.env** file.
2.  Create a **postgres** db and add the credentials to .env file
```
(virtual)$ psql
pc-name=#  CREATE DATABASE <name>;
```
3.  Apply initial migrations
```sh 
(virtual) $ python manage.py migrate 
```
4. Make migrations to your database
```sh
(virtual) $ python manage.py makemigrations application
(virtual) $ python manage.py migrate
```
5. Create admin account
```
(virtual) $ python manage.py createsuperuser
```
6.  Start development server
```
 (virtual) $ python3 manage.py runserver
 ```

## Running the tests

Run automated tests for this system

```sh
(virtual) $ python3 manage.py test application
```

## Deployment

With all environment variables changed to suit your local copy of this repository, deploy the application to [Heroku](https://medium.com/@hdsingh13/deploying-django-app-on-heroku-with-postgres-as-backend-b2f3194e8a43) to see it live

## Built With

* [Django 3.1](https://www.djangoproject.com/) - The web framework used
* [Heroku](https://www.heroku.com/platform) -  Deployment platform
* [Python3.6](https://www.python.org/) - Backend logic
* [Postresql](https://www.postgresql.org/) - Database system


## Authors

* [Karen Ngala](https://github.com/KarenNgala)
* [Mercy Njoroge](https://github.com/Mercy-Njoroge)
* [Bryson Mundia](https://github.com/Bryson69)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details