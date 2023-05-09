#!/usr/bin/python3
# Fabric script distributes archive to your servers


from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ["54.161.250.204"]


def do_pack():
        """Fabric script that generates a .tgz archive from web_static folder"""

        local("sudo mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_{}.tgz".format(date)
        result = local("sudo tar -cvzf {} web_static".format(filename))
        if result.succeeded:
            return filename
        else:
            return None


def do_deploy(archive_path):
    "Distribute archive"""

    if exists(archive_path) is False:
        return False
    filename = archive_path.split("/")[-1]
    no_tgz = '/data/web_static/releases/{}'.format(filename.split('.')[0])
    tmp = '/tmp/'+ filename

    try:
        put(archive_path, "/tmp/")
        sudo("mkdir -p {}/".format(no_tgz))
        sudo("tar -xzf {} -C {}/".format(tmp, no_tgz))
        sudo("rm {}".format(tmp))
        sudo("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        sudo("rm -rf {}/web_static".format(no_tgz))
        sudo("ln -s {}/ /data/web_static/current".format(no_tgz))
        return True

    except:
        return False

def deploy():
    """Create and distribute archive files to servers"""

    filename = do_pack()
    if exists(filename) is False:
        return False
    result = do_deploy(filename)
    return result
