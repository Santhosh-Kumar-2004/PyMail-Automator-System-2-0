import logging
from logging.handlers import TimedRotatingFileHandler
import os

# Ensure the logs folder exist or not
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


# app.log files path existence...
LOG_FILE = os.path.join(LOG_DIR, "app.log")

#Created the logger here
logger = logging.getLogger("PyMailLogger")
logger.setLevel(logging.INFO)


# Create a rotating file handler logger ( New file daily, backup for 7 days.)
handler = TimedRotatingFileHandler(LOG_FILE, when="midnight", interval=1, backupCount=7, encoding="utf-8")
handler.suffix = "%Y-%m-%d"