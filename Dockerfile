FROM jupyter/scipy-notebook
COPY ./requirements.txt /home/jovyan/work
RUN python -m pip install --no-cache -r /home/jovyan/work/requirements.txt