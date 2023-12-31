# Adding project path to python path
import sys

from dotenv import dotenv_values

config = dotenv_values(".env")
sys.path.append(config["PATH_TO_PROJECT"])

from src.api import api
