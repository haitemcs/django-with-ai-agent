# Django with AI Agent

Django learning project combining a Django backend with notebooks for authentication, permissions, documents, and AI-agent experiments.

## Stack

- Python
- Django 6.1
- Django ORM
- Jupyter notebooks

## Structure

    backend/
    ├── config/
    ├── documents/
    └── manage.py

    notebook/
    ├── 1-hello.ipynb
    ├── 2-django-user-perms.ipynb
    └── 3-django-build-in-permission.ipynb

## Backend

The Django application contains a `Document` model and explores Django users, permissions, authentication, and model relationships.

## Notebooks

- Django setup
- Users and permissions
- Built-in Django permissions
- Working with Django models
- Experiments before applying concepts in the Django project

## Run

    cd backend
    python manage.py migrate
    python manage.py runserver

## Technical focus

A learning project for understanding Django models, authentication and authorization, permissions, and connecting notebook experiments with a real Django application.
