# Getting Started

1. Navigate into project

```bash
cd django-vue-template
```

2. Create virtual environment and activate

```bash
python -m virutalenv venv
```

3. Install project requirements

```bash
pip install -r requirements.txt
```

4. Migrate database

```bash
python manage.py migrate
```

5. Run Django server

```bash
python manage.py runserver
```

6. Navigate to Vue App and install required packages

```bash
cd myproject/frontend
yarn install
```

7. Run Vue server

```bash
yarn run serve
```

8. django-vue-template is now running at localhost:8000