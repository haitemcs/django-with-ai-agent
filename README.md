# Django Learning Project: Models, Users, and Permissions

A small Django learning repository focused on ORM fundamentals, a `Document` model, Django's built-in users and permissions, and experiments in Jupyter notebooks. Despite the repository name, the current tracked work is primarily Django learning material; an AI-agent implementation is not documented as part of the current codebase.

## What is included

- A Django project under `backend/`
- A `documents` app with a `Document` model
- Django admin and the default authentication/permission framework
- Notebooks exploring Django setup, users, and built-in permissions

## Repository layout

```text
django-with-ai-agent/
├── backend/
│   ├── manage.py
│   ├── config/
│   ├── documents/
│   └── db.sqlite3
├── notebook/
│   ├── 1-hello.ipynb
│   ├── 2-django-user-perms.ipynb
│   ├── 3-django-build-in-permission.ipynb
│   └── setup.py
├── LICENSE
└── README.md
```

The SQLite database is a local development artifact currently present in the repository. For a clean local setup, you can create a fresh database by removing that file before running migrations; do not delete it if you need the existing local data.

## Requirements

- Python 3.11 or newer compatible with the installed Django version
- pip
- Jupyter Notebook or JupyterLab to run the notebooks

Check the project's Django version in the installed environment before choosing a Python version.

## Run the Django project

From the repository root:

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment, then install Django if it is not already installed:

```bash
python -m pip install Django
```

Apply migrations and start the development server:

```bash
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/admin/ to access Django admin. The current URL configuration exposes the admin route; additional application endpoints are not currently configured.

To create an admin account:

```bash
python manage.py createsuperuser
```

## Run the notebooks

From the repository root:

```bash
python -m pip install notebook
jupyter notebook
```

Open the notebooks in the `notebook/` directory and run their cells in order. Some notebook cells may rely on the Django project and its database; read the setup cells before executing them.

## Learning objectives

- Django models and ORM operations
- Model relationships and timestamps
- User authentication concepts
- Built-in permissions and authorization
- Exploring Django behavior interactively before applying it in a project

## Current limitations

This is a learning project rather than a finished API. The current URL configuration only includes Django admin, and the document app's views are not yet implemented. The notebooks and code should be treated as evolving exercises.

## License

Distributed under the MIT License. See [LICENSE](LICENSE).
