#!/usr/bin/python3
# Fabric script distributes archive to your servers


from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ["18.234.107.48", "54.161.250.204"]

def do_deploy(archive_path):
    "Distribute archive"""

    if exists(archive_path) is False:
        return False
    filename = archive_path.split("/")[-1]
    no_tgz = '/data/web_static/releases/{}'.format(filename.split('.')[0])
    tmp = '/tmp/'+ filename

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        run("ln -s {}/ /data/web_static/current".format(no_tgz))
        return True

    except:
        return False
