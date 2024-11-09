# Uesugi tool bot
Telegram bot which helps you to learn by cards. Currently, the bot is offline, but you can host it in your own. Example of bot usage:
![](Example.png)

## Dependencies
To host by yourself, you need to have linux server with Python 3.11.5, PostgreSQL, and Redis installed.

## Installation and run
First, clone the repository to your machine where you want host the telegram bot and go to the project directory:
``` bash
git clone https://github.com/jakefish18/UesugiToolBot
cd UesugiToolBot
```

Second, it is not a required step, but I highly recommend to create `venv/` for the project
```bash
python3 -m venv venv/
source venv/bin/activate
```
In case you have fish shell:
```bash
python3 -m venv venv/
source venv/bin/activate.fish
```

Third, install the requirements
``` bash
pip3 install -r requirements.txt 
```

Fourth, create a `.env` file in `src` folder and fill it using `.env.example` as an example:
``` bash
# Bot settings.
BOT_TOKEN = ""

# Database settings.
DATABASE_URI = "postgresql://username:password@host:port/dbname"

# Redis settings
REDIS_HOST = localhost
REDIS_PORT = 6379

# Auth settings.
AUTH_TOKEN_EXPIRING_TIME = 0 # In seconds.
ACCESS_TOKEN_LENGHT_IN_BYTES = 0 # x2 symbols.
```
As you can see, you need to get the bot token from BotFather, install redis, and create a postgresql database.

Fifth, run the migrations:
``` bash
cd src
alembic upgrade head
```

Last, run the bot:
```bash
python3 main2.py
```

## Fun fact
It was planned to have website for the better management of the learning collections, so there is `frontend/` folder with some developments, but project is freezed now.