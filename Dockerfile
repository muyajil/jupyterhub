FROM jupyterhub/jupyterhub:1.0.0

RUN pip install \
    dockerspawner==0.10.0

ADD cull_idle_servers.py /cull_idle_servers.py
ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py