# Adding project path to python path
import sys

from dotenv import dotenv_values

config = dotenv_values(".env")
sys.path.append(config["PATH_TO_PROJECT"])

# Launching bot.
from src.telegram_bot import run_bot

run_bot()
