import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H_%M-%S')}.log"
log_directory = os.path.join(os.getcwd(), "logs")  # Fixed this part
os.makedirs(log_directory, exist_ok=True)  # Ensure "logs" directory exists
LOG_FILE_PATH = os.path.join(log_directory, LOG_FILE)  # Use correct directory

logging.basicConfig(
    filename=LOG_FILE_PATH, 
    level=logging.INFO,  # Removed duplicate 'level' argument
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    logging.info("This is a test log message")
    print(f"Log file created at: {LOG_FILE_PATH}")
