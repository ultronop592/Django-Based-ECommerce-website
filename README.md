# Django-Based ECommerce Website (Core)

A Django project scaffold for an e-commerce style website, currently set up with a shared layout and basic pages (`Home`, `About`, `Contact`).

## Tech Stack

- Python 3.x
- Django 6.x (project generated with Django 6.0.1)
- SQLite (default database)
- Bootstrap 5 (CDN)

## Project Structure

```text
Core/
  manage.py
  db.sqlite3
  Core/
    settings.py
    urls.py
    wsgi.py
    asgi.py
  myapp/
    views.py
    urls.py
    models.py
    admin.py
    tests.py
  templates/
    base.html
    index.html
    about.html
    contact.html
  static/
    css/
      base.css
    js/
    img/
```

## Current Features

- Template inheritance using `base.html`
- Shared Bootstrap-based navbar and footer
- Basic route mapping in `myapp`
- Static files directory configured via `STATICFILES_DIRS`

## URL Routes

Configured in `Core/urls.py` and `myapp/urls.py`:

- `/` -> Home page (`index.html`)
- `/about/` -> About page (`about.html`)
- `/contact/` -> Contact page (`contact.html`)
- `/admin/` -> Django admin

## Local Setup

1. Open a terminal in this folder (`Core/`).
2. Create and activate a virtual environment.
3. Install dependencies.
4. Run migrations.
5. Start the development server.

### Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install django
python manage.py migrate
python manage.py runserver
```

### Open in Browser

- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Django App Notes

- `myapp/views.py` renders template pages:
  - `home` -> `index.html`
  - `about` -> `about.html`
  - `contact` -> `contact.html`
- `myapp/models.py` is currently empty and ready for future e-commerce models.

## Next Suggested Improvements

- Add product/category/cart/order models in `myapp/models.py`
- Add authentication (signup/login/logout)
- Add dynamic navbar links to real routes
- Connect static CSS (`static/css/base.css`) in templates using `{% load static %}`
- Add unit tests in `myapp/tests.py`

## Useful Commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
