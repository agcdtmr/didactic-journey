# didactic-journey

## To Do:

- Doing: Following along the Django [Documentation](https://docs.djangoproject.com/en/4.1/intro/tutorial04/)
- Change the port. `python manage.py runserver 8080`

## What I want to accomplish

- Connect filter_jobs_form.html or searh_results with api

## What exactly do I want to accomplish? Most important to least important.

- Let users(women career switchers or tech newbies or juniors) browse all the jobs in tech in Europe in one page
- Let users check one specific job in a new window or page
- Let users filter the jobs per location, salary, job position, work condition(full/part time, remote/wfh/wfo/hybrid), Diversity & Inclusion, Company Size, Company Industry
- Let users share a job advert in their social medias or network
- Let users sign-up / login to save jobs they are interested in
- Let users delete saved jobs
- Let users log out, but still when they log back in again, they would have their saved jobs available on their profile page

## How to run

1. Go to our GitHub [repo](https://github.com/agcdtmr/didactic-journey).
2. Fork or clone our project to your local directory.
3. Install the python libraries below if necessary:
4. Open the repo using pycharm or any IDE.
5. Or open your terminal `cd didactic-journey/mysite`
6. `python manage.py runserver`
7. Click the given 'http://127.0.0.1:8000/'

Home: http://127.0.0.1:8000
Form to filter: http://127.0.0.1:8000/filter_jobs_form
Display the results: http://127.0.0.1:8000/search_results

## Steps made building this project

1. Install Python 3.9 (to verify `python -v`)
2. Find an api - [The Muse](https://www.themuse.com/developers/api/v2)
3. Create api.py to get data back from the api and check if it's working and usable
4. Decide which web framework to use along with Python
5. Install Django 4.1.3 - `python -m pip install Django` (to verify `python -m django --version`)
6. Started Django project `django-admin startproject mysite`
7. Creating an admin user `python manage.py createsuperuser` `http://127.0.0.1:8000/admin/`
8. Created simple html templates
9. Created search engine form

## Files:

- didactic-journey/mysite: root directory
- didactic-journey/mysite/manage.py: command-line utility that lets us interact with this Django project
- didactic-journey/mysite/mysite: actual Python package for the project
- didactic-journey/mysite/mysite/**init**.py: An empty file that tells Python that this directory should be considered a Python package.
- didactic-journey/mysite/mysite/settings.py: Settings/configuration for this Django project
- didactic-journey/mysite/mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
- didactic-journey/mysite/mysite/asgi.py: An entry-point for ASGI-compatible web servers to serve your project.
- didactic-journey/mysite/mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project.
