from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "sessionjaze")
BOT_TOKEN = getenv("8749491505:AAFsPvNEIWVPwOyYnT5e1f5m_nagejHLqj8")
THUMB_IMG = getenv("THUMB_IMG", "https://i.hizliresim.com/j1qk53i.jpg")
BOT_NAME = getenv("BOT_NAME", "🎧 Jaze Müzik")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("JazeMusicBot") 
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "L7XSohbet")
PLAYLIST_NAME = getenv("PLAYLIST_NAME", "ThroneFm") 
ASSISTANT_NAME = getenv("Jaze Asistan")
OWNER = getenv("OWNER", "yikmaz")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
PLAYLIST_ID = int(getenv("PLAYLIST_ID"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8234857464").split()))
