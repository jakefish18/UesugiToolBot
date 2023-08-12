class Settings:
    # Bot settings.
    BOT_TOKEN = ""

    # Database settings.
    DATABASE_NAME = ""
    DATABASE_OWNER = ""
    DATABASE_PASSWORD = ""
    DATABASE_HOST = ""
    DATABASE_DRIVER = ""
    DATABASE_PORT = ""
    DATABASE_URI = (
        f"{DATABASE_DRIVER}://{DATABASE_OWNER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    )


settings = Settings()
