from dotenv import load_dotenv

load_dotenv()

class Config: pass
    

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
