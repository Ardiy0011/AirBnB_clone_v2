#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)

    local("mkdir -p versions")

    # Change directory to 'versions'
    with lcd("versions"):
        local("tar -czvf {} ../web_static".format(archive_name))

    return "versions/{}".format(archive_name)
