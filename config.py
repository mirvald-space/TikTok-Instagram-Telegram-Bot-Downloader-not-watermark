# config.py

import os

from dotenv import load_dotenv

load_dotenv()

# Базовая директория проекта
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Временная директория для хранения загруженных видео
TEMP_DIRECTORY = os.path.join(BASE_DIR, 'temp_videos')
BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')
RAPIDAPI_HOST = "social-media-video-downloader.p.rapidapi.com"
WEBHOOK_PATH = os.getenv('WEBHOOK_PATH')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

# MongoDB configuration
MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_DB_NAME = os.getenv('MONGODB_DB_NAME')
MONGODB_USERS_COLLECTION = os.getenv('MONGODB_USERS_COLLECTION')
MONGODB_COUPONS_COLLECTION = os.getenv('MONGODB_COUPONS_COLLECTION')

# User management configuration
ADMIN_IDS = list(map(int, os.getenv('ADMIN_IDS', '').split(',')))
FREE_LIMIT = int(os.getenv('FREE_LIMIT', 3))
