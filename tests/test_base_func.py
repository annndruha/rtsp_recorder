import datetime
import os
import shutil
import unittest

from src.recorder import get_filename, load_settings


class FuncTests(unittest.TestCase):
    def test_get_filename(self):
        url_rtsp = 'rtsp://login:password@source1.com:5554/additional/url'
        time_zone_delta = 3

        filename = get_filename(url_rtsp, time_zone_delta)

        data_source_folder, filename = os.path.split(filename)
        data_folder, source_folder = os.path.split(data_source_folder)

        self.assertTrue(source_folder == 'source1.com_5554_additional_url')
        self.assertTrue(data_folder == 'data')

        dt = datetime.datetime.strptime(filename, "%Y_%m_%d__%H_%M_%S_%f.png")
        dt_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=time_zone_delta))).replace(tzinfo=None)

        self.assertTrue(abs(dt_now - dt) < datetime.timedelta(seconds=0.1))

    def test_load_settings(self):
        shutil.copyfile('settings_example.json', 'settings.json')
        delay, rtsp_list, time_zone, resize_to, skip_frames, delay_per_cam = load_settings()
        my_rtsp_list = ["rtsp://login:password@source1.com:5554/additional/url",
                        "rtsp://login:password@source2.com:5554/additional/url"]
        my_resize_to = (1920, 1080)
        self.assertTrue(delay == 60)
        self.assertEqual(rtsp_list, my_rtsp_list)
        self.assertTrue(time_zone == 3)
        self.assertEqual(resize_to, my_resize_to)
        self.assertTrue(skip_frames == 1)
        self.assertTrue(delay_per_cam == 30)


if __name__ == "__main__":
    unittest.main()
