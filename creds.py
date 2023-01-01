import os
#from dotenv import load_dotenv, find_dotenv

#load_dotenv(find_dotenv())


class Credentials:
    BOT_TOKEN = os.environ.get("5985869623:AAEYkxV3pTAcedqt7EyAcmiat5rk2axiKRc")  # from @botfather
    API_ID = int(os.environ.get("14055090"))  # from https://my.telegram.org/apps
    API_HASH = os.environ.get("a46f7b439d0afa45b7a69fc450f754e9")  # from https://my.telegram.org/apps
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS","5716680911").split())

# Okay 🤣
