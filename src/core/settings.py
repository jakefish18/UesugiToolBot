from dotenv import dotenv_values

config = dotenv_values(".env")


class Settings:
    # Bot settings.
    BOT_TOKEN = config["BOT_TOKEN"]

    # Database settings.
    DATABASE_URI = config["DATABASE_URI"]


settings = Settings()
