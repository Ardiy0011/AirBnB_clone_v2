#!/usr/bin/python3
"""model to deploy archive"""
from fabric.api import env, run
from os.path import exists
from datetime import datetime
from fabric.api import local
import os

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_pack():
    """function that manipulates files on server"""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)

    local("mkdir -p versions")

    """Change directory to versions"""
    with lcd("versions"):
        local("tar -czvf {} ../web_static".format(archive_name))

    return "versions/{}".format(archive_name)


def do_deploy(archive_path):
    """function to deploy archive"""
    if not exists(archive_path):
        return False

    try:
        """Upload the archive to /tmp/ directory on the web server"""
        put(archive_path, '/tmp/')

        """Extract the archive to /data/web_static/releases"""
        archive_filename = archive_path.split('/')[-1]
        release_folder = "/data/web_static/releases/{}".format(
            archive_filename.split('.')[0]
        )
        run("mkdir -p {}".format(release_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_folder))

        """Remove the uploaded archive from the web server"""
        run("rm /tmp/{}".format(archive_filename))

        """Delete the current symbolic link"""
        current_link = "/data/web_static/current"
        if exists(current_link):
            run("rm {}".format(current_link))

        """Create a new symbolic link"""
        run("ln -s {} {}".format(release_folder, current_link))

        return True

    except Exception as e:
        return False


def deploy():
    """function to deply actually"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
