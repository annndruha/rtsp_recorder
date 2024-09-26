import logging
import time
import traceback

from src.recorder import get_frames_from_all_sources

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    while True:
        try:
            get_frames_from_all_sources()
        except FileNotFoundError as err:
            logging.error('Did you forget create `settings.json`?')
            time.sleep(30)
        except Exception as err:
            logging.error(err)
            traceback.print_tb(err.__traceback__)
            time.sleep(30)
