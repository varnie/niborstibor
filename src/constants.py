import os
from pathlib import Path

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
print(ROOT_DIR)

LOGS_DIR = Path(ROOT_DIR) / 'logs'
DATA_DIR = Path(ROOT_DIR) / 'data'

NIBOR_LAST = DATA_DIR / 'nibor_last.txt'
NIBOR_CSV = DATA_DIR / 'Nibor_Submissions.csv'

STIBOR_LAST = DATA_DIR / 'stibor_last.txt'
STIBOR_CSV = DATA_DIR / 'Stibor_Submissions.csv'

LOG_FILE = LOGS_DIR / 'app.log'

os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)
