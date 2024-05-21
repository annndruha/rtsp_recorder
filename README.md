# rtsp_recorder

Docker container for save RTSP frames from multiple sources in attached volume `data`.


### Run

#### Clone repo and go to directory
```bash
git clone https://github.com/annndruha/rtsp_recorder && cd rtsp_recorder
```
#### Setup your sources
Copy template setting.json
```bash
mv settings_example.json settings.json
```
Change `rtsp_sources_list` links in settings.json (and other parameters if you want)
```json
{
  "rtsp_sources_list": [
    "rtsp://login:password@source1.com:5554/additional/url",
    "rtsp://login:password@source2.com:5554/additional/url"
  ],
  "time_zone_delta": 3,
  "delay": 60,
  "resize_to": [1920, 1080],
  "skip_frames": 1
}
```

#### Run docker container
```bash
docker compose up -d
```
Docker create a volume named `data` and starts save frames form different sources in corresponding folders.
  
### Change settings
The script read settings.json in runtime loop. So, you can add or remove sources and change delay without restarting a container.
