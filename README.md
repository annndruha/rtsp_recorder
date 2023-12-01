# rtsp_recorder

Docker container for save RTSP frames from multiple sources.


### Run

* Create some folder for project (in folder). All next steps do in folder.

* Create `delay.txt` file with only one number: delay in seconds between saving frame from same source.

* Create `rtsp_list.txt` with sources, one per line:
    ```text
    rtsp://username:password@example.com:777/some/additional/url
    rtsp://username:password@example.com:999/some/additional/url
    ```
* Copy `docker-compose.yml` at target machine in same folder as files 
* Run:
    ```bash
    docker compose up -d
    ```
  
### Why files?
The script read files with delay and sources list in runtime loop. So, you can add or remove sources and change delay without restarting a container. (Docker volumes used.)