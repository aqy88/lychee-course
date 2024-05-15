FROM quay.io/jupyter/base-notebook
COPY ./requirements.txt /home/jovyan/work
USER root
RUN apt-get update && apt-get install -y gcc 
RUN pip install --no-cache -r /home/jovyan/work/requirements.txt