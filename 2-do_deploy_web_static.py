#!/usr/bin/python3
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_deploy(archive_path):
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/
        archive_filename = archive_path.split('/')[-1]
        release_folder = "/data/web_static/releases/{}".format(
            archive_filename.split('.')[0]
        )
        run("mkdir -p {}".format(release_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_folder))

        # Remove the uploaded archive from the web server
        run("rm /tmp/{}".format(archive_filename))

        # Delete the current symbolic link
        current_link = "/data/web_static/current"
        if exists(current_link):
            run("rm {}".format(current_link))

        # Create a new symbolic link
        run("ln -s {} {}".format(release_folder, current_link))

        return True

    except Exception as e:
        return False
