import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    AUTH_USER = os.environ.get('AUTH_USERS', '').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "𝗥𝗼𝘆 𝗝𝗮𝗮𝘁™"#Here You Can Change with Your Name  or any custom name or title you prefer


API_ID = 28227907
API_HASH = "bc3acb5bd0282fe4fd076cec1f24df62"
BOT_TOKEN = "8334590640:AAFqlvUVCsdiK153ZzfOULYLzmnp3zbeMB0"
OWNER_ID = 919335654
