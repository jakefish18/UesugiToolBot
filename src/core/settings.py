from dotenv import dotenv_values

# .env file must be placed in src folder.
config = dotenv_values(".env")

class Settings:
    # Site settings.
    FRONTEND_DOMAIN = "127.0.0.1:3000"
    BACKEND_DOMAIN = "127.0.0.1:8000"

    # Bot settings.
    BOT_TOKEN = config["BOT_TOKEN"]

    # Database settings.
    DATABASE_URI = config["DATABASE_URI"]

    # Redis settings.
    REDIS_HOST = config["REDIS_HOST"]
    REDIS_PORT = config["REDIS_PORT"]

    # Auth settings.
    AUTH_TOKEN_EXPIRING_TIME = int(config["AUTH_TOKEN_EXPIRING_TIME"])
    ACCESS_TOKEN_LENGHT_IN_BYTES = int(config["ACCESS_TOKEN_LENGHT_IN_BYTES"])


settings = Settings()
