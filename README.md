# Campus Skill Swap

This repository contains a Django project created for the Campus Skill Swap application.

## Setup

1. Activate the virtual environment:
   - PowerShell: `.\.venv\Scripts\Activate.ps1`

2. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Apply database migrations:
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the development server:
   ```powershell
   python manage.py runserver
   ```

5. Open the site in a browser at `http://127.0.0.1:8000/`.

## Project structure

- `campus_skillswap/` - Django project package
- `manage.py` - Django management utility
- `requirements.txt` - pinned Python dependencies

## Notes

The project uses Django installed in `.venv`.
