from os import getenv

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "")
    CHID = int(getenv("CHID", "-1002177395485"))
    SUDO = list(map(int, getenv("SUDO", "").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
    # New configuration for required channels
    REQUIRED_CHANNELS = getenv("REQUIRED_CHANNELS", "Or3kii").split(',')

cfg = Config()
