import os

c.JupyterHub.spawner_class = 'dockerspawner.SystemUserSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.DockerSpawner.remove = True
c.JupyterHub.hub_ip = os.environ['HUB_IP']
c.Spawner.default_url = '/lab'
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /cull_idle_servers.py --timeout=3600'.split(),
    },
]
c.Authenticator.admin_users = {'muy'}
c.SystemUserSpawner.host_homedir_format_string = os.environ['HOME_PREFIX'] + '/home/{username}'
c.NotebookApp.terminado_settings={'shell_command': ['bash']}
c.DockerSpawner.volumes = {
    "/usr/bin/docker": "/usr/bin/docker",
    "/usr/local/bin/docker-compose": "/usr/local/bin/docker-compose",
    "/var/run/docker.sock": "/var/run/docker.sock",
    "/etc/passwd": "/etc/passwd",
    "/etc/shadow": "/etc/shadow",
    "/etc/group": "/etc/group"
}