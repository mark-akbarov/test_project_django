# Test Django App

## Getting Started

### Create Database

```bash
>>> create database test_db;
>>> create user test_user with password '2404';
>>> grant all privileges on database test_db to test_user;
```

### Clone and install the app

```bash
>>> git clone https://github.com/mark-akbarov/test_project/
>>> virtualenv .venv
>>> source .venv/bin/activate
>>> source .env
>>> pip install -r requirements.txt
>>> python manage.py migrate

```
