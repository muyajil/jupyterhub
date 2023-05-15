FROM jupyterhub/jupyterhub:latest

RUN pip install \
    dockerspawner

ADD cull_idle_servers.py /cull_idle_servers.py
ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
