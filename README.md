# Messaging App

## Installation

- Create and activate virtual environment:

Navigate to 'messaging_backend', and run:

```bash
python3.6 -m venv ./.venv
source ./.venv/bin/activate
python3.6 -m pip install -r requirements.txt
```

- Create local db:

Navigate to 'messaging_backend/messaging_app'

```bash
sudo -u postgres psql
```

It's look like:

```bash
postgres=#
```

Now, insert

```bash
CREATE DATABASE messaging_app;
```

if you don't have user, create:

```bash
CREATE user postgres with encrypted password '123456';
```

and then,

```bash
grant all privileges on database postgres to postgres;
\q
```

Open settings.py file and verify your credentials:

```code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'messaging_app',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

- And now running migrate:

```bash
python manage.py migrate
```

## Running

- Run the microservice:

```bash
python manage.py runserver
```

- Run unit tests:

```bash
python manage.py test
```

## You can use Postman to try this API! :)

Examples:

- Try to send message:

/api/send_message/?sender=Dor&recipient=Keren&message=Hi Keren, how are you today? :)

- Try to get messages of recipient:

/api/messages?recipient=Keren

---

### Enjoy

#### ✨Dor Shamir Ⓒ✨
