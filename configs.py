from os import getenv

class Config:
    API_ID = int(getenv("API_ID", "13602725"))
    API_HASH = getenv("API_HASH", "1b10ef3c3fc08c5d3134d67d15ff42fc")
    BOT_TOKEN = getenv("BOT_TOKEN", "7209810551:AAFenA9M5Rqdnf-P0TjNsQNh57GekfFoBqM")
    FSUB = getenv("FSUB", "or3kii")
    CHID = int(getenv("CHID", "-1002012969670"))
    SUDO = list(map(int, getenv("SUDO", "6265954306").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Tandav2:TandavBotsDB@tandav2.qkdxrpn.mongodb.net/mydatabase?retryWrites=true&w=majority&appName=tandav2")
    
    # New configuration for required channels
    REQUIRED_CHANNELS = getenv("REQUIRED_CHANNELS", "@or3kii,@or3kii").split(',')

cfg = Config()
