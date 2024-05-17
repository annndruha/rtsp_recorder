import datetime
import logging
import os
import time
import traceback

import cv2

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

def moscow_time():
    delta = datetime.timedelta(hours = 3)  # MoscowUTC
    tzone = datetime.timezone(delta)
    return datetime.datetime.now(tzone)


def get_filename(url_rtsp: str) -> str:
    rtsp_folder = url_rtsp.split('@')[1].replace('/', '_').replace(':', '_')
    if not os.path.exists('data'):
        os.makedirs('data')
    directory = os.path.join('data', rtsp_folder)
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_name = os.path.join(directory, moscow_time().strftime("%Y_%m_%d__%H_%M_%S_%f.png"))
    return file_name


while True:
    try:
        with open('delay.txt') as f:
            delay = int(f.readline().strip())
        with open('rtsp_list.txt', 'r') as f:
            rtsp_list = [line.strip() for line in f.readlines()]
            delay_per_cam = int(delay/len(rtsp_list))
            logging.info(f'Sources count: {len(rtsp_list)}')
            logging.info(f'One camera delay (seconds): {delay}. Per cam delay: {delay_per_cam}')

        for rtsp_url in rtsp_list:
            cap = cv2.VideoCapture(rtsp_url)

            _, _ = cap.read()  # Skip some init frames
            _, _ = cap.read()
            ret, frame = cap.read()

            if not ret:
                logging.error(f'{rtsp_url}')
                continue

            logging.info(f'{get_filename(rtsp_url)}')
            time.sleep(delay_per_cam)
            cv2.imwrite(get_filename(rtsp_url), frame)
    except FileNotFoundError:
        logging.error('Did you forget create `delay.txt` and `rtsp_list.txt`?')
    except Exception as err:
        logging.error(err)
        traceback.print_tb(err.__traceback__)
