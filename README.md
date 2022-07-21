![GitHub](https://img.shields.io/github/license/LaGGgggg/NeedBuy?label=License%3A)
![GitHub watchers](https://img.shields.io/github/watchers/LaGGgggg/NeedBuy)
![GitHub last commit](https://img.shields.io/github/last-commit/LaGGgggg/NeedBuy)

# NeedBuy

Online store on django.

# Requirements

python >= **3.10**<br>
python packages: [requirements.txt](NeedBuy/requirements.txt) (How install in "How to start the project?")<br>
[git](https://git-scm.com/downloads) (For project installation)

# How to start the project?

### 1. Clone this repository

```bash
git clone https://github.com/LaGGgggg/NeedBuy.git
cd NeedBuy
```

### 2. Create the virtualenv:

#### With [pipenv](https://pipenv.pypa.io/en/latest/):

```bash
pip install --user pipenv
pipenv shell  # create and activate
```

#### Or classic:

```bash
python -m venv .venv  # create
.venv\Scripts\activate.bat   # activate
```

### 3. Install [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

## For local server:

### 4. Install python packages

```bash
pip install -r requirements.txt
```

### 5. Add environment variables

Create file `.env` in `NeedBuy/app_main`, such it `NeedBuy/app_main/.env`. Next, paste it in `.env`:
```
SECRET_KEY=

# If empty => return False, else => return True.
DEBUG=True
```
You need to add SECRET_KEY (It can be random, this is a good [site](https://djecrety.ir/).)

### 6. Change directory

```bash
cd NeedBuy
```

### 7. Create directory for logs

```bash
mkdir .logs
```

### 8. Run database migrations

```bash
python manage.py migrate
```

### 9. Run development server

```bash
heroku local -f Procfile_local
```

## For heroku server:

### 4. Sign up for a heroku account if you don't have one: [heroku.com](https://heroku.com/)

### 5. Login to heroku in console

```bash
heroku login
```

### 6. Create app

```bash
heroku create <your app name>
heroku git:remote -a <your app name>
```

### 7. Setting app environment variables

```bash
heroku config:set DEBUG=  # Should be empty for production deploy
heroku config:set SECRET_KEY= <your secret_key>  # It can be random, this is a good site: https://djecrety.ir/
```

### 8. Push project to heroku

```bash
git subtree push --prefix NeedBuy heroku main
```

### 9. Setting up web dyno (Without it, you won't be able to see the site)

```bash
heroku ps:scale web=1
```

### 10. Open your website

```bash
heroku open
```

# Current project structure

Soon......

# Contacts

For any questions:<br>
TulNik0@yandex.ru

# License

#### [LICENSE.md](LICENSE.md)
