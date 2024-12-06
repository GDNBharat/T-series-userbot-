import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "28362850")) #optional
API_HASH = getenv("API_HASH", "34f9cb93364db16fc45d003e4c81d97a") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "@DFSchinnaop").split()))
OWNER_ID = int(getenv("OWNER_ID", "7588442909"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://VamsixD:VamsixD@vamsi.x7gyybv.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "8090896989:AAEFJ7fLkr58XQ7DCFpANzX0njBj4XIR80s")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGwyGIApMJ1wDWnVmlHPM5-sJbl6F4XW9CYeG-W4hAF0KccqJvm3DaFc0NGM9y0xVsJ4fpG8qbJAqHxxT7uIRZdepMr0QxL_sMQjCMSoXIRm4YBNX5376lnJ4pdvDVXSt26vDP11DA6rhQzfM7MCDbYSc1vMQM2wOfqIIHdvwYXHe90MCmbHLZh9TRh4U7QktiZa6JX2SfYIfQCHYcGBO1gxtGzMzQdnJ4539w6IZALkomhfQFw6mTa6tJ70D_3XVSmCmOBgbir-fVA3ha63tC6jwvJ2cNpP3P-iaSqVB9aKA6B2UBUXGYvTJyaH8NJiVGeqHpZ80qH7d2ShMll2Izqf1WGxQAAAAHETnMdAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
