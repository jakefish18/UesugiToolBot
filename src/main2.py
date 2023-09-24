# Adding project path to python path
import sys

from dotenv import dotenv_values

config = dotenv_values(".env")
sys.path.append(config["PATH_TO_PROJECT"])


from src import telegram_bot

if __name__ == "__main__":
    telegram_bot.run_bot()
