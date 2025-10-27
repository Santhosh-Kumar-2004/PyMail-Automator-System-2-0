import logging
from logging.handlers import TimedRotatingFileHandler
import os

# Ensure the logs folder exist or not
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


LOG_FILE = os.path.join(LOG_DIR, "app.log")