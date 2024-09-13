import os
import time
import json
import logging
import datetime
import traceback

import cv2

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def current_time(time_zone_delta: float):
    return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=time_zone_delta)))


def get_filename(url_rtsp: str, time_zone_delta: float) -> str:
    rtsp_folder = url_rtsp.split('@')[1].replace('/', '_').replace(':', '_')
    os.makedirs('data', exist_ok=True)
    directory = os.path.join('data', rtsp_folder)
    os.makedirs(directory, exist_ok=True)
    file_name = os.path.join(directory, current_time(time_zone_delta).strftime("%Y_%m_%d__%H_%M_%S_%f.png"))
    return file_name


while True:
    try:
        with open('settings.json') as f:
            settings = json.load(f)

        delay = int(settings['delay'])
        rtsp_list = settings['rtsp_sources_list']
        time_zone = settings['time_zone_delta']
        resize_to = tuple(settings['resize_to'])
        skip_frames = int(settings['skip_frames'])
        assert len(resize_to) == 2
        assert len(rtsp_list) > 0

        delay_per_cam = int(delay / len(rtsp_list))
        logging.info(f'Sources count: {len(rtsp_list)}. Resize to: [{resize_to[0]} {resize_to[1]}]')
        logging.info(f'One camera delay (seconds): {delay}. Per cam delay: {delay_per_cam}.')

        for rtsp_url in rtsp_list:
            cap = cv2.VideoCapture(rtsp_url)

            for _ in range(skip_frames):
                _, _ = cap.read()

            ret, frame = cap.read()

            if not ret:
                logging.error(f'{rtsp_url}')
                continue

            frame = cv2.resize(frame, resize_to)

            filename = get_filename(rtsp_url, time_zone)
            cv2.imwrite(filename, frame)
            logging.info(filename)
            time.sleep(delay_per_cam)

    except FileNotFoundError:
        logging.error('Did you forget create `settings.json`?')
        time.sleep(30)
    except Exception as err:
        logging.error(err)
        traceback.print_tb(err.__traceback__)
        time.sleep(30)
