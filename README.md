# rtsp_recorder

Docker container for save RTSP .png frames from multiple sources in attached volume `data`.


### Run

#### Clone repo
```bash
git clone https://github.com/annndruha/rtsp_recorder && cd rtsp_recorder
```
#### Add configs

* Create `delay.txt` file with only one number: delay in seconds between saving frame from same source.
    ```bash
    nano delay.txt
    ```
* Create `rtsp_list.txt` with sources, one per line:
    ```bash
    nano rtsp_list.txt
    ```
    ```text
    rtsp://username:password@example.com:777/some/additional/url
    rtsp://username:password@example.com:999/some/additional/url
    ```

#### Run docker 
```bash
docker compose up -d
```
Docker create a volume named `data` and starts save frames form different sourses in corresponding folders.
  
### Why config files?
The script read files with delay and sources list in runtime loop. So, you can add or remove sources and change delay without restarting a container. (Docker volumes used.)
