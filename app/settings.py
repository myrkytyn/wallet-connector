import os
from dotenv import load_dotenv

load_dotenv()

MONOBANK_TOKEN = os.getenv("MONOBANK_TOKEN")
TIME_DIFFERENCE = os.getenv("TIME_DIFFERENCE")
DATA_DIRECTORY = os.getenv("DATA_DIRECTORY")
MONOBANK_DIRECTORY = os.getenv("MONOBANK_DIRECTORY")
ACCOUNT = os.getenv("ACCOUNT")
PERIOD = os.getenv("PERIOD")


MONOBANK_PATH = f"{DATA_DIRECTORY}/{MONOBANK_DIRECTORY}"
