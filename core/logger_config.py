import logging
from logging.handlers import TimedRotatingFileHandler
import os


LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)