#!/bin/bash
docker container run -it -p 10000:8888 \
    -v "%cd%/data-volume":/home/jovyan/work \
    myjupyter