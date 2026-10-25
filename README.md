# Django portfolio demo

A small portfolio site: project index, project pages, skills, and a contact form
that saves messages to the database. Content is managed in the Django admin.

## Run it

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations portfolio
python manage.py migrate
python manage.py seed_demo         # sample projects and skills
python manage.py createsuperuser   # for /admin/
python manage.py runserver
```

Open http://127.0.0.1:8000/ and http://127.0.0.1:8000/admin/.

## Make it yours

- Name, role, email and GitHub link: `portfolio/context.py`
- Projects and skills: the admin, or edit `portfolio/management/commands/seed_demo.py`
- Colors and fonts: variables at the top of `static/css/style.css`

## Tests

```bash
python manage.py test
```

## Before deploying

Set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0` and `DJANGO_ALLOWED_HOSTS`, run
`python manage.py collectstatic`, and serve static files with WhiteNoise or your web server.
Contact emails are not sent in this demo; messages are stored and visible in the admin.
