# User Profile with Django

Step to get the project running.

0. Initialize a new virtual environment of your choosing. I use:
    `python -m venv .env` and `source .env/bin/activate`

A predefined build task has been made for users of Visual Studio code in `.vscode/tasks.json`
Or:

1. Use the `pip install -4 requirements.txt` file to install the project dependencies.

2. Run your migrations to create the tables in the database.
   `python manage.py migrate`

3. Run the server.
   `python manage.py runserver`
