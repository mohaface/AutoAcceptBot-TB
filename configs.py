from os import getenv

class Config:
    API_ID = int(getenv("API_ID", "11057906"))
    API_HASH = getenv("API_HASH", "b7f975dcdf30c826b3e6178ff3f72356")
    BOT_TOKEN = getenv("BOT_TOKEN", "8014214381:AAEfhqObVjMJnqucsc4nOIUBLCeDuDgxwXc")
    FSUB = getenv("FSUB", "tmusicranger_1")
    CHID = int(getenv("CHID", "-1002353460983"))
    SUDO = list(map(int, getenv("SUDO", "6864201346").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://m33537924:JLBRhGx8FLxy43c@cluster0.zy8ld.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    # New configuration for required channels
    REQUIRED_CHANNELS = getenv("REQUIRED_CHANNELS", "tmusicranger_1").split(',')

cfg = Config()
